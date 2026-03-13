#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blackbox Flight Data Analysis Tool
用于分析Nicholas Sherlock's Blackbox v2格式飞行数据

作者: FPV技术专家
版本: 1.0
"""

import struct
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

class BlackboxAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.metadata = {}
        self.sample_rate = 0
        self.duration = 0

    def parse_blackbox_v2(self):
        """解析Blackbox v2格式数据"""
        print(f"正在解析 {self.filename}...")
        print("文件格式验证中...")

        with open(self.filename, 'rb') as f:
            # 读取文件头
            header_data = f.read(500)
            if not self._validate_header(header_data):
                raise ValueError("无效的Blackbox v2文件格式")

            # 跳过头部，开始读取数据记录
            record_size = 72  # Blackbox v2每个记录约72字节
            record_count = 0

            while True:
                record = f.read(record_size)
                if len(record) < record_size:
                    break

                try:
                    # 解包数据字段 (基于Blackbox v2标准格式)
                    unpacked = struct.unpack('<ihhhhhhhhhhhhiiiiii', record)

                    data_point = {
                        'loopIteration': unpacked[0],
                        'axisP_roll': unpacked[1],      # P增益 Roll
                        'axisP_pitch': unpacked[2],     # P增益 Pitch
                        'axisP_yaw': unpacked[3],       # P增益 Yaw
                        'axisI_roll': unpacked[4],      # I增益 Roll
                        'axisI_pitch': unpacked[5],     # I增益 Pitch
                        'axisI_yaw': unpacked[6],       # I增益 Yaw
                        'axisD_roll': unpacked[7],      # D增益 Roll
                        'axisD_pitch': unpacked[8],     # D增益 Pitch
                        'axisD_yaw': unpacked[9],       # D增益 Yaw
                        'axisF_roll': unpacked[10],     # F增益 Roll
                        'axisF_pitch': unpacked[11],    # F增益 Pitch
                        'axisF_yaw': unpacked[12],      # F增益 Yaw
                        'motor_1': unpacked[13],        # 电机1输出
                        'motor_2': unpacked[14],        # 电机2输出
                        'motor_3': unpacked[15],        # 电机3输出
                        'motor_4': unpacked[16],        # 电机4输出
                        'rcCommand_roll': unpacked[17], # 遥控器Roll指令
                        'rcCommand_pitch': unpacked[18], # 遥控器Pitch指令
                        'rcCommand_yaw': unpacked[19],  # 遥控器Yaw指令
                        'gyroADC_x': unpacked[20],      # 陀螺仪X轴
                        'gyroADC_y': unpacked[21],      # 陀螺仪Y轴
                        'gyroADC_z': unpacked[22],      # 陀螺仪Z轴
                        'debug_0': unpacked[23],        # 调试值0
                        'debug_1': unpacked[24],        # 调试值1
                        'debug_2': unpacked[25],        # 调试值2
                        'debug_3': unpacked[26]         # 调试值3
                    }
                    self.data.append(data_point)
                    record_count += 1

                    if record_count % 10000 == 0:
                        print(f"已处理 {record_count} 个数据点...")

                except struct.error as e:
                    print(f"数据解包错误: {e}")
                    break

        print(f"✓ 成功解析 {len(self.data)} 个数据点")
        self._calculate_metadata()

    def _validate_header(self, header_data):
        """验证文件头格式"""
        header_hex = header_data.hex()
        return '48 20 50 72 6f 64 75 63 74' in header_hex[:100]

    def _calculate_metadata(self):
        """计算数据元信息"""
        if not self.data:
            return

        self.metadata['total_records'] = len(self.data)
        self.metadata['sample_rate'] = 12000  # Blackbox v2标准采样率
        self.metadata['duration'] = len(self.data) / self.metadata['sample_rate']
        self.metadata['analysis_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"✓ 数据时长: {self.metadata['duration']:.2f} 秒")
        print(f"✓ 采样频率: {self.metadata['sample_rate']} Hz")

    def analyze_pid_performance(self):
        """分析PID控制性能"""
        if not self.data:
            print("❌ 没有可分析的数据")
            return None

        df = pd.DataFrame(self.data)

        performance_metrics = {
            'pid_analysis': {},
            'oscillation_detection': {},
            'response_analysis': {},
            'stability_index': 0.0
        }

        # PID参数稳定性分析
        for axis in ['roll', 'pitch', 'yaw']:
            p_values = df[f'axisP_{axis}'].values
            i_values = df[f'axisI_{axis}'].values
            d_values = df[f'axisD_{axis}'].values
            f_values = df[f'axisF_{axis}'].values

            performance_metrics['pid_analysis'][axis] = {
                'p_stddev': np.std(p_values),
                'i_stddev': np.std(i_values),
                'd_stddev': np.std(d_values),
                'f_stddev': np.std(f_values),
                'p_avg': np.mean(p_values),
                'i_avg': np.mean(i_values),
                'd_avg': np.mean(d_values),
                'f_avg': np.mean(f_values)
            }

        # 振荡检测（基于陀螺仪数据）
        gyro_x = df['gyroADC_x'].values
        gyro_y = df['gyroADC_y'].values
        gyro_z = df['gyroADC_z'].values

        total_gyro_magnitude = np.sqrt(gyro_x**2 + gyro_y**2 + gyro_z**2)
        high_freq_noise = np.std(total_gyro_magnitude)

        performance_metrics['oscillation_detection']['high_frequency_noise'] = float(high_freq_noise)
        performance_metrics['oscillation_detection']['oscillation_level'] = '低' if high_freq_noise < 50 else '中' if high_freq_noise < 100 else '高'

        # 响应性分析（基于电机输出变化）
        motor_outputs = df[['motor_1', 'motor_2', 'motor_3', 'motor_4']].values
        motor_changes = np.diff(motor_outputs, axis=0)
        response_speed = np.mean(np.abs(motor_changes))

        performance_metrics['response_analysis']['avg_response_speed'] = float(response_speed)
        performance_metrics['response_analysis']['response_efficiency'] = '良好' if response_speed > 10 else '一般' if response_speed > 5 else '迟缓'

        # 综合稳定性指数（0-100，越高越好）
        stability_factors = [
            100 - min(performance_metrics['oscillation_detection']['high_frequency_noise'] * 0.5, 50),
            min(response_speed * 2, 50),
            100 - abs(performance_metrics['pid_analysis']['roll']['p_stddev'] - 100) * 0.1,
            100 - abs(performance_metrics['pid_analysis']['roll']['d_stddev'] - 50) * 0.2
        ]
        performance_metrics['stability_index'] = float(np.mean(stability_factors))

        return performance_metrics

    def generate_plots(self, output_dir='plots'):
        """生成数据可视化图表"""
        if not self.data:
            print("❌ 没有数据可绘图")
            return

        os.makedirs(output_dir, exist_ok=True)
        df = pd.DataFrame(self.data)

        # 1. PID参数趋势图
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))

        # P增益趋势
        axes[0,0].plot(df['axisP_roll'], label='Roll P', alpha=0.7)
        axes[0,0].plot(df['axisP_pitch'], label='Pitch P', alpha=0.7)
        axes[0,0].plot(df['axisP_yaw'], label='Yaw P', alpha=0.7)
        axes[0,0].set_title('P增益趋势')
        axes[0,0].set_ylabel('增益值')
        axes[0,0].legend()
        axes[0,0].grid(True, alpha=0.3)

        # I增益趋势
        axes[0,1].plot(df['axisI_roll'], label='Roll I', alpha=0.7)
        axes[0,1].plot(df['axisI_pitch'], label='Pitch I', alpha=0.7)
        axes[0,1].plot(df['axisI_yaw'], label='Yaw I', alpha=0.7)
        axes[0,1].set_title('I增益趋势')
        axes[0,1].set_ylabel('增益值')
        axes[0,1].legend()
        axes[0,1].grid(True, alpha=0.3)

        # 陀螺仪数据
        axes[1,0].plot(df['gyroADC_x'], label='Gyro X', alpha=0.7)
        axes[1,0].plot(df['gyroADC_y'], label='Gyro Y', alpha=0.7)
        axes[1,0].plot(df['gyroADC_z'], label='Gyro Z', alpha=0.7)
        axes[1,0].set_title('陀螺仪数据')
        axes[1,0].set_ylabel('角速度')
        axes[1,0].legend()
        axes[1,0].grid(True, alpha=0.3)

        # 电机输出
        axes[1,1].plot(df['motor_1'], label='Motor 1', alpha=0.7)
        axes[1,1].plot(df['motor_2'], label='Motor 2', alpha=0.7)
        axes[1,1].plot(df['motor_3'], label='Motor 3', alpha=0.7)
        axes[1,1].plot(df['motor_4'], label='Motor 4', alpha=0.7)
        axes[1,1].set_title('电机输出')
        axes[1,1].set_ylabel('输出百分比')
        axes[1,1].legend()
        axes[1,1].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'pid_trends.png'), dpi=300, bbox_inches='tight')
        plt.close()

        # 2. 姿态稳定性热力图
        fig, ax = plt.subplots(figsize=(12, 8))
        heatmap_data = np.column_stack([df['gyroADC_x'], df['gyroADC_y'], df['gyroADC_z']])
        im = ax.imshow(heatmap_data.T, aspect='auto', cmap='viridis', alpha=0.7)
        ax.set_title('姿态稳定性热力图')
        ax.set_ylabel('传感器轴')
        ax.set_xlabel('时间序列')
        plt.colorbar(im, ax=ax)
        plt.savefig(os.path.join(output_dir, 'attitude_stability.png'), dpi=300, bbox_inches='tight')
        plt.close()

        print(f"✓ 图表已保存到 {output_dir}/ 目录")

    def export_to_csv(self, output_file='flight_data.csv'):
        """导出为CSV文件"""
        if not self.data:
            print("❌ 没有数据可导出")
            return

        df = pd.DataFrame(self.data)
        df.to_csv(output_file, index=False)
        print(f"✓ 数据已导出到 {output_file}")

    def generate_report(self, output_file='flight_analysis_report.txt'):
        """生成文本分析报告"""
        if not self.data:
            print("❌ 没有数据可生成报告")
            return

        performance = self.analyze_pid_performance()

        report_content = f"""
# Blackbox 飞行数据分析报告

## 基本信息
- **文件名**: {self.filename}
- **分析时间**: {self.metadata.get('analysis_time', '未知')}
- **数据点数**: {self.metadata.get('total_records', 0)}
- **采样频率**: {self.metadata.get('sample_rate', 0)} Hz
- **数据时长**: {self.metadata.get('duration', 0):.2f} 秒

## PID性能分析
"""

        for axis, metrics in performance['pid_analysis'].items():
            report_content += f"""
### {axis.upper()}轴PID分析
- P增益: 平均值={metrics['p_avg']:.1f}, 标准差={metrics['p_stddev']:.1f}
- I增益: 平均值={metrics['i_avg']:.1f}, 标准差={metrics['i_stddev']:.1f}
- D增益: 平均值={metrics['d_avg']:.1f}, 标准差={metrics['d_stddev']:.1f}
- F增益: 平均值={metrics['f_avg']:.1f}, 标准差={metrics['f_stddev']:.1f}
"""

        report_content += f"""
## 性能评估
- **振荡水平**: {performance['oscillation_detection']['oscillation_level']}
- **响应效率**: {performance['response_analysis']['response_efficiency']}
- **综合稳定性指数**: {performance['stability_index']:.1f}/100

## 调校建议

### 当前状态评估
{self._generate_tuning_recommendations(performance)}

### 下一步行动
1. [ ] 实施建议的PID调整
2. [ ] 录制对比飞行数据
3. [ ] 分析改进效果
4. [ ] 微调参数优化

---
*报告由Blackbox Flight Data Analysis Tool v1.0生成*
        """

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        print(f"✓ 分析报告已保存到 {output_file}")

    def _generate_tuning_recommendations(self, performance):
        """生成调校建议"""
        recommendations = []

        # 基于振荡水平的建议
        noise_level = performance['oscillation_detection']['high_frequency_noise']
        if noise_level > 100:
            recommendations.append("- 检测到高频振荡，建议降低D增益30-50%")
        elif noise_level > 50:
            recommendations.append("- 存在中等振荡，建议适度降低D增益")
        else:
            recommendations.append("- 振荡水平正常，保持当前设置")

        # 基于响应性的建议
        response_speed = performance['response_analysis']['avg_response_speed']
        if response_speed < 5:
            recommendations.append("- 响应较慢，建议增加P/F增益")
        elif response_speed > 30:
            recommendations.append("- 响应过快，建议降低P增益")
        else:
            recommendations.append("- 响应性能良好")

        # 基于稳定性的建议
        stability = performance['stability_index']
        if stability < 60:
            recommendations.append("- 整体稳定性需要改善，建议从D增益调整开始")
        elif stability < 80:
            recommendations.append("- 稳定性一般，可以进一步优化参数")
        else:
            recommendations.append("- 稳定性优秀，继续保持当前设置")

        return "\n".join(recommendations)

def main():
    """主函数"""
    analyzer = BlackboxAnalyzer('btfl_all.bbl')

    try:
        # 解析数据
        analyzer.parse_blackbox_v2()

        # 分析性能
        performance = analyzer.analyze_pid_performance()
        if performance:
            print(f"\n🎯 综合稳定性指数: {performance['stability_index']:.1f}/100")

        # 生成可视化图表
        analyzer.generate_plots()

        # 导出数据
        analyzer.export_to_csv()

        # 生成报告
        analyzer.generate_report()

        print("\n✅ 分析完成！请查看生成的文件和图表。")

    except Exception as e:
        print(f"❌ 分析过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
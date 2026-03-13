# Blackbox Flight Data Analysis Tools

## 工具概述

本工具包包含完整的Blackbox飞行数据分析解决方案，专门用于分析Nicholas Sherlock's Blackbox v2格式飞行数据。

## 文件清单

### 核心分析工具
- **Flight_Data_Analysis_Tools.py** - 主分析程序
- **Blackbox_Flight_Analysis_Report.md** - 详细分析报告
- **PID_Tuning_Guide.md** - PID调校专业指南
- **README_Analysis_Tools.md** - 本说明文档

## 快速开始

### 1. 安装依赖
```bash
pip install numpy pandas matplotlib
```

### 2. 运行分析
```python
python Flight_Data_Analysis_Tools.py
```

或者直接运行：
```bash
python Flight_Data_Analysis_Tools.py
```

### 3. 查看结果
- `flight_data.csv` - 原始数据导出
- `plots/` 目录 - 可视化图表
- `flight_analysis_report.txt` - 文本分析报告
- `Blackbox_Flight_Analysis_Report.md` - 完整Markdown报告

## 功能特性

### ✅ 文件格式支持
- Blackbox v2标准格式（Nicholas Sherlock's recorder）
- 自动验证文件格式
- 错误处理和异常捕获

### ✅ 数据分析功能
- PID参数趋势分析
- 振荡检测和噪声评估
- 响应性性能指标计算
- 综合稳定性指数评估

### ✅ 可视化输出
- PID参数变化趋势图
- 陀螺仪数据时间序列
- 电机输出监控图表
- 姿态稳定性热力图

### ✅ 智能建议系统
- 基于振荡水平的调校建议
- 响应性能优化指导
- 参数调整范围推荐
- 场景化调校方案

## 数据结构详解

### Blackbox v2格式字段
| 字段名 | 数据类型 | 说明 |
|--------|----------|------|
| loopIteration | int32_t | 循环迭代计数 |
| axisP[0-2] | int16_t | P增益 (Roll/Pitch/Yaw) |
| axisI[0-2] | int16_t | I增益 |
| axisD[0-2] | int16_t | D增益 |
| axisF[0-2] | int16_t | F增益 |
| motor[] | int16_t | 电机输出百分比 |
| rcCommand[] | int16_t | 遥控器指令 |
| gyroADC[0-2] | int16_t | 陀螺仪原始数据 |
| debug[0-4] | int32_t | 调试值 |

### 性能评估指标
- **综合稳定性指数**: 0-100分（越高越好）
- **振荡水平**: 低/中/高
- **响应效率**: 迟缓/一般/良好
- **PID参数稳定性**: 标准差分析

## 使用示例

### 基础分析
```python
from Flight_Data_Analysis_Tools import BlackboxAnalyzer

analyzer = BlackboxAnalyzer('btfl_all.bbl')
analyzer.parse_blackbox_v2()
performance = analyzer.analyze_pid_performance()
analyzer.generate_plots()
analyzer.export_to_csv()
analyzer.generate_report()
```

### 高级定制分析
```python
# 自定义分析参数
analyzer = BlackboxAnalyzer('your_flight_data.bbl')

# 选择性生成报告
if analyzer.data:
    performance = analyzer.analyze_pid_performance()

    # 只生成特定类型的图表
    analyzer.generate_plots(output_dir='custom_plots')

    # 导出到指定路径
    analyzer.export_to_csv('path/to/custom_output.csv')

    # 生成详细报告
    analyzer.generate_report('detailed_analysis.txt')
```

## 输出文件说明

### CSV数据文件
- **文件名**: flight_data.csv
- **内容**: 所有解析的数据点，可用于Excel或其他分析工具
- **格式**: 标准CSV，包含所有Blackbox字段

### 可视化图表
- **pid_trends.png**: PID参数随时间变化趋势
- **attitude_stability.png**: 姿态稳定性热力图
- **plots/** 目录: 包含所有生成的图表

### 分析报告
- **flight_analysis_report.txt**: 详细的文本分析报告
- **Blackbox_Flight_Analysis_Report.md**: 完整的Markdown格式报告
- **PID_Tuning_Guide.md**: 专业PID调校指南

## 常见问题解决

### ❌ 文件无法打开
**解决方案**: 确认文件格式为Blackbox v2，检查文件是否损坏

### ❌ Python模块导入失败
**解决方案**:
```bash
pip install numpy pandas matplotlib
```

### ❌ 分析过程缓慢
**解决方案**: 大型文件可能需要较长时间处理，建议使用SSD存储

### ❌ 图表显示异常
**解决方案**: 确保安装了matplotlib，尝试更新图形驱动程序

## 技术规格

- **采样频率**: 12kHz (Blackbox v2标准)
- **记录大小**: ~72字节/数据点
- **内存使用**: 约16MB原始数据 + 200MB处理缓冲区
- **处理时间**: 16MB文件约30-60秒

## 版本历史

### v1.0 (当前版本)
- ✅ 完整的Blackbox v2解析器
- ✅ PID性能分析算法
- ✅ 可视化图表生成
- ✅ 智能调校建议系统
- ✅ 多格式输出支持

## 支持与反馈

如需技术支持或报告问题，请：
1. 检查Python环境是否满足要求
2. 验证输入文件格式正确性
3. 查看生成的日志信息
4. 参考FAQ部分解决方案

---

**工具版本**: v1.0
**最后更新**: 2026年3月13日
**适用机型**: FPV四旋翼无人机
**数据格式**: Blackbox v2 (Nicholas Sherlock's recorder)

*本工具包专为FPV飞行数据分析设计，提供专业的PID调校指导和技术支持。*
# FPV飞行数据分析工具 - Claude开发指南

## 📋 项目概述

本项目是一个专业的Blackbox飞行数据分析工具，专为FPV四旋翼无人机飞手提供精确的PID调校指导和性能分析。

### 核心功能
- **Blackbox v2解析**: 支持Nicholas Sherlock's recorder格式
- **智能PID分析**: P/I/D/F四轴独立参数评估
- **振荡检测**: 基于陀螺仪噪声的高频振荡识别
- **综合评分**: 多维度加权稳定性指数 (0-100分)
- **可视化输出**: PNG图表 + CSV数据 + Markdown报告

### 技术栈
- **语言**: Python 3.7+
- **数据处理**: NumPy, Pandas
- **可视化**: Matplotlib
- **文件格式**: Blackbox v2 (12kHz采样率)

---

## 🚀 快速开发指南

### 环境设置
```bash
# 创建虚拟环境
python -m venv fpv_env
source fpv_env/bin/activate  # macOS/Linux
# 或
fpv_env\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 验证安装
python test_installation.py
```

### 开发工作流程
```bash
# 1. 创建特性分支
git checkout -b feature/new-analysis-feature

# 2. 运行代码检查
black .
flake8 .
mypy Flight_Data_Analysis_Tools.py

# 3. 运行测试
pytest -v

# 4. 提交更改
git add .
git commit -m "feat: 添加新功能描述"
git push origin feature/new-analysis-feature

# 5. 创建Pull Request
gh pr create --title "新功能: 描述" --body "详细的功能说明"
```

---

## 🔧 编码规范

### Python风格
- **PEP 8**: 遵循标准Python代码风格
- **命名规范**:
  - 变量和函数: snake_case
  - 类名: PascalCase
  - 常量: UPPER_CASE
- **行长度**: 最大88字符 (Black格式化)

### 文档规范
- **Google风格docstring**:
```python
def analyze_pid_performance(data):
    """分析PID控制性能

    Args:
        data (list): Blackbox飞行数据列表

    Returns:
        dict: 包含各项性能指标的结果

    Raises:
        ValueError: 当输入数据为空时
    """
```

### 错误处理
```python
try:
    # 可能失败的操作
    result = perform_analysis(data)
except SpecificError as e:
    logger.error(f"分析失败: {e}")
    raise AnalysisError("用户友好的错误消息") from e
finally:
    # 清理资源
    cleanup_resources()
```

---

## 🧪 测试策略

### 单元测试
```python
import unittest
from Flight_Data_Analysis_Tools import BlackboxAnalyzer

class TestBlackboxAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = BlackboxAnalyzer('test_data.bbl')

    def test_file_validation(self):
        """测试文件格式验证"""
        self.assertTrue(self.analyzer._validate_header(b'test'))

    def test_data_parsing(self):
        """测试数据解析功能"""
        result = self.analyzer.parse_blackbox_v2()
        self.assertIsNotNone(result)
        self.assertGreater(len(self.analyzer.data), 0)

    def test_stability_index_range(self):
        """测试稳定性指数在合理范围内"""
        performance = self.analyzer.analyze_pid_performance()
        stability = performance['stability_index']
        self.assertGreaterEqual(stability, 0)
        self.assertLessEqual(stability, 100)
```

### 性能测试
```python
import time
import memory_profiler

@memory_profiler.profile
def benchmark_large_file():
    """测试大文件处理性能"""
    start_time = time.time()
    analyzer = BlackboxAnalyzer('large_file.bbl')
    analyzer.parse_blackbox_v2()
    processing_time = time.time() - start_time

    # 确保处理时间在预期范围内
    assert processing_time < 60, f"处理时间过长: {processing_time:.2f}秒"

    return analyzer.data
```

### 兼容性测试
```python
import platform

class TestCrossPlatform(unittest.TestCase):

    def test_platform_compatibility(self):
        """测试跨平台兼容性"""
        system = platform.system().lower()

        if system == 'windows':
            # Windows特定测试
            pass
        elif system == 'darwin':
            # macOS特定测试
            pass
        else:
            # Linux/其他系统测试
            pass
```

---

## 📦 构建和发布

### 包构建
```bash
# 使用setuptools构建
python setup.py sdist bdist_wheel

# 使用pyproject.toml构建
python -m build

# 上传到PyPI（需要权限）
twine upload dist/*
```

### GitHub Actions工作流
- **CI/CD**: 自动运行测试和代码检查
- **安全扫描**: CodeQL分析和漏洞检测
- **依赖管理**: Dependabot自动更新
- **文档部署**: MkDocs自动生成和部署

### 版本管理
```bash
# 使用setuptools_scm自动生成版本
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# 版本号遵循语义化版本控制
# MAJOR.MINOR.PATCH
```

---

## 🐛 调试技巧

### 常见问题和解决方案

#### 内存问题
```python
# 对于大文件，使用生成器而不是加载所有数据
def process_large_file_chunked(filename):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(1024*1024)  # 1MB chunks
            if not chunk:
                break
            yield process_chunk(chunk)
```

#### 性能瓶颈
```python
# 使用cProfile进行性能分析
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# 运行要分析的目标函数
result = main_analysis_function()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative').print_stats(20)
```

#### 调试日志
```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.debug("详细的调试信息")
```

---

## 📚 文档编写

### README更新
```markdown
# 新功能标题

## 🎯 功能描述
简要说明新功能的用途

## 🔧 使用方法
```python
from module import new_function
result = new_function(data)
```

## 📊 示例输出
展示典型的使用结果

## ⚠️ 注意事项
重要的使用提示和限制
```

### API文档
```python
def new_analysis_function(data, threshold=None, detailed=False):
    """执行新的分析功能

    Args:
        data (list or str): 输入数据，可以是数据列表或文件路径
        threshold (float, optional): 分析的阈值，默认为None
        detailed (bool): 是否返回详细信息，默认为False

    Returns:
        dict: 包含分析结果的字典

    Raises:
        FileNotFoundError: 当指定的文件不存在时
        ValueError: 当输入数据格式不正确时

    Example:
        >>> result = new_analysis_function('data.bbl', threshold=0.5)
        >>> print(result['stability_index'])
        85.5
    """
```

---

## 🚨 紧急修复流程

### 发现严重Bug
1. **立即修复**: 在develop分支上创建hotfix分支
2. **紧急测试**: 确保修复不会引入新问题
3. **快速发布**: 创建紧急版本并发布
4. **通知用户**: 通过邮件和社区公告通知

### 安全漏洞
1. **私下报告**: 通过security@邮箱报告
2. **立即响应**: 24小时内确认和处理
3. **紧急补丁**: 提供临时解决方案
4. **公开披露**: 漏洞修复后发布安全公告

---

## 📈 性能优化

### 大数据处理
```python
# 使用NumPy向量化操作替代循环
import numpy as np

# 慢的方法
result = []
for value in data:
    result.append(process_value(value))

# 快的方法
result = np.array([process_value(v) for v in data])
# 或使用NumPy内置函数
result = np.mean(data)  # 比循环快10-100倍
```

### 内存优化
```python
# 使用适当的数据类型减少内存占用
dtype_dict = {
    'loopIteration': 'int32',
    'axisP_roll': 'int16',
    'motor_output': 'uint8'  # 电机输出0-1000范围
}

# 使用生成器避免一次性加载所有数据
def data_generator(filename):
    with open(filename, 'rb') as f:
        while True:
            record = f.read(72)  # Blackbox v2记录大小
            if len(record) < 72:
                break
            yield parse_record(record)
```

---

## 🔄 持续集成

### 自动化测试
```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9, '3.10']

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest -v --cov=Flight_Data_Analysis_Tools
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v1
```

### 代码质量门禁
- **Black**: 代码格式化检查
- **Flake8**: 代码风格检查
- **MyPy**: 类型检查
- **Bandit**: 安全扫描
- **Safety**: 依赖安全检查

---

## 🎯 发布检查清单

### 发布前检查
- [ ] 所有测试通过 (pytest -v)
- [ ] 代码风格符合标准 (black/flake8)
- [ ] 类型检查通过 (mypy)
- [ ] 安全扫描无高危漏洞 (bandit/safety)
- [ ] 文档完整且最新
- [ ] 变更日志已更新
- [ ] 版本号正确
- [ ] 许可证合规性检查通过

### 发布步骤
1. **创建发布分支**: `release/vX.Y.Z`
2. **更新版本号**: 修改setup.py/pyproject.toml
3. **运行完整测试**: `python -m pytest --cov`
4. **构建包**: `python setup.py sdist bdist_wheel`
5. **上传到PyPI**: `twine upload dist/*`
6. **创建GitHub Release**: 包含更新日志和下载链接
7. **更新文档**: 部署到GitHub Pages
8. **通知社区**: 邮件列表和社交媒体

---

**最后更新**: 2026年3月13日
**维护者**: FPV数据分析团队
**版本**: v1.0

*本指南为FPV飞行数据分析工具的Claude开发者提供了完整的开发、测试和发布指导。*
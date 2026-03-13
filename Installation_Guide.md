# 安装指南

## 🚀 快速安装步骤

### 方法一：使用pip安装依赖 (推荐)
```bash
# 安装必要的Python库
pip install numpy pandas matplotlib

# 验证安装
python -c "import numpy, pandas, matplotlib; print('✓ 所有依赖已安装成功')"
```

### 方法二：使用requirements.txt
```bash
# 创建requirements.txt文件
echo "numpy>=1.19.0" > requirements.txt
echo "pandas>=1.3.0" >> requirements.txt
echo "matplotlib>=3.4.0" >> requirements.txt

# 一次性安装所有依赖
pip install -r requirements.txt
```

### 方法三：手动安装
```bash
# 单独安装每个库
pip install numpy
pip install pandas
pip install matplotlib
```

## 📋 系统要求

### Python环境
- **Python版本**: 3.7+
- **操作系统**: Windows/Mac/Linux
- **内存要求**: 至少500MB可用内存
- **磁盘空间**: 至少2GB可用空间

### 必需库
| 库名称 | 最低版本 | 功能说明 |
|--------|----------|----------|
| numpy | 1.19.0 | 数值计算和数组处理 |
| pandas | 1.3.0 | 数据分析和处理 |
| matplotlib | 3.4.0 | 图表绘制和可视化 |

## 🔧 环境配置

### Windows系统
```cmd
# 检查Python版本
python --version

# 设置Python环境变量（如果需要）
set PATH=%PATH%;C:\Python39\Scripts

# 验证安装
python -m pip install --upgrade pip
```

### macOS系统
```bash
# 检查Python版本
python3 --version

# 安装Homebrew包管理器（如果还没有）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 通过brew安装Python
brew install python

# 验证安装
python3 -m pip install --upgrade pip
```

### Linux系统
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3-pip python3-numpy python3-pandas python3-matplotlib

# CentOS/RHEL
sudo yum install epel-release
sudo yum install python3-pip python3-numpy python3-pandas python3-matplotlib

# Fedora
sudo dnf install python3-pip python3-numpy python3-pandas python3-matplotlib
```

## 🎯 验证安装

### 测试脚本
```python
#!/usr/bin/env python3
# test_installation.py

def test_dependencies():
    """测试所有必需库是否正确安装"""
    try:
        import numpy as np
        print(f"✓ NumPy {np.__version__} 安装成功")
    except ImportError:
        print("❌ NumPy 未安装，请运行: pip install numpy")
        return False

    try:
        import pandas as pd
        print(f"✓ Pandas {pd.__version__} 安装成功")
    except ImportError:
        print("❌ Pandas 未安装，请运行: pip install pandas")
        return False

    try:
        import matplotlib
        print(f"✓ Matplotlib {matplotlib.__version__} 安装成功")
    except ImportError:
        print("❌ Matplotlib 未安装，请运行: pip install matplotlib")
        return False

    return True

def test_blackbox_parser():
    """测试Blackbox解析器基本功能"""
    try:
        from Flight_Data_Analysis_Tools import BlackboxAnalyzer
        print("✓ Blackbox分析器导入成功")
        return True
    except ImportError as e:
        print(f"❌ Blackbox分析器导入失败: {e}")
        return False

if __name__ == "__main__":
    print("🔍 正在验证安装...")
    if test_dependencies() and test_blackbox_parser():
        print("\n🎉 所有测试通过！可以开始分析了。")
        print("💡 提示: 运行 'python Flight_Data_Analysis_Tools.py' 开始分析")
    else:
        print("\n❌ 安装验证失败，请检查错误信息并重新安装。")
```

### 运行验证
```bash
python test_installation.py
```

## 🐛 常见问题解决

### ❌ pip安装失败
**问题**: pip无法安装某些库
**解决方案**:
```bash
# 升级pip
python -m pip install --upgrade pip

# 使用国内镜像源（中国用户）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy pandas matplotlib

# 或者使用清华镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ numpy pandas matplotlib
```

### ❌ 权限问题
**问题**: 需要管理员权限才能安装
**解决方案**:
```bash
# Windows: 以管理员身份运行命令提示符
# macOS/Linux: 使用sudo
sudo pip install numpy pandas matplotlib
```

### ❌ 版本冲突
**问题**: 不同库之间版本不兼容
**解决方案**:
```bash
# 创建虚拟环境（推荐）
python -m venv fpv_env
source fpv_env/bin/activate  # macOS/Linux
# 或
fpv_env\Scripts\activate     # Windows

# 在虚拟环境中安装
pip install numpy pandas matplotlib
```

### ❌ 缺少编译器
**问题**: 某些库需要C编译器来构建
**解决方案**:
```bash
# Windows: 安装Microsoft C++ Build Tools
# 下载链接: https://visualstudio.microsoft.com/visual-cpp-build-tools/

# macOS: 确保Xcode命令行工具已安装
xcode-select --install

# Linux: 安装build-essential
sudo apt-get install build-essential  # Ubuntu/Debian
sudo yum groupinstall "Development Tools"  # CentOS/RHEL
```

## 🌐 网络优化

### 使用镜像源
```bash
# 设置默认镜像源（永久生效）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 临时使用镜像源
pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ numpy
```

### 代理设置
```bash
# 如果使用代理
pip install --proxy http://user:password@proxyserver:port numpy pandas matplotlib
```

## 📱 移动设备安装

### Android (Termux)
```bash
# 在Termux中安装
pkg install python
pip install numpy pandas matplotlib

# 注意：性能可能受限，建议在大文件上谨慎使用
```

### iOS (Pythonista等应用)
- 目前不支持完整的NumPy/Pandas
- 建议使用网页版在线分析工具
- https://blackbox-parser.com/

## 🔄 更新和维护

### 定期更新
```bash
# 更新所有库到最新版本
pip install --upgrade numpy pandas matplotlib

# 或者只更新特定库
pip install --upgrade numpy
```

### 清理缓存
```bash
# 清理pip缓存
pip cache purge

# 卸载并重新安装
pip uninstall numpy pandas matplotlib
pip install numpy pandas matplotlib
```

## 📞 技术支持

### 获取帮助
```bash
# 查看库的版本信息
python -c "import numpy; print(numpy.__version__)"

# 查看库的路径
python -c "import numpy; print(numpy.__file__)"
```

### 错误报告
如果遇到安装问题，请提供以下信息：
- 操作系统类型和版本
- Python版本 (`python --version`)
- 完整的错误信息
- 尝试过的解决方法

---

**安装日期**: 2026年3月13日
**最后更新**: 2026年3月13日
**适用版本**: Python 3.7+
**支持平台**: Windows/Mac/Linux/Android(iOS有限支持)

*本指南为您提供完整的环境搭建指导，如有问题请及时反馈。*

## 🔗 相关链接

- [Python官方网站](https://www.python.org/)
- [NumPy文档](https://numpy.org/doc/)
- [Pandas文档](https://pandas.pydata.org/docs/)
- [Matplotlib文档](https://matplotlib.org/stable/contents.html)
- [Blackbox Parser在线工具](https://blackbox-parser.com/)
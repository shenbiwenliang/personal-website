# 贡献指南

## 🎯 欢迎加入FPV数据分析社区！

感谢您有兴趣为FPV飞行数据分析项目做出贡献。本指南将帮助您了解如何参与项目开发、报告问题或提出改进建议。

---

## 📋 项目概述

### 关于本项目
FPV飞行数据分析系统是一个专门为Blackbox v2格式飞行数据提供分析和调校指导的开放源代码项目。我们致力于为FPV飞手提供最专业、最易用的数据分析工具。

### 核心价值
- **专业性**: 基于Blackbox标准的精确分析
- **实用性**: 从专业分析到通俗易懂的用户体验
- **创新性**: 创新的PID性能评估算法
- **可扩展性**: 模块化设计便于功能扩展

---

## 🚀 如何贡献

### 🐛 报告Bug
发现bug时请按照以下步骤操作：

#### 1. 搜索现有问题
```bash
# 在GitHub Issues中搜索相关问题
gh issue list --search "bug report"
```

#### 2. 创建新Issue
**模板**:
```markdown
### Bug描述
[清晰描述遇到的问题]

### 重现步骤
1. [第一步]
2. [第二步]
3. [第三步]

### 期望行为
[描述预期的正确行为]

### 实际行为
[描述实际发生的错误行为]

### 环境信息
- **操作系统**: [如 Windows 10, macOS 12.0]
- **Python版本**: [如 Python 3.9.7]
- **库版本**:
  - NumPy: [版本号]
  - Pandas: [版本号]
  - Matplotlib: [版本号]
- **错误日志**: [完整错误信息]

### 附件
[如果有的话，上传相关截图或日志文件]
```

#### 3. 提交Issue
```bash
gh issue create --title "Bug描述" --body "完整的问题报告"
```

### 💡 提出新功能建议

#### 1. 讨论需求
在Issue中描述新功能的想法和具体用例。

#### 2. 设计文档
提供详细的设计方案，包括：
- **功能说明**: 详细的功能描述
- **技术方案**: 实现思路和算法设计
- **用户场景**: 目标用户和使用方式
- **API设计**: 如果需要的话

#### 3. 获得批准
等待核心开发团队的review和批准。

### 🔧 提交代码贡献

#### 1. Fork项目
```bash
git clone https://github.com/yourusername/fpv-analysis.git
cd fpv-analysis
git remote add upstream https://github.com/fpv-team/blackbox-analysis.git
```

#### 2. 创建分支
```bash
# 从main分支创建新特性分支
git checkout -b feature/new-analysis-feature

# 或者修复bug的分支
git checkout -b bugfix/memory-leak-issue
```

#### 3. 开发代码
遵循以下规范：
- **代码风格**: 遵循PEP 8规范
- **命名规范**: 使用有意义的变量和函数名
- **注释要求**: 关键算法需要详细注释
- **测试覆盖**: 为新功能添加单元测试

#### 4. 编写测试
```python
def test_new_feature():
    """测试新功能的正确性"""
    # 编写具体的测试用例
    pass
```

#### 5. 提交更改
```bash
# 添加修改的文件
git add .

# 提交更改（使用清晰的提交信息）
git commit -m "feat: 添加新的PID分析模块

- 实现P/I/D/F参数的智能分析
- 增加振荡检测算法
- 优化内存使用效率"

# 推送到你的fork
git push origin feature/new-analysis-feature
```

#### 6. 创建Pull Request
```bash
gh pr create \
  --title "新功能: PID智能分析模块" \
  --body "详细的PR说明和功能描述" \
  --base main \
  --head yourusername:feature/new-analysis-feature
```

---

## 📝 开发规范

### 代码风格
- **Python版本**: 3.7+
- **编码格式**: UTF-8
- **缩进**: 4个空格（不要使用tab）
- **最大行宽**: 88字符
- **导入顺序**: 标准库 -> 第三方库 -> 本地模块

### 示例代码风格
```python
import numpy as np
import pandas as pd

def analyze_pid_performance(data):
    """
    分析PID控制性能

    Args:
        data (list): Blackbox飞行数据列表

    Returns:
        dict: 包含各项性能指标的结果
    """
    if not data:
        raise ValueError("数据不能为空")

    try:
        df = pd.DataFrame(data)
        # 性能分析逻辑
        performance = calculate_stability_index(df)
        return performance
    except Exception as e:
        logger.error(f"PID分析失败: {e}")
        raise
```

### 提交消息规范
使用[Conventional Commits](https://www.conventionalcommits.org/)格式：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### 常用类型
- **feat**: 新功能
- **fix**: Bug修复
- **docs**: 文档更新
- **style**: 代码风格调整
- **refactor**: 代码重构
- **test**: 测试相关
- **chore**: 构建过程或辅助工具的变动

#### 示例
```
feat: 添加陀螺仪数据可视化功能

- 实现gyroADC数据的实时图表显示
- 支持多轴数据对比分析
- 优化图表渲染性能

Closes #123
```

---

## 🧪 测试规范

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
```

### 性能测试
- **小文件测试**: <1MB数据处理时间
- **中文件测试**: 16MB数据处理时间
- **大文件测试**: >100MB数据处理时间
- **内存使用**: 峰值内存不超过500MB

### 兼容性测试
- **操作系统**: Windows 10/11, macOS 10.15+, Ubuntu 20.04+
- **Python版本**: 3.7, 3.8, 3.9, 3.10
- **依赖版本**: 主要库的兼容版本

---

## 📚 文档规范

### 代码文档
- **函数文档**: 使用Google风格的docstring
- **类文档**: 详细说明类的用途和方法
- **模块文档**: 每个.py文件开头必须有模块说明
- **示例代码**: 提供使用示例

### README更新
- **功能变更**: 更新README中的功能描述
- **安装指南**: 确保安装步骤准确无误
- **示例代码**: 提供最新的使用示例

### API文档
- **接口说明**: 详细描述每个函数的参数和返回值
- **使用示例**: 提供典型使用场景的代码示例
- **错误处理**: 说明可能的异常和错误情况

---

## 🌐 社区准则

### 行为准则
我们致力于创建一个友好、尊重和包容的社区：

1. **保持尊重**: 对所有成员保持礼貌和专业
2. **建设性反馈**: 提供有帮助的批评和建议
3. **知识分享**: 乐于分享经验和解决方案
4. **耐心指导**: 帮助新手学习和成长

### 讨论规范
- **问题描述**: 提供清晰的问题描述和复现步骤
- **技术支持**: 基于事实和技术进行讨论
- **避免争论**: 专注于解决问题而非争论对错
- **引用来源**: 提供可靠的参考资料

---

## 🔒 安全政策

### 漏洞报告
发现安全问题请立即通过以下方式报告：
- **邮件**: security@fpv-analysis.com
- **加密**: 使用PGP密钥加密敏感信息
- **响应时间**: 24小时内确认收到

### 安全规范
- **代码审查**: 所有代码必须经过安全审查
- **依赖管理**: 定期更新依赖库，修复已知漏洞
- **权限控制**: 限制敏感操作的访问权限
- **数据保护**: 用户数据隐私保护措施

---

## 📞 联系方式

### 主要联系渠道
- **GitHub Issues**: 技术问题和功能建议
- **Email**: tech@fpv-analysis.com
- **Discord**: FPV Analysis Community
- **论坛**: RCGroups专题讨论区

### 响应时间
- **紧急Bug**: 24小时内响应
- **一般问题**: 3个工作日内回复
- **功能讨论**: 一周内回复
- **代码Review**: 根据优先级安排

---

## 🙏 感谢贡献者

### 核心团队成员
- **项目发起人**: FPV数据分析团队
- **技术架构师**: 算法设计和系统架构
- **UI/UX设计师**: 用户体验和界面设计
- **测试工程师**: 质量保证和测试覆盖

### 社区贡献者
我们感谢每一位社区成员的贡献，包括但不限于：
- Bug报告和问题反馈
- 功能建议和创意分享
- 文档翻译和改进
- 测试用例和验证
- 用户支持和指导

---

**最后更新时间**: 2026年3月13日
**版本**: v1.0
**维护团队**: FPV数据分析核心团队

*感谢您的贡献！让我们一起为FPV飞手创造更好的数据分析工具。*

## 🔗 相关链接

- [项目主页](https://github.com/fpv-team/blackbox-analysis)
- [MIT许可证](LICENSE)
- [行为准则](CODE_OF_CONDUCT.md)
- [安全政策](SECURITY.md)
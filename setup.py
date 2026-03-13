#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FPV飞行数据分析工具 - Python包配置

作者: FPV数据分析团队
版本: 1.0.0
许可证: MIT
"""

from setuptools import setup, find_packages
import os
import sys

# 读取README文件
def read_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

# 读取LICENSE文件
def read_license():
    with open('LICENCE.md', 'r', encoding='utf-8') as f:
        return f.read()

# 获取版本信息
def get_version():
    """从__version__文件中获取版本号"""
    version_file = 'Flight_Data_Analysis_Tools.py'
    if os.path.exists(version_file):
        with open(version_file, 'r', encoding='utf-8') as f:
            for line in f:
                if '__version__' in line:
                    return line.split('=')[1].strip().strip('"\'')
    return '1.0.0'

# 获取依赖项
def get_requirements():
    """读取requirements.txt文件"""
    requirements = []
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('dev-requirements'):
                    requirements.append(line)
    return requirements

# 获取开发依赖项
def get_dev_requirements():
    """获取开发环境依赖项"""
    dev_requirements = [
        'pytest>=6.0.0',
        'black>=21.0.0',
        'flake8>=3.9.0',
        'mypy>=0.910',
        'sphinx>=4.0.0',
        'mkdocs>=1.2.0',
        'bandit>=1.7.0',
        'safety>=2.3.0',
        'detect-secrets>=1.4.0',
    ]
    return dev_requirements

# 获取分类器
def get_classifiers():
    """获取PyPI分类器"""
    classifiers = [
        # 开发状态
        'Development Status :: 5 - Production/Stable',

        # 目标受众
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',

        # 主题
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # 许可证
        'License :: OSI Approved :: MIT License',

        # 支持的Python版本
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

        # 操作系统
        'Operating System :: OS Independent',

        # 语言
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
    ]

    # 特定领域分类器
    domain_classifiers = [
        'Framework :: Blackbox',
        'Framework :: Betaflight',
        'Framework :: FPV',
        'Framework :: Flight Control',
        'Framework :: PID Control',
    ]

    return classifiers + domain_classifiers

# 获取关键词
def get_keywords():
    """获取项目关键词"""
    keywords = [
        'fpv', 'flight data', 'blackbox', 'pid tuning', 'drone analysis',
        'flight control', 'data visualization', 'performance analysis',
        'nicholas sherlock', 'betaflight', 'quadcopter', 'multirotor',
        'flight recorder', 'data parser', 'oscillation detection',
        'stability index', 'response analysis', 'motor output',
        'gyroscope data', 'flight performance', 'tuning guide'
    ]

    chinese_keywords = [
        'FPV', '飞行数据', '黑匣子', 'PID调校', '无人机分析',
        '飞行控制', '数据可视化', '性能分析', '尼古拉斯·舍洛克',
        'Betaflight', '四旋翼', '多旋翼', '飞行记录器', '数据解析',
        '振荡检测', '稳定性指数', '响应分析', '电机输出', '陀螺仪数据'
    ]

    return keywords + chinese_keywords

# 获取作者信息
def get_author_info():
    """获取作者和联系信息"""
    return {
        'name': 'FPV数据分析团队',
        'email': 'team@fpv-analysis.com',
        'url': 'https://github.com/fpv-team/blackbox-analysis',
        'maintainer': 'FPV数据分析核心团队',
        'organization': 'FPV数据分析开源社区',
    }

def main():
    """主函数"""
    # 基本信息
    version = get_version()
    author_info = get_author_info()

    # 配置参数
    setup(
        # 基本信息
        name='fpv-flight-data-analyzer',
        version=version,
        description='专业的Blackbox飞行数据分析工具，为FPV飞手提供精准的PID调校指导',
        long_description=read_readme(),
        long_description_content_type='text/markdown',

        # 作者信息
        author=author_info['name'],
        author_email=author_info['email'],
        maintainer=author_info['maintainer'],

        # 项目链接
        url=author_info['url'],
        project_urls={
            'Bug Reports': 'https://github.com/fpv-team/blackbox-analysis/issues',
            'Source Code': 'https://github.com/fpv-team/blackbox-analysis',
            'Documentation': 'https://fpv-analysis.demo.com',
            'Community Forum': 'https://rcgroups.com/',
            'Security Policy': 'https://github.com/fpv-team/blackbox-analysis/blob/main/.github/SECURITY.md',
        },

        # 包信息
        packages=find_packages(include=['*']),
        include_package_data=True,
        package_data={
            '': ['*.md', '*.txt', '*.yml', '*.yaml'],
            'fpv_analysis': ['data/*.bbl', 'examples/*.py'],
        },

        # 脚本和命令
        entry_points={
            'console_scripts': [
                'fpv-analyze=Flight_Data_Analysis_Tools:main',
                'fpv-flight-analysis=Flight_Data_Analysis_Tools:main',
            ],
        },

        # 依赖项
        install_requires=get_requirements(),
        extras_require={
            'dev': get_dev_requirements(),
            'test': get_dev_requirements() + ['pytest-cov', 'coverage'],
            'docs': ['sphinx', 'sphinx-rtd-theme', 'mkdocs', 'mkdocs-material'],
            'security': ['bandit', 'safety', 'detect-secrets'],
            'all': get_requirements() + get_dev_requirements(),
        },

        # 测试配置
        test_suite='tests',
        tests_require=['pytest'],

        # 构建配置
        python_requires='>=3.7',
        zip_safe=False,

        # PyPI元数据
        license='MIT',
        classifiers=get_classifiers(),
        keywords=get_keywords(),

        # 商业友好性
        platforms=['any'],
        options={
            'bdist_wheel': {
                'universal': False,
            },
        },

        # 额外文件
        data_files=[
            ('', ['README.md', 'LICENCE.md', 'CHANGELOG.md', 'CONTRIBUTING.md']),
            ('docs/', ['README_Analysis_Tools.md', 'Quick_Start_Guide.md', 'Installation_Guide.md']),
            ('templates/', ['Master_Index.md', 'Tech_Specifications.md']),
        ],

        # 商业信息
        commercial_use=True,
        research_use=True,
        educational_use=True,
        non_commercial_use=True,

        # 技术支持
        support_email='support@fpv-analysis.com',
        support_url='https://github.com/fpv-team/blackbox-analysis/discussions',
    )

if __name__ == '__main__':
    main()
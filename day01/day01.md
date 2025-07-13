1. 创建虚拟环境
    `python -m venv .venv` 创建虚拟环境 
    `source ./.venv/activate.fish` 在fish下激活虚拟环境
    - 安装black 代码格式化工具
    - 安装isort 导入排序工具
    - 安装pylint 静态代码检测工具
    graph LR
    A[代码开发] --> B[isort 整理导入]
    B --> C[black 格式化代码]
    C --> D[pylint 质量检查]
    D --> E[修复问题]
    E --> A
2. 熟悉vsCode的python插件调试方式
3. 练习基础语法

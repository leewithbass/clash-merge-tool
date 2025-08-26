# 贡献指南

感谢您考虑为 Clash 订阅合并工具做出贡献！我们欢迎任何形式的贡献，包括但不限于代码提交、问题报告、功能建议等。

## 如何贡献

### 报告 Bug

在提交 Bug 报告前，请先确认以下几点：
1. 检查是否已有相关的 Issue
2. 尽可能提供详细的复现步骤
3. 提供运行环境信息（操作系统、Python 版本等）

### 提交功能建议

我们欢迎新功能建议！请：
1. 检查是否已有相关的 Issue
2. 清晰描述功能需求和使用场景
3. 如果可能，提供实现思路

### 代码贡献

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码风格

请遵循 PEP 8 代码规范，确保代码可读性和一致性。

## 开发环境设置

1. Fork 并克隆项目
2. 创建虚拟环境
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # 或
   venv\Scripts\activate  # Windows
   ```
3. 安装开发依赖
   ```bash
   pip install -r requirements.txt
   ```

## 测试

在提交 Pull Request 前，请确保：
1. 代码能正常运行
2. 没有引入新的错误
3. 保持代码风格一致

## 问题和讨论

如有任何问题或建议，欢迎在 Issues 中提出讨论。

再次感谢您的贡献！
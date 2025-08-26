# 🚀 Clash 订阅合并工具 | Shadowsocks 节点智能整合专家

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/platform-cross--platform-lightgrey" alt="Platform">
</p>

## 🌟 项目简介

**Clash 订阅合并工具**是一款专为 Shadowsocks 用户设计的智能配置文件生成器。它能够将多个订阅链接中的节点智能整合，自动生成优化的 Clash 配置文件，让您的网络体验更加流畅和便捷。

无论是个人用户管理多个订阅源，还是团队协作需要统一配置，这款工具都能为您提供完美的解决方案。

## ✨ 核心特性

### 🔗 多源订阅整合
- 支持同时处理多个 Shadowsocks 订阅链接
- 自动解码 Base64 编码的订阅内容
- 智能识别并解析多种格式的 Shadowsocks 节点

### 🧠 智能节点处理
- **智能过滤**：自动识别并过滤信息性节点（如流量统计、到期提醒等）
- **精准解析**：支持标准和非标准格式的 Shadowsocks 链接
- **去重优化**：确保生成的配置文件简洁高效

### 🌍 地区智能分组
- **自动识别**：智能识别节点名称中的地区信息（支持中文、英文、Emoji 等多种格式）
- **精细化分组**：按地区自动创建 `url-test` 代理组，实现延迟最优选择
- **灵活配置**：支持亚洲、欧洲、北美、大洋洲等主要地区

### 🎨 优雅的用户体验
- **交互式界面**：使用 [Rich](https://github.com/Textualize/rich) 库打造精美的命令行界面
- **实时进度**：直观的进度显示和处理状态反馈
- **统计报表**：生成详细的节点统计表格，一目了然

### 🛠️ 标准化输出
- 生成完全兼容 Clash 的 YAML 配置文件
- 预设优化的代理组结构（PROXY 主组、地区分组、手动选择组）
- 遵循最佳实践的默认配置参数

## 🚀 快速开始

### 📋 环境要求
- Python 3.7 或更高版本
- 支持 Windows、macOS、Linux 等主流操作系统

### 📦 安装依赖
```bash
pip install requests pyyaml rich
```

### 🏃‍♂️ 运行工具
```bash
python merge_clash.py
```

### 🎯 使用流程
1. **输入订阅链接**：按提示逐行输入您的 Shadowsocks 订阅链接（每行一个）
2. **指定输出文件**：输入生成的配置文件名（默认为 `config.yaml`）
3. **等待处理完成**：工具会自动获取、解析并生成配置文件
4. **享受优化配置**：在脚本同目录下获取您的专属 Clash 配置文件

## 📁 项目结构

```
clash_merge/
├── merge_clash.py     # 主程序文件
├── config.yaml       # 生成的配置文件示例
├── README.md         # 项目说明文档
├── requirements.txt  # 依赖包列表
└── LICENSE           # 开源许可证
```

## 🎯 配置文件详解

生成的配置文件包含以下智能结构：

### 🔌 Proxies（代理节点）
所有解析出的有效 Shadowsocks 节点，经过智能过滤和命名优化。

### 📦 Proxy Groups（代理组）
```yaml
# 主选择组 - 汇聚所有地区分组
- name: "PROXY"
  type: select
  proxies:
    - " 🇭🇰 香港"
    - " 🇸🇬 新加坡"
    - " 🇯🇵 日本"
    - " 🇺🇸 美国"
    - "MANUAL-SELECT"

# 地区分组 - 自动测速选择最优节点
- name: " 🇭🇰 香港"
  type: url-test
  url: "http://www.gstatic.com/generate_204"
  interval: 300
  proxies:
    - "HK Node 1"
    - "HK Node 2"

# 手动选择组 - 包含所有节点供手动切换
- name: "MANUAL-SELECT"
  type: select
  proxies:
    - "所有节点列表..."
```

### 📜 Rules（规则）
默认规则集，所有流量通过 PROXY 组处理。

> **注意**：为了方便每个人的使用，此脚本在合并时并没有添加分流规则。个人习惯是在全局扩展脚本中添加相关分流规则。

## 🔧 技术架构

### 核心依赖库
- **[requests](https://docs.python-requests.org/)**: 简洁优雅的 HTTP 库
- **[PyYAML](https://pyyaml.org/)**: 强大的 YAML 解析和生成库
- **[Rich](https://github.com/Textualize/rich)**: 美观的终端界面库

### 设计理念
1. **模块化设计**：功能分离，易于维护和扩展
2. **错误处理**：完善的异常处理机制
3. **用户体验**：注重交互体验和视觉效果
4. **兼容性**：支持多种格式和平台

## 🤝 贡献指南

我们欢迎任何形式的贡献！

### 提交 Issue
- 发现 Bug 或有功能建议？请提交 [Issue](https://github.com/yourusername/clash_merge/issues)
- 请使用清晰的标题和详细的描述

### Pull Request
1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 开源许可证

本项目采用 MIT 许可证，详情请参见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 感谢 [Clash](https://github.com/Dreamacro/clash) 项目提供的优秀代理工具
- 感谢 [Rich](https://github.com/Textualize/rich) 团队提供的精美终端界面库
- 感谢所有为开源社区做出贡献的开发者们

## 📞 联系方式

如有任何问题或建议，欢迎通过以下方式联系：
- 提交 GitHub Issue
- 发送邮件至：[your-email@example.com](mailto:your-email@example.com)

---

<p align="center">
  <strong>⭐ 如果您觉得这个项目有用，请给它一个 Star！⭐</strong>
</p>
# Clash 订阅合并工具

<!-- PROJECT SHIELDS -->
<p align="center">
  <a href="https://github.com/yourusername/clash_merge/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/yourusername/clash_merge.svg?style=for-the-badge" alt="Contributors">
  </a>
  <a href="https://github.com/yourusername/clash_merge/network/members">
    <img src="https://img.shields.io/github/forks/yourusername/clash_merge.svg?style=for-the-badge" alt="Forks">
  </a>
  <a href="https://github.com/yourusername/clash_merge/stargazers">
    <img src="https://img.shields.io/github/stars/yourusername/clash_merge.svg?style=for-the-badge" alt="Stargazers">
  </a>
  <a href="https://github.com/yourusername/clash_merge/issues">
    <img src="https://img.shields.io/github/issues/yourusername/clash_merge.svg?style=for-the-badge" alt="Issues">
  </a>
  <a href="https://github.com/yourusername/clash_merge/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/yourusername/clash_merge.svg?style=for-the-badge" alt="MIT License">
  </a>
</p>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/yourusername/clash_merge">
    <img src="https://raw.githubusercontent.com/Dreamacro/clash/master/docs/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Clash 订阅合并工具</h3>

  <p align="center">
    一款智能整合 Shadowsocks 订阅的 Clash 配置文件生成器
    <br />
    <a href="https://github.com/yourusername/clash_merge"><strong>探索文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/yourusername/clash_merge">查看Demo</a>
    ·
    <a href="https://github.com/yourusername/clash_merge/issues">报告Bug</a>
    ·
    <a href="https://github.com/yourusername/clash_merge/issues">请求功能</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## 关于项目

Clash 订阅合并工具是一款专为 Shadowsocks 用户设计的智能配置文件生成器。它能够将多个订阅链接中的节点智能整合，自动生成优化的 Clash 配置文件，让您的网络体验更加流畅和便捷。

### 特色功能

* **多源订阅整合** - 支持同时处理多个 Shadowsocks 订阅链接
* **智能节点处理** - 自动过滤无效节点，保留有效代理
* **地区智能分组** - 按地区自动创建代理组，实现最优选择
* **优雅用户体验** - 使用 Rich 库打造精美终端界面
* **标准化输出** - 生成完全兼容 Clash 的 YAML 配置文件

<!-- GETTING STARTED -->
## 快速开始

### 环境要求

* Python 3.7 或更高版本
* pip 包管理器

### 安装步骤

1. 克隆项目
   ```sh
   git clone https://github.com/leewithbass/clash_merge.git
   ```
2. 安装依赖
   ```sh
   pip install -r requirements.txt
   ```
3. 运行工具
   ```sh
   python merge_clash.py
   ```

<!-- USAGE EXAMPLES -->
## 使用说明

1. 运行脚本后，按提示输入您的 Shadowsocks 订阅链接
2. 指定输出配置文件名
3. 工具将自动处理并生成优化的 Clash 配置文件

> **注意**：为了方便每个人的使用，此脚本在合并时并没有添加分流规则。个人习惯是在全局扩展脚本中添加相关分流规则。

<!-- ROADMAP -->
## 路线图

- [x] 基础订阅合并功能
- [x] 多格式 Shadowsocks 链接支持
- [x] 智能地区分组
- [ ] 支持更多代理协议（V2Ray、Trojan等）
- [ ] Web 界面版本
- [ ] 配置文件模板自定义

<!-- CONTRIBUTING -->
## 贡献指南

欢迎任何形式的贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解更多详情。

<!-- LICENSE -->
## 开源许可证

本项目采用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件。

<!-- CONTACT -->
## 联系方式

项目链接: [https://github.com/yourusername/clash_merge](https://github.com/yourusername/clash_merge)

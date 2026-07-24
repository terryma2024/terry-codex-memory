# Terry Codex Profile

这是一个可迁移、可审阅的 Codex 配置仓库。它用于在干净环境中重建工作方法、能力清单和安全边界；它**不是**当前机器的完整镜像。

## 快速开始

1. 克隆本仓库，不要覆盖现有 `~/.codex`。
2. 阅读 [初始化指南](docs/initialization.md) 与 [工作原则](profile/working-principles.md)。
3. 先运行 `scripts/audit.sh`，确认新环境中可用的命令和缺失项。
4. 仅按需安装 [技能清单](manifests/skills.md) 中的 Skills。
5. 复制 `config/codex-config.template.toml` 的非敏感项到新环境配置；凭据仅通过本机安全存储或环境变量提供。
6. 若新环境具备对应的 Xray 维护命令，再按 [xray-route 说明](skills/xray-route/README.md) 安装或引用该 Skill。

## 内容与边界

- 保留：工作习惯、可验证工作流、能力清单、配置结构、脱敏自建 Skill。
- 不保留：API Key、令牌、Cookie、私有端点、SSH 私钥、会话记录、缓存、日志、设备路径、实时网络规则。
- 所有包含 `YOUR_` 或 `<...>` 的值都必须在新机器本地填写，禁止提交回本仓库。

## 验收标准

初始化完成后，新 Codex 应能读懂本仓库的工作原则，按项目选择合适的 Skill，执行前先验证真实状态，并遵守安全与回滚边界。它不应被假定拥有本机账号、网络、硬件或历史会话。


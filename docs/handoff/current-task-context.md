# Codex Memory 迁移包：当前任务 Context

## 目标

维护 `terry-codex-memory`：一个可迁移的 Codex 配置仓库。它应让干净环境中的 Codex 学习 Terry 的工作习惯、经过验证的工作流、已使用/自建 Skill 和非敏感配置结构。

## 仓库状态

- 本地仓库：`/Users/matianyi/Projects/terry-codex-memory`
- 远端：GitHub 上同名仓库，`main` 已推送。
- 核心入口：`README.md`、`docs/initialization.md`、`profile/`、`manifests/`、`skills/`。
- 已纳入的自建 Skills：`thinking-partner`、`vocab-print-cards`、`xray-route`。
- 已有 SOP：`docs/sop/codex-memory-curation.md`。

## 安全边界（不可突破）

- 绝不提交 API Key、令牌、Cookie、密码、私钥、私人地址、真实网络规则、生产数据、历史会话原文、缓存或日志。
- 只沉淀脱敏后的概括性规则、可验证工作流、非敏感模板和可审阅 Skill 源码。
- 新 Skill 必须有真实任务验证、清楚的输入输出/依赖/失败边界，并通过相应检查。
- 每次提交前运行 `scripts/audit.sh` 和 `git diff --check`；脚本更新还要做语法或基础运行检查。

## 当前自动化

已创建名为“每周 Codex Memory 整理”的本机 Codex 自动任务：每周执行一次，按 SOP 提炼最近七天的可迁移增量，只有实质更新才提交并推送，失败时通知。

### 新项目建立后必须做的第一件事

将该自动任务重新绑定到新创建的 Codex 项目。当前自动任务因新仓库尚未出现在 Codex 项目列表中，使用的是临时本地执行环境；不要长期保留这一绑定。

## 新任务应执行的顺序

1. 阅读本文件、README、初始化指南和 SOP。
2. 确认新 Codex 项目已指向本仓库。
3. 将每周自动任务绑定到该项目，并检查其提示词仍引用本 SOP。
4. 只读审阅现有仓库和自动化状态；不要修改凭据、会话或系统目录。
5. 按 SOP 做一次演练：无敏感数据时才能写入、审计、提交和推送。
6. 后续每周只纳入经过验证的新经验；没有实质增量时不创建空提交。

## 建议的新任务提示词

“阅读 `docs/handoff/current-task-context.md`，继续维护本仓库的 Codex Memory 迁移包。先确认每周自动任务已绑定到当前项目，再按 `docs/sop/codex-memory-curation.md` 执行只读检查。严格遵守脱敏边界；不要复制原始会话或任何凭据。”


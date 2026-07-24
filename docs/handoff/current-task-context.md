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

已创建名为“每周 Codex Memory 整理”的本机 Codex 自动任务：每周一 09:00 执行，按 SOP 提炼最近七天的可迁移增量，只有实质更新才提交并推送，仅在失败时通知。

### 当前绑定状态

2026-07-24 已确认：Codex 项目 `codex-memory` 指向本仓库，自动任务也已绑定到该项目及本仓库目录。后续只需在项目路径、自动任务或执行环境发生变化时重新核对绑定，不要无故重建重复任务。

## 新任务应执行的顺序

1. 阅读本文件、README、初始化指南和 SOP。
2. 确认 Codex 项目仍指向本仓库。
3. 检查每周自动任务仍绑定到该项目，且提示词仍引用本 SOP；发现漂移时才更新。
4. 只读审阅现有仓库和自动化状态；不要修改凭据、会话或系统目录。
5. 按 SOP 做一次演练：无敏感数据时才能写入、审计、提交和推送。
6. 后续每周只纳入经过验证的新经验；没有实质增量时不创建空提交。

## 建议的新任务提示词

“阅读 `docs/handoff/current-task-context.md`，继续维护本仓库的 Codex Memory 迁移包。先确认每周自动任务已绑定到当前项目，再按 `docs/sop/codex-memory-curation.md` 执行只读检查。严格遵守脱敏边界；不要复制原始会话或任何凭据。”

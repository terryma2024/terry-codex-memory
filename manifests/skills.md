# Skills 清单

以下是有历史任务证据、值得在新环境按需准备的能力。它们不都是项目运行时依赖；安装前须确认来源、版本和新环境兼容性。

| 类别 | Skills | 用途 |
|---|---|---|
| 研究与知识库 | `obsidian-markdown`、`obsidian-cli`、`obsidian-bases`、`excalidraw-diagram`、`defuddle`、`scholar-skill` | 来源可追溯研究与知识沉淀 |
| 自建决策辅助 | `thinking-partner` | 一问一答地澄清目标、约束、成功标准与下一步 |
| 自建学习输出 | `vocab-print-cards` | 生成可打印的中译英默写卡与答案 PDF |
| 学习 | `tutor`、`tutor-setup` | 交互式学习与材料组织 |
| 飞书协作 | `lark-doc`、`lark-drive`、`lark-base`、`lark-markdown`、`lark-slides`、`lark-sheets` | 在线文档、云盘、表格与演示材料 |
| 工程与界面 | `superpowers`、`shadcn`、`opencli-usage`、`opencli-browser` | 需求变更、调试、界面与浏览器工作 |
| 网络维护 | `xray-route` | 本机 Xray 路由维护；仅在配套命令已安装时使用 |

## 安装原则

- 不批量安装“所有可用 Skills”。
- 先在目标项目中确认用途、依赖、权限和测试方式。
- 对开发类需求，默认采用 Superpowers 的计划、测试和验证流程。
- 全局安装仅用于跨项目稳定基础能力；项目专有能力优先随项目管理。
- 本仓库内的 `thinking-partner`、`vocab-print-cards` 与 `xray-route` 是可审阅的自建 Skill 源码；其中后两者分别需要目标机器具备 Python/PDF 运行环境与本机 Xray 命令。

## 项目内 Skill 的边界

- 先读取项目的 `AGENTS.md` 和项目内 Skill，再开始开发、调试、测试或视觉验收；项目规则优先于本清单的通用建议。
- 已在单一项目验证的专用 Skill 继续随该项目版本化，不复制到本仓库或全局安装目录。
- 周度整理只提炼跨项目成立的工作原则和证据门；只有触发场景、输入、输出、依赖与失败边界都稳定时，才考虑迁入通用自建 Skill。
- 发布项目内 Skill 时只提交该 Skill 和明确要求的规则文件；子模块指针、其他工作树改动和运行证据不自动进入同一提交。

# Verbatim Harbor v0.1：参评材料索引

文档补充日期：2026-11-04。

| 材料 | 内容 / 入口 |
| --- | --- |
| 参赛者 / 单位 | 高天翊 / 北京理工大学 |
| 系统 / 展示版本 | Verbatim Harbor / v0.1 |
| 赛道 | Textual；组别以已审核绑定信息为准 |
| 公开仓库 | <https://github.com/GTYanita/verbatim-harbor> |
| 固定生产源码 Commit | `a007726a4ee8e75bf0c4ff711992c91d9a4893e4` |
| 源码与归档身份 | [RELEASE_IDENTITY.json](../RELEASE_IDENTITY.json) |
| 部署、依赖和运行说明 | [README.md](../README.md)、[DEPLOYMENT.md](DEPLOYMENT.md)、[requirements.txt](../requirements.txt) |
| API 字段与同步契约 | [README.md](../README.md#api-契约与示例) |
| 模型、预算和参数 | [README.md](../README.md#模型与运行依赖) |
| 容量、超时与恢复 | [OPERATIONS.md](OPERATIONS.md) |
| 来源、技术差异与许可 | [PROVENANCE.md](../PROVENANCE.md)、[METHOD_CHANGES.md](METHOD_CHANGES.md)、[LICENSE](../LICENSE) |
| 文件核验 | [SHA256SUMS.json](../SHA256SUMS.json)，对应当前提交内 canonical Git blob 字节 |

Add/Search 使用已登记的私密 Token；Health 无需鉴权。示例只提供占位符，不公开 Eval Key、服务 Token 或百炼凭据。采用同步 Add，不申报异步 Add 状态接口。

许可与版权信息见根目录 LICENSE；运行文件身份及技术差异见 PROVENANCE.md。

Add/Search 不调用生成模型；实际 Embedding 为 `text-embedding-v4`、1024 维。平台控制 Answer/Judge；模型及组别资格以赛事审核为准，不把本文当作其他规则的豁免。

Full 已由参赛者提交，仓库保留最初受理任务 `teval_cc46e8ef0571706c` 作为版本关联。后续恢复、状态、成绩与有效提交认定以平台记录为准。固定源码及评测记录保持原身份。

# Verbatim Harbor（原文港）v0.1

开发证据流水线、运行回归检查及构建容器，见[开发指南](manual/CONTRIBUTING.md)。

面向 Agent Memory Challenge **Textual Track** 的记忆服务，提供同步 Add、原文证据 Search 和 Health。参赛者：**高天翊**；所属单位：**北京理工大学**；GitHub：**GTYanita**。

系统持久化原始对话和文档，通过向量与词法检索组织相关原文片段。Search 交付记忆证据；最终回答、代码任务执行和评分由赛事平台统一完成。本版本处理文本字符串，不声明支持多模态图片内容数组或 Coding Track。

## 版本与核验

| 项目 | 记录 |
| --- | --- |
| 展示名称 / 版本 | Verbatim Harbor / v0.1 |
| 冻结实现 | `selected-original-question-answer-pair-v9` |
| 对应生产源码的固定 Commit | [`a007726a4ee8e75bf0c4ff711992c91d9a4893e4`](https://github.com/GTYanita/verbatim-harbor/tree/a007726a4ee8e75bf0c4ff711992c91d9a4893e4) |
| 冻结部署归档 SHA256 | `7befac6e2c4b2dc0b7e31c7e78b8cb783bcf5ca7cd26397e53d88ef3078cf2e5` |
| 历史 Full 受理任务 | `teval_cc46e8ef0571706c` |

本次补充为文档更新，未改变参评生产 Python、依赖锁定、模型、算法或运行配置。`main` 的文档提交与上表参评源码提交分开记录；复核时请固定 Commit。归档哈希标识原部署包，不等同于任意 GitHub 自动下载 ZIP 的哈希。

版本字段见 [RELEASE_IDENTITY.json](RELEASE_IDENTITY.json)，当前提交文件摘要见 [SHA256SUMS.json](SHA256SUMS.json)。Health 中的软件版本字段与参赛展示版本分别记录，参赛展示版本以上表为准。Full 已提交；最新任务状态、成绩及有效提交认定以平台与主办方复核为准，本仓库不据此宣称 Full 已成功完成或取得特定成绩。

## 模型与运行依赖

| 组件 | 本版本实际使用 |
| --- | --- |
| Embedding | 百炼 `text-embedding-v4`，1024 维，单批最多 10 条 |
| Add / Search 生成模型 | 无；不调用聊天补全、摘要或答案生成模型 |
| 检索 | 原文分段、稠密与词法检索、确定性证据组织 |
| 检索模式 / 返回预算 | `query_document_evidence` / 24000 字符 |
| 存储 | SQLite，独立数据库与用户命名空间 |
| 运行时 | Python；下方复现采用 Python 3.12，依赖版本见 [requirements.txt](requirements.txt) |
| 本地 GPU / 模型权重 | 此生产配置不需要；Embedding 依赖外部百炼服务 |

正式请求 `top_k` 为 100，接口允许整数 1–100。24000 字符为服务侧证据预算，包含输出元数据开销的具体计算以源码为准，不等同于平台 Answer 的 token 预算。平台仍按其冻结规则构造实际回答输入，本服务不覆盖 Answer/Judge 模型、提示或评分。

输入和持久化使用 Unicode 文本，可接受中英文；不同语言的检索质量需各自评测。参赛组别及模型要求以已审核版本和现行规则为准，上表如实列出本服务使用的组件。

## 本地启动

在独立复现环境中使用新的测试数据库与自有密钥。

```powershell
git clone https://github.com/GTYanita/verbatim-harbor.git
cd verbatim-harbor
# 如需复核原参评代码，检出上方固定 Commit；本次补充说明保留在文档提交中。
git checkout a007726a4ee8e75bf0c4ff711992c91d9a4893e4
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item env.example .env
```

在本机私密 `.env` 中设置 `MEMORY_API_KEY`、`DASHSCOPE_API_KEY` 和有效的 `AE_EMBEDDING_URL`，将 `AE_DATABASE` 改为独立路径，例如 `data/verbatim-harbor-v01-review/memory.sqlite3`。保留上表模型、维度、模式和预算，替换模板中的 `{WorkspaceId}` 占位地址。不要将 `.env` 或真实密钥提交到 Git。

```powershell
.\.venv\Scripts\python.exe preflight.py --env-file .env
.\start_local.ps1 -Port 18401 -PythonPath .\.venv\Scripts\python.exe -EnvFile .env
```

服务监听 `http://127.0.0.1:18401`。预检默认不发出 Embedding 请求；`--live` 会在临时数据库中对合成数据调用真实 Embedding，有计费与配额消耗，不属于官方 Smoke。Linux、容器及公网部署见 [DEPLOYMENT.md](manual/DEPLOYMENT.md)。

## API 契约与示例

| 接口 | 方法 | 相对路径 | 鉴权 |
| --- | --- | --- | --- |
| Add | POST | `/add` | 已登记 Token |
| Search | POST | `/search` | 已登记 Token |
| Health | GET | `/health` | 无 |

Add/Search 接受 `Authorization: Bearer <MEMORY_API_KEY>`、`Authorization: Token <MEMORY_API_KEY>` 或 `X-Api-Key: <MEMORY_API_KEY>`。参赛系统 Token 与平台 Eval Key 是不同凭据，均不公开。下面是本地合成示例，勿向参评命名空间写入测试内容。

**Add 请求**：`request_id`、`user_id`、`session_id` 和非空 `messages` 必填；`timestamp` 可选，单位为 Unix 毫秒。

```json
{
  "request_id": "demo-write-001",
  "user_id": "demo-user",
  "session_id": "demo-session-1",
  "messages": [
    {"role": "user", "content": "项目代号是海港，发布日期为 11 月 8 日。", "timestamp": 1793491200000}
  ]
}
```

同步成功为 HTTP 200；必须在持久化完成、相关记忆可被后续 Search 立即检索后返回：

```json
{"success": true, "request_id": "demo-write-001", "user_id": "demo-user", "session_id": "demo-session-1"}
```

**Search 请求**：只在该 `user_id` 范围内检索；同一用户可以跨 `session_id`。开放题省略 `options`；选择题仅传平台提供的选项文本，不含正确答案标签。

```json
{"user_id": "demo-user", "query": "海港项目什么时候发布？", "top_k": 5}
```

响应结构示意，`id`、分数和具体片段由服务生成：

```json
{"data": [{"id": "opaque-memory-id", "content": "[user] 项目代号是海港，发布日期为 11 月 8 日。", "score": 1.0}]}
```

`data` 是按证据优先顺序排列的数组，不增加 `items` 包装，不超过本次 `top_k`；无检索结果返回 `{"data": []}`。有原始时间戳时可附 `created_at`。分数用于排序，不是答案正确概率。

核心约束：

- **隔离**：`user_id` 是边界，不混用其他用户记忆；`session_id` 用于来源组织，不限制同用户跨会话检索。
- **幂等**：同一用户的相同 `request_id` 和载荷重试不重复写入；同标识不同载荷返回 409。重试保留原 ID、消息顺序与载荷。
- **写后可见**：此版本仅同步 Add，不以后台入队或 HTTP 202 代替写入成功。
- **原文证据**：Search 返回已写入内容的原文片段及角色、时间元数据，不生成当前题目的答案、选项字母或外部金标。

错误包括鉴权失败 401、幂等冲突 409、字段或内容校验失败 422、上游 Embedding 暂时不可用 503。未成功返回的请求不能计为已完成；使用有界重试，不无限重试或更换 ID 绕开冲突。完整规范以 [API Guide](https://agentmemories.ai/api-guide) 和 [Documentation](https://agentmemories.ai/docs) 为准。

## 验证、容量与数据管理

离线合成检查：

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

这些检查使用测试编码器与临时数据，不代表正式模型准确率或 Full 规模容量。容量和资源限制见 [OPERATIONS.md](manual/OPERATIONS.md)。Full 异常恢复须遵守平台与主办方的处理要求，不能通过清库、改模型或换算法直接续跑。

仓库不包含评测密钥、私有环境文件、数据库、模型权重、评测题目、标准答案或完整评测日志。评测数据与派生副本仅用于当前任务；依现行规则，在任务完成后 30 天内删除，延期须事先获得主办方书面同意。故障恢复保留要求按主办方确认执行，不把数据上传至 GitHub。

## 文档与许可

[部署与复现](manual/DEPLOYMENT.md) · [运行与恢复](manual/OPERATIONS.md) · [参评材料索引](manual/SUBMISSION.md) · [技术版本差异](manual/METHOD_CHANGES.md) · [版本与许可](PROVENANCE.md) · [MIT 许可证](LICENSE)

版权与许可信息见 [LICENSE](LICENSE)。

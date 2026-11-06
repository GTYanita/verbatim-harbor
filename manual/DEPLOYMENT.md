# Verbatim Harbor v0.1：部署与复现

本说明对应 [README](../README.md) 的固定源码，提供独立环境的安装和运行步骤。

## 1. 环境和密钥

独立复现采用 Python 3.12；仓库 operations/Dockerfile 也采用该版本。安装 [requirements.txt](../requirements.txt) 中的锁定依赖。生产配置不需要本地 GPU 或权重下载，通过 HTTPS 调用百炼 `text-embedding-v4`，需要相应权限、配额与网络。

复制 `env.example` 为私密 `.env` 后设置：

| 变量 | 复现设置 |
| --- | --- |
| `MEMORY_API_KEY` | 本地自行生成的非空鉴权密钥，不复用参评 Token |
| `DASHSCOPE_API_KEY` | 有效的百炼私密凭据 |
| `AE_EMBEDDING_URL` | 账户对应的百炼文本向量同步地址；替换 `{WorkspaceId}` |
| `AE_EMBEDDING_BACKEND` | `dashscope` |
| `AE_EMBEDDING_DIMENSIONS` | `1024` |
| `AE_EMBEDDING_BATCH_SIZE` | `10` |
| `AE_EMBEDDING_TIMEOUT` | `60` 秒，单次上游尝试 |
| `AE_EMBEDDING_MAX_ATTEMPTS` | `3`，有界重试 |
| `AE_EMBEDDING_MAX_REQUESTS` | `0`；适配器不设置请求总数上限，供应商配额仍生效 |
| `AE_DATABASE` | 独立路径，如 `data/verbatim-harbor-v01-review/memory.sqlite3` |
| `AE_MODE` | `query_document_evidence` |
| `AE_CONTEXT_CHARS` | `24000` |
| `AE_ADD_INDEXER` / `AE_PLANNER` / `AE_LOCAL_EVIDENCE_SEARCH` | `0`；不使用生成式链路 |

保持鉴权启用，不设置 `AE_LOCAL_NO_AUTH=1`。模板的旧目录名仅为历史默认值；复现时指定新目录，不连接生产库。数据库、私密配置和密钥不纳入归档。

## 2. Windows

在仓库根目录运行；已有私密 `.env` 时不要覆盖：

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item env.example .env
# 编辑 .env，填写密钥、有效地址和独立 AE_DATABASE 后继续。
.\.venv\Scripts\python.exe tools/preflight.py --env-file .env
.\start_local.ps1 -Port 18401 -PythonPath .\.venv\Scripts\python.exe -EnvFile .env
```

脚本加载环境文件，并以单个 Uvicorn worker 在回环地址监听。另一终端使用自有测试密钥调用 Add/Search；Health 为 `http://127.0.0.1:18401/health`。

## 3. Linux

先复制模板并编辑私密 `.env`，使用合法 Bash 环境变量赋值格式，密钥含特殊字符时正确引用。然后在仓库根目录运行：

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tools/preflight.py --env-file .env
set -a
. ./.env
set +a
.venv/bin/python -m uvicorn adaptive_evidence.api:app --host 127.0.0.1 --port 18401 --workers 1 --no-access-log
```

单 worker 和独立数据库用于保持复现配置清晰。不要临时改变已参评服务的 worker、模型或检索设置。

## 4. 容器复现

独立复现可使用 `operations/Dockerfile`，显式指定新镜像、卷和本地端口：

```bash
docker build -t verbatim-harbor:v0.1-review .
docker volume create verbatim-harbor-v01-review
docker run --rm --name verbatim-harbor-v01-review --env-file .env \
  -e AE_DATABASE=/data/verbatim-harbor-v01-review/memory.sqlite3 \
  -p 127.0.0.1:18401:8000 \
  -v verbatim-harbor-v01-review:/data verbatim-harbor:v0.1-review
```

镜像使用非 root 用户，数据卷须可写；绑定宿主目录时配置相应权限。数据卷与端口应由复现环境独立配置。

## 5. 检查与公网接入

- `python tools/preflight.py --env-file .env`：配置检查，不发真实 Embedding 请求。
- `python tools/preflight.py --env-file .env --live`：临时 SQLite 合成检查，会调用真实 Embedding，有费用与配额消耗；不是官方 Smoke。
- `python -m unittest discover -s tests`：离线合成检查，不证明官方答案成绩或容量。

跨主机访问时由部署者配置有效 HTTPS、路径映射和独立鉴权；应用提供相对路由 `/add`、`/search`、`/health`。

## 6. 文件身份与恢复

源码身份以固定 Commit、归档哈希及逐文件核验为准。持久化与恢复边界见 [OPERATIONS.md](OPERATIONS.md)。

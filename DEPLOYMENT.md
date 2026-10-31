# Verbatim Harbor v0.1：m01 部署

独立源码目录：/opt/memory-lab/releases/m01/evidence-selected-question-v9-7befac6e2c4b

服务：memory-lab@m01.service；后端端口：18101；Python 环境：/opt/memory-lab/venv；独立数据目录：/var/lib/memory-lab/m01。

配置使用 query_document_evidence、24000 字符返回预算和 text-embedding-v4（1024维）。Add/Search 鉴权凭据仅由运营者私密配置提供。Health 的底层软件版本字段继承上游，不代表参赛展示版本。

线上源码与本仓库 adaptive_evidence/ 的生产 Python 必须逐文件一致。共享 /opt/memory-lab/source 以及其他服务不属于本仓库部署目标。发布仓库不会自动改动线上服务。

同 user_id 跨 session_id 检索；不同 user_id 严格隔离。Add 在事务提交、缓存失效且可以立即 Search 后返回200；request_id 重试不重复写入，内容冲突返回409。

Full 前重新检查真实 admission、配额、活动任务、端点、TLS、源码、鉴权和容量。正式受理后不因结果不理想更换版本或撤回。运行中只读监控，保存终态结果及前后源码验证。

服务器资源快照和并发16的合成检查不能证明全部 Full 规模容量。官方数据库、源码包和模型资源须分别管理，不公开评测数据。按赛事数据保留规则处理副本和备份，不跨用户或团队共享。

本仓库使用继承的 MIT 实现；原作者和来源、修改清单见 PROVENANCE.md，版权和许可证见 LICENSE。

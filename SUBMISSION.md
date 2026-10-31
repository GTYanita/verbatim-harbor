# Verbatim Harbor v0.1 提交信息草稿

参赛者：高天翊

所属单位：北京理工大学

赛道：Textual；参赛组别以账号已审核绑定信息为准，不能据此草稿更改。

仓库：https://github.com/GTYanita/verbatim-harbor

版本：v0.1；候选：selected-original-question-answer-pair-v9。固定 commit 在发布后补充。

Original Work：由参赛者自行补充；基础实现不列为本申请原创贡献。复用内容和全部修改单独披露于 PROVENANCE.md，LICENSE 保持。

Add：https://101.201.226.162/m01/add

Search：https://101.201.226.162/m01/search

Health：https://101.201.226.162/m01/health

Add/Search 使用已登记的 Token 鉴权，密钥不出现在仓库、URL、截图或此说明中。Health 无需鉴权。使用同步 Add；未申报异步 Add 状态接口。

正式请求保持平台原生字段和当前 options：max_add_concurrency=16、search_concurrency=16、top_k=100。统一 Answer/Judge 设置归平台所有，本服务不覆盖其提示或模型。

本服务 Add/Search 不调用生成模型，仅使用 text-embedding-v4、1024 维向量及确定性原文检索。关于开源方法榜 Add 模型要求，应以赛事现行规则和审核结果为准；未采用其他生成模型。

本地完整有效评分仍有缺失，不宣称已证明准确率提升或 Full 成绩。Smoke 完成不代表 Full 容量或成绩保证。

Full 受理前须完成信息补充与本人确认；受理后固定生产代码、版本、接口、依赖和配置，避免同一服务评测或部署冲突。

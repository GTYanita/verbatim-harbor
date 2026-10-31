# Verbatim Harbor v0.1 提交信息草稿

参赛者：高天翊

所属单位：北京理工大学

赛道：Textual；参赛组别以账号已审核绑定信息为准，不能据此草稿更改。

仓库：https://github.com/GTYanita/verbatim-harbor

版本：v0.1；候选：selected-original-question-answer-pair-v9。固定源码以 RELEASE_IDENTITY.json 的部署归档SHA256及本仓库当前提交为准。

Original Work：本次方法改动是已选原文提问与相邻原助手回答的局部组织：同 session/request、位置相邻、提问不超过512字符且带问号，并含回答缺失的原查询词时，将最多一条已选完整提问移到该回答之前。保持原文字节和来源，不生成答案、不新增外部知识、不改变平台模型、提示或评分。基础检索、存储、选材和预算能力均为复用内容，不作为本申请原创贡献；原作者、许可证及全部方法修改见 PROVENANCE.md。此说明不主张学术首创性。

Add：https://101.201.226.162/m01/add

Search：https://101.201.226.162/m01/search

Health：https://101.201.226.162/m01/health

Add/Search 使用已登记的 Token 鉴权，密钥不出现在仓库、URL、截图或此说明中。Health 无需鉴权。使用同步 Add；未申报异步 Add 状态接口。

正式请求保持平台原生字段和当前 options：max_add_concurrency=16、search_concurrency=16、top_k=100。统一 Answer/Judge 设置归平台所有，本服务不覆盖其提示或模型。

本服务 Add/Search 不调用生成模型，仅使用 text-embedding-v4、1024 维向量及确定性原文检索。关于开源方法榜 Add 模型要求，应以赛事现行规则和审核结果为准；未采用其他生成模型。

本地完整有效评分仍有缺失，不宣称已证明准确率提升或 Full 成绩。Smoke 完成不代表 Full 容量或成绩保证。

Textual Full已受理：teval_cc46e8ef0571706c。参赛者已确认本次提交及本地评分缺项；受理后固定生产代码、版本、接口、依赖和配置，暂缓同服务Smoke。材料完整性与参赛资格仍以赛事方审核为准。

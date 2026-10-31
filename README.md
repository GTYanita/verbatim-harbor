# Verbatim Harbor（原文港）v0.1

参赛者：高天翊。所属单位：北京理工大学。仓库账号：GTYanita。

本仓库对应 m01 的冻结候选 `selected-original-question-answer-pair-v9`。系统保存原始记忆，结合向量与词法检索返回原文证据；统一 Answer、代码任务执行和评分由赛事平台负责。

## Original Work

本次方法改动是已选原文提问与相邻原助手回答的局部组织：同 session/request、位置相邻、提问不超过512字符且带问号，并含回答缺失的原查询词时，将最多一条已选完整提问移到该回答之前。保持原文字节和来源，不生成答案、不新增外部知识、不改变平台模型、提示或评分。基础检索、存储、选材和预算能力均为复用内容，不作为本申请原创贡献；原作者、许可证及全部方法修改见 PROVENANCE.md。此说明不主张学术首创性。

## 接口

|接口|地址|
|---|---|
|Add|https://101.201.226.162/m01/add|
|Search|https://101.201.226.162/m01/search|
|Health|https://101.201.226.162/m01/health|

Add 同步持久化，以 user_id 隔离、request_id 幂等。同一 user_id 可跨 session_id 检索。Search 返回按证据优先顺序排列的 data 数组，条数不超过 top_k；无结果返回 {"data": []}。不把当前问题答案、选项或外部金标生成或拼接为记忆。

源码归档 SHA256：`7befac6e2c4b2dc0b7e31c7e78b8cb783bcf5ca7cd26397e53d88ef3078cf2e5`。仓库文档独立于该已冻结的部署归档，生产 Python 按逐文件哈希一致性核验。

[部署](DEPLOYMENT.md) · [提交材料](SUBMISSION.md) · [方法来源和修改](PROVENANCE.md) · [MIT 许可证](LICENSE)

仓库不包含凭据、环境私密文件、数据库、模型权重、评测题目或标准答案。Textual Full 已于北京时间2026-10-31 23:49受理，任务 teval_cc46e8ef0571706c；受理期间冻结生产源码、配置和依赖。材料是否完整合规以赛事方审核为准。

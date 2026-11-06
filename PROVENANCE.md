# 当前参赛版本与技术记录

参赛者：高天翊（北京理工大学）；系统展示名 Verbatim Harbor v0.1。

固定源码提交：`e84af580a3a9a21f1eab6328d41e8b93bb52552e`；对应归档 SHA256：`bff4443ee3cbdf4a5e320dfa56fb8e65ca7775d857550c4112de7ddb7a9c74fa`。许可见 [LICENSE](LICENSE)。

当前输出组织由以下模块处理： evidence_pipeline/adaptive_evidence/selected_question_pairs.py，并在 evidence_pipeline/adaptive_evidence/focused_packing.py 接入最终输出顺序调整。最多将一条已经选入的完整短用户提问移动至同次写入、紧邻的原助手回答前；不新增证据、查询、全历史画像、生成答案、模型调用或检索状态，不改变内部来源选择和预算。

下方技术记录用于版本复现与许可核验。

## 历史技术记录

以下按版本记录接口、模型与技术配置；当前参评范围以前述固定文件身份和运行说明为准。

### 模型与接口记录

代码采用 [MIT 许可证](LICENSE)，版权通知见许可证正文。

2026-09-29：0.2.0 默认 Embedding 改为百炼 `text-embedding-v4`（1024 维）；BGE 仅保留在历史实验路径。适配器使用[百炼原生文本向量同步 API](https://help.aliyun.com/zh/model-studio/text-embedding-synchronous-api/)，未包含模型权重。方法与验证范围见 README、SUBMISSION 和 PILOT_RESULTS。

历史模型与诊断数据：

- [BGE-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5)：历史实验使用的嵌入模型；模型适用其许可证与模型卡。0.2.0 配置使用 text-embedding-v4。
- [LoCoMo-Refined](https://github.com/mem-eval-suite/LoCoMo_refined)：本地公开诊断数据，发布候选包不附带数据或答案。

API 契约依据 [AML API Guide](https://agentmemories.ai/api-guide)。历史规划模块接口依据 [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) 和 [GPT-4o-mini](https://developers.openai.com/api/docs/models/gpt-4o-mini)。第二期规则已于 2026-09-29 重新核验，当前按赛事 FAQ 的模型要求准备，详见 README_CYCLE2.md。

代码采用 MIT 许可；依赖、模型和数据适用各自许可证。发布包不包含模型权重、原始诊断数据或标准答案。

## 0.3.0 Add 阶段更新（2026-10-06）

新增通过 [OpenRouter Chat Completions](https://openrouter.ai/docs/quickstart) 调用 `openai/gpt-4o-mini` 的适配器。新增的 Add 索引处理使用模型选择原文短语，代码验证其为原文子串，再用于向量与 BM25 索引加权。模型输出不会作为新事实或最终答案返回。提供方固定为 OpenAI，使用[结构化输出](https://openrouter.ai/docs/guides/features/structured-outputs)及[提供方参数约束](https://openrouter.ai/docs/guides/routing/provider-selection)。这是新的方法配置，其效果需要单独验证；历史基线分数不能直接移作本版本成绩。

## 0.3.1 reliability update (2026-10-08)

This version replaced free-form cue copying with integer selection of deterministic source spans, added private per-request batch checkpoints and sanitized diagnostic logs. This changes the method identity and requires an independently bound version and a fresh database. It does not claim a measured quality improvement.

## 0.4.0 local model option (2026-10-08)

Added an explicitly selected loopback Chat Completions backend, actual-model reporting and model/runtime profile isolation. Shared source-span validation and the original OpenRouter GPT-4o-mini request behavior are retained. Local compatibility adds the schema to the prompt and has its own identity.

Local validation used existing [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) weights; its local model card declares Apache-2.0. Model weights, tokenizer and third-party library binaries are not redistributed in this package. local_runtime/ contains the exact existing project model-server source and a runtime/weight hash manifest; the model remains subject to its own license. This profile is not covered by the 0.3.1 official Smoke result.

## 0.4.1 runtime reliability update (2026-10-08)

Added a supervised GPU worker process, bounded request queue, cancellation/deadlines, shared single/batch tensor cleanup and sanitized runtime metrics. The original 0.4.0 loading helpers remain, while supervised serving uses the new generation lifecycle. All nine external model/tokenizer file hashes were rechecked and match 0.4.0. Source-span prompts, indexing/retrieval behavior and cloud fallback policy are unchanged. The runtime identity and database are new; the 0.4.0 official Smoke score does not certify this version.


## 0.6.0 local evidence planner

Bounded query planning and source-identifier selection. Local select6 experiment scores are not official scores. Add and embedding behavior remain at the 0.4.1 configuration.

## 0.6.1 batch-selection correction

Batch-selection correction: explicit irrelevant-batch abstention, a validated 16-ID limit, and deterministic BM25 accumulation.

## 0.27.0 raw-source memory (2026-10-13)

Remove generative Add indexing and generative Search planning from this release. Retain original-source hybrid retrieval and source windows. Generative Answer belongs to the external evaluator. Embedding remains text-embedding-v4. Historical sections above describe prior releases, not enabled components in this package.

## 0.28.0 deterministic evidence windows (2026-10-13)

Budget-aware neighbor reservation, exact overlap merging and within-Add source ordering, combined with the existing SQLite Porter lexical view. Add and embedding settings are unchanged from 0.27.0. Public paired retrieval diagnostics are described in README.md; no official score is implied.


##0.29.0 relevant source admission (2026-10-13)

Version update: relevance-first source packing, bounded distinct-source admission, exact source overlap merging and bounded original user standing-instruction reservation. Existing embeddings and query calls are unchanged; production uses focus_stem_rules. Research-only contextual, fine-passage and phrase variants are not selected for this release.

The public comparison holds stored sources and embedding identity constant. LLM fact consolidation and Answer fallback are excluded.

## 0.30.0 conditional original-source provenance (2026-10-14)

Add an original-user Porter lexical ranking stream only for scopes dominated by one long original user document; otherwise preserve 0.29 ranking. No generative extraction, model reranking, or extra embedding request. LLM compilation, code generation, and answer correction are excluded.

Public CL-Bench data (https://huggingface.co/datasets/tencent/CL-bench) was used only in isolated local diagnostics. The primary authors' repository mirror was verified against the publisher's SHA-256. No benchmark-specific answer, task identifier, or public/private dataset is included in the source package. Dataset licenses remain separate from the implementation's MIT license.
## 0.31.0 query-local source coherence (2026-10-14)

Routing uses already-computed dense scores, original role/offsets, and literal same-source section references. Direct document lookup and prior-answer references use distinct lexical views while preserving all source roles. No task identifiers or benchmark answers occur in production routing.

## 0.32.0 direct evidence budget (2026-10-14)

Source packing protects direct matches before bounded original source expansion. Ranking, prompt, embeddings and call counts are unchanged from 0.31. Public tests are isolated from official evaluation. Production routing does not contain task identifiers or reference answers. No generative consolidation or compiler is introduced.
# Verbatim Harbor（原文港）

Public source for the m01 memory service, based on **Context Weave / SourceTrail 0.32.0**, originally authored by **王子铭 (Giorno-Banana)** and distributed under the [MIT license](LICENSE). Application contact: 高天翊. Repository account: GTYanita.

This package preserves the exact0.32 production Python files. The new display name and deployment documentation do not represent a new retrieval algorithm or a verified score improvement. The current research candidate and its incomplete local evaluation are excluded.

## Service

| API | Address |
|---|---|
| POST Add | https://101.201.226.162/m01/add |
| POST Search | https://101.201.226.162/m01/search |
| GET Health | https://101.201.226.162/m01/health |

Add stores original text, roles, source offsets and available timestamps. Search combines text-embedding-v4 with lexical retrieval and deterministic original-evidence packing. Default mode is query_document_evidence, with a24000-character return budget and top_k≤100. The memory service makes no generative LLM call; final Answer/Judge belongs to the external evaluator.

Add/Search require the server private memory-system key. Health is public. Never commit keys, GitHub credentials, private environment files, databases, model weights or evaluation data.

## Reproduction and attribution

- [Deployment and API registration notes](DEPLOYMENT.md)
- [Unchanged original release README](README.exact32.md)
- [Original method sources and release history](PROVENANCE.md)
- [Frozen source identity](RELEASE_IDENTITY.json)
- [Original MIT copyright and license](LICENSE)

Install requirements.txt in a separate environment and follow DEPLOYMENT.md or the original startup instructions. Publishing this repository does not reconfigure the existing m01 host. There is no official score for this registration.

# m01 deployment

Application display name: **Verbatim Harbor（原文港）**. The implementation is the unchanged Context Weave / SourceTrail 0.32.0 source by 王子铭 (Giorno-Banana), distributed under MIT. Keep LICENSE, PROVENANCE.md and README.exact32.md with every copy.

## Public API

| Purpose | Endpoint |
|---|---|
| Add, POST | https://101.201.226.162/m01/add |
| Search, POST | https://101.201.226.162/m01/search |
| Health, GET | https://101.201.226.162/m01/health |

The deployment supplied by the operator returned HTTP 200 and status=ok at its health endpoint on 2026-10-31 (Asia/Shanghai). It reported version 0.32.0, text-embedding-v4, raw_source Add, query_document_evidence Search, context_chars=24000 and no generative LLM in the memory service. This observation does not establish throughput, long-term availability or capacity.

Add and Search authenticate with `Authorization: Token <MEMORY_API_KEY>`; the source also supports Bearer or X-Api-Key. Health is public. Add is synchronous; do not invent an asynchronous Add-status endpoint. The memory-system key must equal the private server-side MEMORY_API_KEY. Do not use a GitHub password or an AML eval_key for this field.

## Reproduce on a separate host

Use a supported Python environment, install requirements.txt, and configure private environment values following env.example. Set an explicit separate AE_DATABASE, MEMORY_API_KEY, DASHSCOPE_API_KEY, and the account's correct AE_EMBEDDING_URL. Keep AE_MODE=query_document_evidence and AE_CONTEXT_CHARS=24000. No credentials, environment files or databases belong in Git.

The Dockerfile starts the FastAPI application on port8000. Configure the reverse proxy to remove `/m01` before forwarding to this application. The container does not terminate TLS. Use a valid certificate covering the public endpoint. See README.exact32.md and start_local.ps1 for the original startup path; compose.yaml is inherited historical configuration and is not a claim about this m01 host.

The supplied m01 host is managed separately. Publishing this repository does not deploy or reconfigure that host. The health response alone does not prove its running file hashes equal this repository; server-side release verification remains required.

## Evaluation limits

Return at most the caller's top_k (maximum100), within a 24000-character Search budget. This is the service's return budget, not a claim about the evaluator's final input limit. Start compatibility testing conservatively with Add/Search concurrency1 until the operator validates capacity.

There is no official score for this new registration. Historical scores for other registrations do not transfer to this display name. No Smoke/Full evaluation, version binding or promotion is authorized by publishing this repository.

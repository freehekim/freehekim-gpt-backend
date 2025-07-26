# FreeHekim GPT Backend

Bu backend, OpenAI GPT-4 API ile çalışan basit bir FastAPI servisini içerir.
Render üzerinde çalıştırmak için yapılandırılmıştır.

## Ortam Değişkenleri

- OPENAI_API_KEY
- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET
- AZURE_TENANT_ID
- AZURE_SCOPE

## Başlatma

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

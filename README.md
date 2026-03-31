# InsightSQL Assistant

API backend desenvolvida com Python e FastAPI para simular um assistente de BI conversacional com foco em consultas analíticas sobre vendas.

## Objetivo

O projeto foi criado como portfólio para demonstrar habilidades em:

- desenvolvimento backend com Python
- construção de APIs com FastAPI
- modelagem de dados com SQLAlchemy
- uso de SQLite para persistência
- organização modular de rotas
- documentação automática com Swagger
- seed automático de dados para demonstração
- separação de lógica analítica em camada de serviço

## Funcionalidades atuais

- Listagem de vendas
- Cadastro de vendas
- Filtro de vendas por região
- Resumo analítico de vendas
- Banco SQLite local
- Seed automático com dados de exemplo
- Swagger UI para testes
- Insights de vendas por região
## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic

## Rotas principais

- `GET /`
- `GET /health`
- `GET /sales`
- `POST /sales`
- `GET /sales/region/{region_name}`
- `GET /sales/summary`
- `GET /sales/insights/regions`
## Como executar

```bash
cd ~/Área\ de\ trabalho/InsightSQL-Assistant
source .venv/bin/activate
uvicorn main:app --reload

Documentação da API

Após subir o servidor, acesse:

http://127.0.0.1:8000/docs

Estrutura do projeto
InsightSQL-Assistant/
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   └── sales.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── analytics.py
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── seed.py
├── data/
├── docs/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

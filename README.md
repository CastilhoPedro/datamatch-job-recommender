# DataMatch 📊

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-blue)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**Um motor de busca de vagas na área de dados que ranqueia oportunidades pelas competências exigidas na descrição — não pelo título.**

Você informa suas habilidades (ex: `Python`, `Spark`, `dashboards`) e o sistema retorna vagas compatíveis, ordenadas por relevância via TF-IDF + Similaridade de Cosseno.

---

## 🎯 Motivação

Títulos de vaga na área de dados são caóticos: "Analista de Dados", "Analista de BI", "Cientista de Dados" e "Engenheiro de Analytics" frequentemente descrevem o mesmo trabalho — ou o mesmo título esconde exigências completamente diferentes. Isso deixa estudantes e profissionais perdidos sobre onde suas habilidades realmente se encaixam.

O **DataMatch** ataca esse problema ignorando o título e olhando para o que importa: **as competências técnicas efetivamente exigidas na descrição da vaga.**

---

## 🏗️ Arquitetura

O projeto segue uma **arquitetura em camadas com fluxo unidirecional**. Cada camada tem uma única responsabilidade e só conversa com a camada seguinte — o frontend nunca acessa scraper ou vetorizador diretamente, sempre passa pela camada de serviços.

```mermaid
flowchart LR
    A[Scrapers<br/>Selenium] --> B[(Database<br/>PostgreSQL)]
    B --> C[Processing<br/>NLP + TF-IDF]
    C --> D[Services<br/>handler_front]
    D --> E[Frontend<br/>Streamlit]
    E -.feedback.-> D
```

**Por que essa separação importa:** ela isola o motor de matching (regras de relevância vivem em `processing`, não no banco), permite trocar a fonte de dados sem tocar no frontend, e torna cada peça testável de forma independente. É a aplicação prática de *Separation of Concerns* e do princípio de *Dependency Direction*.

### Decisões técnicas de destaque

- **Persistência do modelo** com `joblib` (`.joblib`) — o vetorizador TF-IDF é treinado e salvo, não recalculado a cada busca.
- **Repository-like layer** (`database.py`) centralizando o CRUD, com um *decorator* para eliminar boilerplate de escrita (DRY).
- **Session management** via context managers do SQLAlchemy — sem vazamento de conexões.
- **Segredos fora do código** — credenciais e `DATABASE_URL` lidos de variáveis de ambiente (`config/settings.py`).
- **Schema versionado** com Alembic, em vez de `create_all` no import.

---

## ✨ Status das Funcionalidades

| Funcionalidade | Estado |
| :--- | :--- |
| Busca por competências (input do usuário) | ✅ Implementado |
| Matching TF-IDF + Similaridade de Cosseno | ✅ Implementado |
| Ranqueamento de vagas por relevância | ✅ Implementado |
| Interface Streamlit com cards de vaga | ✅ Implementado |
| Filtros (senioridade, data de publicação) | ✅ Implementado |
| Pré-processamento NLP (spaCy) | 🟡 Existe, ainda não ligado ao vetorizador |
| Scraping (LinkedIn) | 🟡 Base em Selenium; scrapers por fonte a modularizar |
| Scraping (Glassdoor / Catho) | ⬜ Planejado |
| Sistema de feedback (Like / Dislike) | ⬜ Planejado |

---

## 🛠️ Stack

| Categoria | Ferramentas |
| :--- | :--- |
| **Coleta de dados** | Selenium, BeautifulSoup |
| **NLP / ML** | spaCy (`pt_core_news_sm`), scikit-learn (TF-IDF, cosine similarity) |
| **Persistência** | PostgreSQL, SQLAlchemy, Alembic |
| **Modelo** | joblib |
| **Frontend** | Streamlit |
| **Conceitos** | Web Scraping, NLP, Sistemas de Recomendação, Similaridade Vetorial |

---

## 🚀 Como Executar

> ⚠️ Projeto em desenvolvimento. Alguns componentes (scraping multi-fonte, feedback) ainda estão em construção.

**Pré-requisitos:** Python 3.x e uma instância PostgreSQL acessível.

```bash
# 1. Clonar o repositório
git clone https://github.com/<seu-usuario>/datamatch-job-recommender.git
cd datamatch-job-recommender

# 2. Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Baixar o modelo de linguagem do spaCy
python -m spacy download pt_core_news_sm
```

Configure as variáveis de ambiente num arquivo `.env` na raiz:

```env
# ⚠️ Confirme os nomes exatos das variáveis em src/backend/config/settings.py
DATABASE_URL=postgresql://usuario:senha@localhost:5432/datamatch
# ... demais credenciais de scraping, se aplicável
```

```bash
# 5. Aplicar as migrações do banco (Alembic)
alembic upgrade head          # ⚠️ ajuste conforme a config do alembic.ini

# 6. Rodar a aplicação
streamlit run src/frontend/app/main.py
```

---

## 📁 Estrutura do Projeto

```
datamatch-job-recommender
├─ notebooks/            # Exploração: NLP e scraping
├─ requirements.txt
└─ src
   ├─ backend
   │  ├─ config/         # settings.py — env vars e segredos
   │  ├─ database/       # connection, models, database (CRUD)
   │  ├─ processing/     # nlp.py, vectorizer.py (TF-IDF + cosseno)
   │  ├─ scrapers/       # common.py (Selenium), linkedin, glassdoor
   │  ├─ services/       # handler_front.py — ponte back <-> front
   │  └─ utils/
   ├─ frontend
   │  ├─ app/            # main.py — aplicação Streamlit
   │  └─ utils/          # helpers de UI
   └─ utils/             # helper.py — listas fixas (skills, UFs, etc.)
```

---

## 🛣️ Roadmap

- [ ] **Modularizar os scrapers** por fonte (LinkedIn, Glassdoor, Catho) sobre uma base comum; avaliar migração para Scrapy/Playwright.
- [ ] **Conectar o pré-processamento NLP** (lematização, stopwords) ao pipeline de vetorização.
- [ ] **Modelos contextuais:** evoluir de TF-IDF para embeddings (BERT) e capturar semântica além da sobreposição de palavras.
- [ ] **Personalização via feedback:** usar os sinais de Like/Dislike para refinar o ranqueamento.
- [ ] **Performance:** indexação para manter a busca rápida conforme a base de vagas cresce.

---

## 📄 Licença

Distribuído sob a licença MIT. <!-- ⚠️ adicione um arquivo LICENSE se ainda não houver -->

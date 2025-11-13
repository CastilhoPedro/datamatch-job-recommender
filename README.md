# DataMatch 📊

![Status](https://img.shields.io/badge/status-em%20planejamento-yellow)

Um motor de busca focado em competências para vagas na área de dados, que conecta as habilidades dos profissionais às reais exigências do mercado.

## 🎯 Objetivo

O objetivo principal do DataMatch é esclarecer o caminho para profissionais que se sentem perdidos no mercado de dados, ajudando-os a identificar onde suas habilidades se encaixam melhor e quais vagas são mais adequadas ao seu perfil e nível técnico. Para isso, o projeto se propõe a desenvolver um motor de busca especializado que conecta profissionais a oportunidades de emprego com base em suas competências técnicas, e não apenas em títulos de vagas.

A motivação surgiu da dificuldade enfrentada por estudantes e profissionais da área, que frequentemente encontram inconsistências entre os títulos das vagas e as habilidades que são, de fato, exigidas.

## ✨ Funcionalidades Planejadas

* **Busca por Habilidades:** O usuário insere suas competências técnicas (ex: "Python", "Spark", "dashboards") e o sistema busca vagas compatíveis.
* **Matching Inteligente:** Um algoritmo baseado em TF-IDF e Similaridade de Cosseno ranqueará as vagas, priorizando a relevância das habilidades inseridas pelo usuário na descrição da vaga.
* **Web Scraping Contínuo:** O sistema coletará vagas de forma automatizada das principais plataformas (LinkedIn, Glassdoor, Catho) para manter a base de dados sempre atualizada.
* **Interface Intuitiva:** Uma interface simples, desenvolvida com Streamlit, permitirá que o usuário filtre os resultados por nível de senioridade e data de publicação.
* **Sistema de Feedback:** Um mecanismo de "Like" e "Dislike" será implementado para coletar feedback do usuário e, futuramente, aprimorar a precisão das recomendações.

## 🛠️ Tecnologias

A arquitetura do projeto integra diversas ferramentas e conceitos da engenharia e ciência de dados:

| Categoria             | Ferramentas e Conceitos                                     |
| :-------------------- | :---------------------------------------------------------- |
| **Coleta de Dados** | Scrapy, BeautifulSoup, Selenium                               |
| **Processamento e NLP** | Scikit-learn, Spacy                                       |
| **Banco de Dados** | PostgreSQL                                                     |
| **Interface (Frontend)**| Streamlit                                                 |
| **Conceitos Base** | Web Scraping, Processamento de Linguagem Natural (NLP), Sistemas de Recomendação |

## 🚀 Como Executar o Projeto

>  **Atenção:** O projeto ainda está em fase de planejamento. As instruções detalhadas de instalação e execução serão disponibilizadas futuramente.

## 📁 Estrutura do Projeto

A estrutura de diretórios planejada para organizar o código e os artefatos do projeto é a seguinte:

```
datamatch-job-recommender
├─ notebooks
│  ├─ 01_NLP_development.ipynb
│  └─ 02_Scraper_development.ipynb
├─ README.md
├─ requirements.txt
└─ src
   ├─ backend
   │  ├─ config
   │  │  ├─ settings.py
   │  │  └─ __init__.py
   │  ├─ database
   │  │  ├─ connection.py
   │  │  ├─ database.py
   │  │  ├─ models.py
   │  │  └─ __init__.py
   │  ├─ processing
   │  │  ├─ nlp.py
   │  │  ├─ utils
   │  │  │  ├─ model_persistence.py
   │  │  │  └─ __init__.py
   │  │  ├─ vectorizer.py
   │  │  └─ __init__.py
   │  ├─ scrapers
   │  │  ├─ common.py
   │  │  ├─ glassdoor.py
   │  │  ├─ linkedin.py
   │  │  └─ __init__.py
   │  ├─ services
   │  │  ├─ handler_front.py
   │  │  └─ __init__.py
   │  ├─ utils
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ frontend
   │  ├─ app
   │  │  ├─ main.py
   │  │  └─ __init__.py
   │  ├─ utils
   │  │  ├─ commom.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ utils
   │  ├─ helper.py
   │  └─ __init__.py
   └─ __init__.py

```


## 🛣️ Próximos Passos (Roadmap)

Embora o algoritmo inicial seja baseado em TF-IDF, o plano de longo prazo inclui aprimoramentos significativos:

* **Migração para Modelos Contextuais:** Evoluir o algoritmo de matching para modelos de linguagem mais avançados, como o BERT, para capturar melhor o contexto e a semântica das descrições das vagas.
* **Personalização com Feedback:** Utilizar os dados de feedback (Likes/Dislikes) para treinar um modelo de recomendação mais personalizado.
* **Otimização de Performance:** Implementar técnicas de indexação para garantir que o sistema continue performático à medida que a base de vagas crescer.



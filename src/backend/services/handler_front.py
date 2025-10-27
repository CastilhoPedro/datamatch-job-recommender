import time
from src.utils.helper import dates
from src.backend.processing.vectorizer import Vectorizer
from src.backend.database.database import Database

db = Database()

def get_jobs():
    # import pandas as pd
    # df = pd.read_sql("SELECT * FROM vagas_raw", SessionLocal().bind)
    # jobs = df.to_dict(orient="records")

    jobs = [
    {
        "titulo": "Histórico de Ocupação",
        "empresa": "ITA",
        "local": "Itapevi, SP",
        "fonte": "SILT",
        "nivel": "Jr",
        "link": "https://sistema.ssw.inf.br/bin/ssw0422"
    },
    {
        "titulo": "Entradas e Saidas",
        "empresa": "VIX",
        "local": "Vitória, ES",
        "fonte": "SILT",
        "nivel": "Sr",
        "link": "https://ativalogprd.seniorcloud.com.br/siltwms/#tarefasprincipais"
    },
        {
        "titulo": "Histórico de Ocupação",
        "empresa": "ITA",
        "local": "Itapevi, SP",
        "fonte": "SILT",
        "nivel": "Jr",
        "link": "https://sistema.ssw.inf.br/bin/ssw0422"
    },
    {
        "titulo": "Entradas e Saidas",
        "empresa": "VIX",
        "local": "Vitória, ES",
        "fonte": "SILT",
        "nivel": "Sr",
        "link": "https://ativalogprd.seniorcloud.com.br/siltwms/#tarefasprincipais"
    },
        {
        "titulo": "Histórico de Ocupação",
        "empresa": "ITA",
        "local": "Itapevi, SP",
        "fonte": "SILT",
        "nivel": "Jr",
        "link": "https://sistema.ssw.inf.br/bin/ssw0422"
    },
    {
        "titulo": "Entradas e Saidas",
        "empresa": "VIX",
        "local": "Vitória, ES",
        "fonte": "SILT",
        "nivel": "Sr",
        "link": "https://ativalogprd.seniorcloud.com.br/siltwms/#tarefasprincipais"
    }
    
        ]
    return jobs

def process_user_data(skills: list, localization: str, date: str, seniority: str):
    # time.sleep(2.4)
    date = dates[date]
    
    vec = Vectorizer()
    list_jobs = vec.get_vagas_rank(' '.join(skills))
    
    jobs = db.read_vagas_list(
        date=date,
        ids_list=list_jobs,
        localization=localization,
        seniority=seniority
    )
    
    return jobs


if __name__ == '__main__':
    teste = process_user_data(
        skills=['python', 'sql'],
        localization='SP',
        date='Últimos 30 dias',
        seniority='Júnior'
    )
    print(teste)
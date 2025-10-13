import time


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

def process_user_data(skills: list, localization: str, date: int, seniority: str):
    time.sleep(2.4)
    print(f" A lista de skills do usuário são: {[f"{skill}" for skill in skills]}\n Usuário reside em: {localization}\n Quantidade de dias atrás: {date}\n Nível de senioridade: {seniority}")
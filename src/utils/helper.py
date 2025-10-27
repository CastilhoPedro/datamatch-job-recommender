import datetime
from datetime import date


skills_list = [
    "Power BI", 
    "Power Automate", 
    "Banco de dados", 
    "SQL Server"
]

ufs_dict = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins"
}

seniority = [
    'Estágio',
    'Júnior',
    'Pleno',
    'Sênior'
]

dates = {
    'Último dia': date.today() - datetime.timedelta(days=1),
    'Últimos 3 dias': date.today() - datetime.timedelta(days=3),
    'Últimos 7 dias': date.today() - datetime.timedelta(days=7),
    'Últimos 15 dias': date.today() - datetime.timedelta(days=15),
    'Últimos 30 dias': date.today() - datetime.timedelta(days=300)
}
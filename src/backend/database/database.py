from backend.database.models import *
from backend.database.connection import engine


class Database:
    def __init__(self):
        Base.metadata.create_all(bind= engine)


    # precisaremos fazer as funções para adicionar linhas e alrerar linhas (coluna 'processada' de false para true)
    # def 


if __name__ == '__main__':
    db = Database()
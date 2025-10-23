from src.backend.database.models import *
from src.backend.database.connection import *
from sqlalchemy.exc import IntegrityError

class Database:
    def __init__(self):
        Base.metadata.create_all(bind= engine)

    @staticmethod
    def create_row(func):
        def wrapper(self, *args, **kwargs):
            with SessionLocal() as db:
                new_row = func(self, *args, **kwargs)
                
                db.add(new_row)
                try:
                    db.commit()
                    print('linha adicionada com sucesso!')
                except IntegrityError: # depois criar uma camada de logging
                    print('ERRO de integridade do banco')
        return wrapper
    
    # precisaremos fazer as funções para adicionar linhas e alrerar linhas (coluna 'processada' de false para true)
    @create_row
    def add_vaga_raw(self, nome_vaga: str, descricao_vaga: str, nome_empresa: str, localizacao: str, url: str) -> Vagas:
        return Vagas(
            nome_vaga= nome_vaga,
            descricao_vaga= descricao_vaga,
            nome_empresa= nome_empresa,
            localizacao= localizacao,
            url= url
        )

    @create_row
    def add_senioridade(self, nivel: str) -> Senioridade:  # talvez deixe de existir
        return Senioridade(nivel= nivel)
    
    @create_row
    def add_vetor(self, id_vaga: int, vetor: float) -> Vetores:
        return Vetores(
            id_vaga=  id_vaga, 
            vetor= vetor
        )

    def update_vaga_to_processed(self, id_vaga):
        with SessionLocal() as db:
            vaga = db.query(Vagas).filter(Vagas.id_vaga == id_vaga).first()
            vaga.processado = True
            db.commit()


if __name__ == '__main__':
    db = Database()


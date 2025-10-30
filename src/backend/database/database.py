from src.backend.database.models import *
from src.backend.database.connection import *
from sqlalchemy.exc import IntegrityError

class Database:
    def __init__(self):
        try:
            Base.metadata.create_all(bind= engine)
        except UnicodeDecodeError:
            raise UnicodeDecodeError("Houve um problema ao conectar ao banco, por favor verifique se o mesmo está ativado. Caso esteja, cheque as credenciais no arquivo de ambiente")

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
    

    @create_row
    def add_vaga(self, nome_vaga: str, descricao_vaga: str, nome_empresa: str, url: str, data_publicacao: datetime) -> Vagas:
        return Vagas(
            nome_vaga= nome_vaga,
            descricao_vaga= descricao_vaga,
            nome_empresa= nome_empresa,
            url= url,
            data_publicacao= data_publicacao
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

    def update_vaga_to_processed(self, id_vaga) -> None:
        with SessionLocal() as db:
            vaga = db.query(Vagas).where(Vagas.id_vaga == id_vaga).first()
            vaga.processado = True
            db.commit()

    def read_vaga_description_list(self) -> list[str]:
        with SessionLocal() as db:
            descr_list = db.query(Vagas.id_vaga, Vagas.descricao_vaga).where(
                Vagas.processado == False, 
                ) 
            return [i for i in descr_list.all()] 
    
    
    def read_vagas_list(self, localization: str, seniority: str, date: datetime, ids_list: list) -> list[str]:
        with SessionLocal() as db:
            # descr_list = db.query(Vagas).join(Localizacao, Vagas.id_localizacao == Localizacao.id).join(Senioridade,Vagas.senioridade == Senioridade.id).where(
            #     Vagas.processado == False, 
            #     Vagas.data_publicacao >= date, 
            #     # Localizacao.uf == localization,
            #     # Senioridade.nivel == seniority,
            #     Vagas.id_vaga.in_(ids_list)
            #     ) 
            descr_list = db.query(Vagas).where(
                Vagas.processado == False, 
                Vagas.data_publicacao >= date, 
                Vagas.id_vaga.in_(ids_list)
            )
            
            return [
                {
                "titulo": i.nome_vaga,
                "empresa": i.nome_empresa,
                "local": "Teste",
                "fonte": "Teste",
                "nivel": i.senioridade,
                "link": i.url
                } 
                for i in descr_list.all()]   # no futuro precisaremos fazer uma função para extrair os vetores das vagas 

if __name__ == '__main__':
    db = Database()
    print(db.read_vaga_description_list())
    
    
    
        
    # db.add_vaga(
    #     nome_vaga='cientista de dados pleno',
    #     descricao_vaga='procuramos um cientista de dados pleno com experiência em machine learning, python, pandas e visualização de dados. desejável conhecimento em cloud (aws ou gcp).',
    #     nome_empresa='tech insights',
    #     url='www.techinsights.com/vagas/123',
    #     data_publicacao= datetime.date(year=2025, day=12, month=2)
    # )

    # db.add_vaga(
    #     nome_vaga='engenheiro de dados sênior',
    #     descricao_vaga='responsável pela construção de pipelines de dados e integrações. necessário domínio de sql, python, spark e ferramentas de orquestração como airflow.',
    #     nome_empresa='dataflow solutions',
    #     url='www.dataflow.com.br/vagas/engenheiro-senior',
    #     data_publicacao= datetime.date(year=2025, day=12, month=3)
    # )

    # db.add_vaga(
    #     nome_vaga='analista de business intelligence',
    #     descricao_vaga='buscamos um analista de BI para criar dashboards e relatórios. é essencial conhecimento em power bi, sql e modelagem de dados.',
    #     nome_empresa='global analytics',
    #     url='www.globalanalytics.com/jobs/bi-analyst',
    #     data_publicacao= datetime.date(year=2025, day=12, month=5)
    # )

    # db.add_vaga(
    #     nome_vaga='analista de dados jr',
    #     descricao_vaga='vaga para analista de dados jr com foco em marketing digital. necessário excel avançado e noções de python e google analytics.',
    #     nome_empresa='growth lab',
    #     url='www.growthlab.com/vagas/analista-dados',
    #     data_publicacao= datetime.date(year=2025, day=11, month=2)
    # )

    # db.add_vaga(
    #     nome_vaga='engenheiro de machine learning',
    #     descricao_vaga='estamos em busca de um engenheiro de machine learning para desenvolver modelos preditivos e sistemas de recomendação. é preciso dominar python, sklearn e mlops.',
    #     nome_empresa='future ai',
    #     url='www.futureai.com/carreiras/ml-engineer',
    #     data_publicacao= datetime.date(year=2025, day=22, month=2)
    # )



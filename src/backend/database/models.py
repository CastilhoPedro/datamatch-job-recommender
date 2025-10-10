from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Vocabulario(Base):
    __tablename__ = 'vocabulario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    palavra = Column(Text, nullable=False, unique=True)

class Localizacao(Base):
    __tablename__ = 'localizacao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(String(2), unique=True, nullable=False)

class Senioridade(Base):
    __tablename__ = 'senioridade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nivel = Column(String(15), unique=True, nullable=False)

class Vetores(Base):
    __tablename__ = 'vetores'
    id_vaga = Column(Integer, ForeignKey('vagas_raw.id_vaga', ondelete='CASCADE'), primary_key=True)
    id_palavra = Column(Integer, ForeignKey('vocabulario.id', ondelete='CASCADE'), primary_key=True)
    score_tfidf = Column(Float, nullable=False)

    
    vaga = relationship("VagasRaw")
    vocabulario = relationship("Vocabulario")

class RelsRaw(Base):
    __tablename__ = 'vagas_raw'
    id_vaga = Column(Integer, primary_key=True)
    nome_vaga = Column(String(70), nullable=False)
    descricao_vaga = Column(Text, nullable=False)
    nome_empresa = Column(String(50))
    localizacao = Column(String(2)) #aqui ele ainda vai trazer a UF, na processed que vamos transformar a UF em número para deixar mais barato computacionalmente.
    data_publicacao = Column(String(15)) 
    processado = Column(Boolean, default=False)
    url = Column(Text, unique=True, nullable=False)
    data_coleta = Column(DateTime(timezone=True), default=datetime.datetime.now)

class VagasProcessed(Base):
    __tablename__ = 'vagas_processed'
    id_vaga = Column(Integer, ForeignKey('vagas_raw.id_vaga'), primary_key=True)
    nome_vaga = Column(String(70), nullable=False)
    nome_empresa = Column(String(50))
    senioridade = Column(Integer, ForeignKey('senioridade.id'))
    localizacao = Column(Integer, ForeignKey('localizacao.id'))
    data_publicacao = Column(DateTime(timezone=True))
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()

class Vocabulario(Base):
    __tablename__ = 'vocabulario'
    id = Column(Integer, primary_key=True, autoincrement='auto') 
    palavra = Column(Text, nullable=False, unique=True)

class Localizacao(Base): # terá valores fixos adicionados automaticamente (as UFs: SP, RJ, BA)
    __tablename__ = 'localizacao'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uf = Column(String(2), unique=True, nullable=False)

class Senioridade(Base): #terá valores fixos adicionados automaticamente (jr, pl, sr)
    __tablename__ = 'senioridade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nivel = Column(String(15), unique=True, nullable=False)

class Vetores(Base):
    __tablename__ = 'vetores'
    id_vaga = Column(Integer, ForeignKey('vagas.id_vaga', ondelete='CASCADE'), primary_key=True)
    id_palavra = Column(Integer, ForeignKey('vocabulario.id', ondelete='CASCADE'), primary_key=True)
    score_tfidf = Column(Float, nullable=False)

    
    vaga = relationship("Vagas")
    vocabulario = relationship("Vocabulario")

class Vagas(Base):
    __tablename__ = 'vagas'
    id_vaga = Column(Integer, primary_key=True, autoincrement='auto')
    nome_vaga = Column(String(70), nullable=False)
    descricao_vaga = Column(Text, nullable=False)
    nome_empresa = Column(String(50), nullable=False)
    localizacao = Column(String(2), default= None, nullable= True) 
    data_publicacao = Column(DateTime(timezone=True), nullable=False)   
    processado = Column(Boolean, default=False)
    url = Column(Text, unique=True, nullable=False)
    data_coleta = Column(DateTime(timezone=True), default=datetime.datetime.now)
    senioridade = Column(Integer, ForeignKey('senioridade.id'), default= None, nullable= True)
    id_localizacao = Column(Integer, ForeignKey('localizacao.id'), default= None, nullable= True)
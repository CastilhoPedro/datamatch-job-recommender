# Em models.py
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import JSONB
import datetime

Base = declarative_base()

class Vocabulario(Base):
    __tablename__ = 'vocabulario'
    id_palavra = Column(Integer, primary_key=True)
    palavra = Column(Text, nullable=False, unique=True)

class Vaga(Base):
    __tablename__ = 'vagas'
    id_vaga = Column(Integer, primary_key=True)
    portal = Column(Text, nullable=False)
    url = Column(Text, unique=True, nullable=False)
    descricao = Column(Text)
    data_coleta = Column(DateTime(timezone=True), default=datetime.datetime.now)

class Vetores(Base):
    __tablename__ = 'vetores'
    id_vaga = Column(Integer, ForeignKey('vagas.id_vaga', ondelete='CASCADE'), primary_key=True)
    id_palavra = Column(Integer, ForeignKey('vocabulario.id_palavra', ondelete='CASCADE'), primary_key=True)
    score_tfidf = Column(Float, nullable=False)

    # Relacionamentos (opcional, mas bom para ORM)
    vaga = relationship("Vaga")
    vocabulario = relationship("Vocabulario")
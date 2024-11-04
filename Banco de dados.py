from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dataclasses import dataclass


BD = create_engine("sqlite:///Sorveteriadorique.bd")

Session = sessionmaker(bind=BD)
session = Session()

Base = declarative_base()

@dataclass
class Usuario(Base):
    __tablename__ = "usuarios"

    cpf = Column(String,primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    senha = Column(String)

@dataclass
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    valor = Column(Float)

@dataclass
class Venda(Base):
    __tablename__ = "vendas"
    
    nome_comprador = Column(String)
    data_de_compra = Column(DateTime)
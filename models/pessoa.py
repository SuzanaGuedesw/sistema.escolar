from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from abc import abstractmethod
from sqlalchemy import Column, Integer, String
from .base import Base

class Pessoa(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    _nome = Column("nome", String)
    _idade = Column("idade", Integer)

    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @abstractmethod
    def exibir_detalhes(self):
        pass


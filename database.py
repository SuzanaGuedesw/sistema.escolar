from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

banco = create_engine('sqlite:///sistema.db')
Seccao = sessionmaker(bind=banco)
secao = Seccao()

def criar_banco():
    Base.metadata.create_all(banco)
from sqlalchemy import Column, Integer, String
from .base import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    contador_cursos = 0

    def __init__(self, nome: str):
        self.nome = nome
        Curso.contador_cursos += 1

    def exibir_detalhes(self):
        return f"""
        Curso ID: {self.id}
        Nome: {self.nome}
        """

    @classmethod
    def total_cursos(cls):
        return cls.contador_cursos

    @staticmethod
    def inserir_curso(session):
        try:
            nome = input("Nome do curso: ")
            curso = Curso(nome)
            session.add(curso)
            session.commit()
            print("Curso inserido com sucesso!")
        except Exception as e:
            print("Erro ao inserir curso:", e)
            session.rollback()

    @staticmethod
    def listar_cursos(session):
        cursos = session.query(Curso).all()
        if not cursos:
            print("Nenhum curso cadastrado.")
            return
        for c in cursos:
            print(c.exibir_detalhes())

    @staticmethod
    def atualizar_curso(session):
        Curso.listar_cursos(session)
        try:
            curso_id = int(input("ID do curso a ser atualizado: "))
            curso = session.query(Curso).filter_by(id=curso_id).first()
            if not curso:
                print("Curso não encontrado.")
                return
            
            novo_nome = input(f"Nome atual ({curso.nome}): ") or curso.nome
            curso.nome = novo_nome
            session.commit()
            print("Curso atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar curso:", e)
            session.rollback()

    @staticmethod
    def excluir_curso(session):
        Curso.listar_cursos(session)
        try:
            curso_id = int(input("ID do curso a ser excluído: "))
            curso = session.query(Curso).filter_by(id=curso_id).first()
            if not curso:
                print("Curso não encontrado.")
                return
            
            session.delete(curso)
            session.commit()
            print("Curso excluído com sucesso!")
        except Exception as e:
            print("Erro ao excluir curso:", e)
            session.rollback()

    @staticmethod
    def listar_disciplinas_do_curso(session):
        from .disciplina import Disciplina
        Curso.listar_cursos(session)
        curso_id = int(input("ID do curso para listar disciplinas: "))
        curso = session.query(Curso).filter_by(id=curso_id).first()
        
        if not curso:
            print("Curso não encontrado.")
            return
            
        print(f"\nDisciplinas do curso {curso.nome}:")
        disciplinas = session.query(Disciplina).filter_by(curso_id=curso.id).all()
        
        if not disciplinas:
            print("Nenhuma disciplina cadastrada para este curso.")
            return
            
        for disciplina in disciplinas:
            print(disciplina.exibir_detalhes()) 
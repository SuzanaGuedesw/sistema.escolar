from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .aluno import Aluno
from .disciplina import Disciplina

class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))

    aluno = relationship("Aluno", backref="matriculas")
    disciplina = relationship("Disciplina", backref="matriculas")

    def __init__(self, aluno, disciplina):
        self.aluno = aluno
        self.disciplina = disciplina

    def exibir_detalhes(self):
        return f"""
        Matrícula ID: {self.id}
        Aluno: {self.aluno.nome} (ID: {self.aluno.id})
        Disciplina: {self.disciplina.nome} (ID: {self.disciplina.id})
        Curso: {self.disciplina.curso.nome}
        """

    @staticmethod
    def matricular_aluno(session):
        try:
            Aluno.listar_alunos(session)
            aluno_id = int(input("ID do aluno para matricular: "))
            aluno = session.query(Aluno).filter_by(id=aluno_id).first()
            if not aluno:
                print("Aluno não encontrado.")
                return
            Disciplina.listar_disciplinas(session)
            disciplina_id = int(input("ID da disciplina para matricular: "))
            disciplina = session.query(Disciplina).filter_by(id=disciplina_id).first()
            if not disciplina:
                print("Disciplina não encontrada.")
                return
            matricula = Matricula(aluno, disciplina)
            session.add(matricula)
            session.commit()
            print(f"Aluno {aluno.nome} matriculado na disciplina {disciplina.nome} com sucesso!")
        except ValueError:
            print("IDs devem ser números inteiros.")
        except Exception as e:
            print("Erro na matrícula:", e)
            session.rollback()

    @staticmethod
    def listar_matriculas(session):
        matriculas = session.query(Matricula).all()
        if not matriculas:
            print("Nenhuma matrícula cadastrada.")
            return
        for m in matriculas:
            print(m.exibir_detalhes())

    @staticmethod
    def cancelar_matricula(session):
        Matricula.listar_matriculas(session)
        try:
            matricula_id = int(input("ID da matrícula a ser cancelada: "))
            matricula = session.query(Matricula).filter_by(id=matricula_id).first()
            if not matricula:
                print("Matrícula não encontrada.")
                return
            
            session.delete(matricula)
            session.commit()
            print("Matrícula cancelada com sucesso!")
        except Exception as e:
            print("Erro ao cancelar matrícula:", e)
            session.rollback()

    @staticmethod
    def listar_matriculas_por_aluno(session):
        Aluno.listar_alunos(session)
        aluno_id = int(input("ID do aluno para listar matrículas: "))
        aluno = session.query(Aluno).filter_by(id=aluno_id).first()
        
        if not aluno:
            print("Aluno não encontrado.")
            return
            
        print(f"\nMatrículas do aluno {aluno.nome}:")
        matriculas = session.query(Matricula).filter_by(aluno_id=aluno.id).all()
        
        if not matriculas:
            print("Nenhuma matrícula encontrada para este aluno.")
            return
            
        for matricula in matriculas:
            print(matricula.exibir_detalhes())

    @staticmethod
    def listar_matriculas_por_disciplina(session):
        Disciplina.listar_disciplinas(session)
        disciplina_id = int(input("ID da disciplina para listar matrículas: "))
        disciplina = session.query(Disciplina).filter_by(id=disciplina_id).first()
        
        if not disciplina:
            print("Disciplina não encontrada.")
            return
            
        print(f"\nMatrículas na disciplina {disciplina.nome}:")
        matriculas = session.query(Matricula).filter_by(disciplina_id=disciplina.id).all()
        
        if not matriculas:
            print("Nenhuma matrícula encontrada para esta disciplina.")
            return
            
        for matricula in matriculas:
            print(matricula.exibir_detalhes())
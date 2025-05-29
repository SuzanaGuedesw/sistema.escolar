from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .curso import Curso

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)

    curso = relationship("Curso", backref="disciplinas")

    def __init__(self, nome: str, curso: Curso):
        if not isinstance(curso, Curso):
            raise ValueError("Curso must be a valid Curso object")
        self.nome = nome
        self.curso = curso

    def exibir_detalhes(self):
        return f"""
        Disciplina ID: {self.id}
        Nome: {self.nome}
        Curso: {self.curso.nome if self.curso else 'Nenhum curso associado'}
        """

    @staticmethod
    def inserir_disciplina(session):
        try:
            nome = input("Nome da disciplina: ").strip()
            if not nome:
                print("Nome da disciplina não pode ser vazio.")
                return

            Curso.listar_cursos(session)
            curso_id = int(input("ID do curso ao qual a disciplina pertence: "))
            curso = session.query(Curso).filter_by(id=curso_id).first()
            
            if not curso:
                print("Curso não encontrado.")
                return
                
            if session.query(Disciplina).filter_by(nome=nome).first():
                print("Já existe uma disciplina com este nome.")
                return

            disciplina = Disciplina(nome, curso)
            session.add(disciplina)
            session.commit()
            print("Disciplina inserida com sucesso!")
        except ValueError:
            print("ID do curso deve ser número inteiro.")
        except Exception as e:
            print("Erro ao inserir disciplina:", e)
            session.rollback()

    @staticmethod
    def listar_disciplinas(session):
        disciplinas = session.query(Disciplina).all()
        if not disciplinas:
            print("Nenhuma disciplina cadastrada.")
            return
        for d in disciplinas:
            print(d.exibir_detalhes())

    @staticmethod
    def atualizar_disciplina(session):
        Disciplina.listar_disciplinas(session)
        try:
            disciplina_id = int(input("ID da disciplina a ser atualizada: "))
            disciplina = session.query(Disciplina).filter_by(id=disciplina_id).first()
            if not disciplina:
                print("Disciplina não encontrada.")
                return
            
            print("\nDeixe em branco para manter o valor atual.")
            nome = input(f"Nome atual ({disciplina.nome}): ").strip() or disciplina.nome
            
            # Verificar se o novo nome já existe (exceto para a própria disciplina)
            if nome != disciplina.nome and session.query(Disciplina).filter_by(nome=nome).first():
                print("Já existe uma disciplina com este nome.")
                return
            
            # Atualizar curso se necessário
            print(f"Curso atual: {disciplina.curso.nome} (ID: {disciplina.curso.id})")
            mudar_curso = input("Deseja mudar o curso? (s/n): ").lower() == 's'
            curso = disciplina.curso
            
            if mudar_curso:
                Curso.listar_cursos(session)
                curso_id = int(input("Novo ID do curso: "))
                curso = session.query(Curso).filter_by(id=curso_id).first()
                if not curso:
                    print("Curso não encontrado. Mantendo o atual.")
                    curso = disciplina.curso
            
            disciplina.nome = nome
            disciplina.curso = curso
            session.commit()
            print("Disciplina atualizada com sucesso!")
        except ValueError:
            print("IDs devem ser números inteiros.")
        except Exception as e:
            print("Erro ao atualizar disciplina:", e)
            session.rollback()

    @staticmethod
    def excluir_disciplina(session):
        Disciplina.listar_disciplinas(session)
        try:
            disciplina_id = int(input("ID da disciplina a ser excluída: "))
            disciplina = session.query(Disciplina).filter_by(id=disciplina_id).first()
            if not disciplina:
                print("Disciplina não encontrada.")
                return
            
            confirmacao = input(f"Tem certeza que deseja excluir a disciplina '{disciplina.nome}'? (s/n): ").lower()
            if confirmacao != 's':
                print("Operação cancelada.")
                return
                
            session.delete(disciplina)
            session.commit()
            print("Disciplina excluída com sucesso!")
        except ValueError:
            print("ID deve ser um número inteiro.")
        except Exception as e:
            print("Erro ao excluir disciplina:", e)
            session.rollback()

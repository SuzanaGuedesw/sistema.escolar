from sqlalchemy import Column, Integer
from .pessoa import Pessoa

class Aluno(Pessoa):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)    
    matricula = Column(Integer, unique=True)
    contador_alunos = 0

    def __init__(self, nome: str, idade: int, matricula: int):
        super().__init__(nome, idade)
        self.matricula = matricula
        Aluno.contador_alunos += 1

    def exibir_detalhes(self):
        return f"""
        Aluno ID: {self.id}
        Nome: {self.nome}
        Idade: {self.idade}
        Matrícula: {self.matricula}
        """

    @classmethod
    def total_alunos(cls):
        return cls.contador_alunos

    @staticmethod
    def inserir_aluno(session):
        try:
            nome = input("Nome do aluno: ")
            idade = int(input("Idade do aluno: "))
            matricula = int(input("Matrícula: "))
            aluno = Aluno(nome, idade, matricula)
            session.add(aluno)
            session.commit()
            print("Aluno inserido com sucesso!")
        except ValueError:
            print("Idade e matrícula devem ser números inteiros.")
        except Exception as e:
            print("Erro ao inserir aluno:", e)
            session.rollback()

    @staticmethod
    def listar_alunos(session):
        alunos = session.query(Aluno).all()
        if not alunos:
            print("Nenhum aluno cadastrado.")
            return
        for a in alunos:
            print(a.exibir_detalhes())

    @staticmethod
    def atualizar_aluno(session):
        Aluno.listar_alunos(session)
        try:
            aluno_id = int(input("ID do aluno a ser atualizado: "))
            aluno = session.query(Aluno).filter_by(id=aluno_id).first()                     #duvida#
            if not aluno:
                print("Aluno não encontrado.")
                return
            
            print("\nDeixe em branco para manter o valor atual.")
            nome = input(f"Nome atual ({aluno.nome}): ") or aluno.nome
            idade = input(f"Idade atual ({aluno.idade}): ")
            idade = int(idade) if idade else aluno.idade
            matricula = input(f"Matrícula atual ({aluno.matricula}): ")
            matricula = int(matricula) if matricula else aluno.matricula             #duvida#
            
            aluno.nome = nome
            aluno.idade = idade
            aluno.matricula = matricula
            session.commit()
            print("Aluno atualizado com sucesso!")
        except ValueError:
            print("Idade e matrícula devem ser números inteiros.")
        except Exception as e:
            print("Erro ao atualizar aluno:", e)
            session.rollback()

    @staticmethod
    def excluir_aluno(session):
        Aluno.listar_alunos(session)
        try:
            aluno_id = int(input("ID do aluno a ser excluído: "))
            aluno = session.query(Aluno).filter_by(id=aluno_id).first()
            if not aluno:
                print("Aluno não encontrado.")
                return
            
            session.delete(aluno)
            session.commit()
            print("Aluno excluído com sucesso!")
        except Exception as e:
            print("Erro ao excluir aluno:", e)
            session.rollback()

    @staticmethod
    def listar_alunos_por_curso(session):
        from .matricula import Matricula
        from .disciplina import Disciplina
        
        Disciplina.listar_disciplinas(session)
        disciplina_id = int(input("ID da disciplina para filtrar alunos: "))
        disciplina = session.query(Disciplina).filter_by(id=disciplina_id).first()
        
        if not disciplina:
            print("Disciplina não encontrada.")
            return
            
        print(f"\nAlunos matriculados no curso {disciplina.curso.nome}:")
        matriculas = session.query(Matricula).filter_by(disciplina_id=disciplina.id).all()
        
        if not matriculas:
            print("Nenhum aluno matriculado neste curso.")
            return
            
        for matricula in matriculas:
            print(matricula.aluno.exibir_detalhes())
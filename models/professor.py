from sqlalchemy import Column, Integer, String
from .pessoa import Pessoa

class Professor(Pessoa):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True)
    departamento = Column(String)

    def __init__(self, nome: str, idade: int, departamento: str):
        super().__init__(nome, idade)
        self.departamento = departamento

    def exibir_detalhes(self):
        return f"""
        Professor ID: {self.id}
        Nome: {self.nome}
        Idade: {self.idade}
        Departamento: {self.departamento}
        """

    @staticmethod
    def inserir_professor(session):
        try:
            nome = input("Nome do professor: ")
            idade = int(input("Idade do professor: "))
            departamento = input("Departamento: ")
            professor = Professor(nome, idade, departamento)
            session.add(professor)
            session.commit()
            print("Professor inserido com sucesso!")
        except ValueError:
            print("Idade deve ser número inteiro.")
        except Exception as e:
            print("Erro ao inserir professor:", e)
            session.rollback()

    @staticmethod
    def listar_professores(session):
        professores = session.query(Professor).all()
        if not professores:
            print("Nenhum professor cadastrado.")
            return
        for p in professores:
            print(p.exibir_detalhes())

    @staticmethod
    def atualizar_professor(session):
        Professor.listar_professores(session)
        try:
            professor_id = int(input("ID do professor a ser atualizado: "))
            professor = session.query(Professor).filter_by(id=professor_id).first()
            if not professor:
                print("Professor não encontrado.")
                return
            
            print("\nDeixe em branco para manter o valor atual.")
            nome = input(f"Nome atual ({professor.nome}): ") or professor.nome
            idade = input(f"Idade atual ({professor.idade}): ")
            idade = int(idade) if idade else professor.idade
            departamento = input(f"Departamento atual ({professor.departamento}): ") or professor.departamento
            
            professor.nome = nome
            professor.idade = idade
            professor.departamento = departamento
            session.commit()
            print("Professor atualizado com sucesso!")
        except ValueError:
            print("Idade deve ser número inteiro.")
        except Exception as e:
            print("Erro ao atualizar professor:", e)
            session.rollback()

    @staticmethod
    def excluir_professor(session):
        Professor.listar_professores(session)
        try:
            professor_id = int(input("ID do professor a ser excluído: "))
            professor = session.query(Professor).filter_by(id=professor_id).first()
            if not professor:
                print("Professor não encontrado.")
                return
            
            session.delete(professor)
            session.commit()
            print("Professor excluído com sucesso!")
        except Exception as e:
            print("Erro ao excluir professor:", e)
            session.rollback()
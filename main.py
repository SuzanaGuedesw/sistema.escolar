import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.aluno import Aluno
from models.professor import Professor
from models.curso import Curso
from models.disciplina import Disciplina
from models.matricula import Matricula

engine = create_engine('sqlite:///banco.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def menu():
    while True:
        print("""
        ==== Sistema Acadêmico ====
        1 - Gerenciar Alunos
        2 - Gerenciar Professores
        3 - Gerenciar Cursos
        4 - Gerenciar Disciplinas
        5 - Gerenciar Matrículas
        0 - Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_professores()
        elif opcao == "3":
            menu_cursos()
        elif opcao == "4":
            menu_disciplinas()
        elif opcao == "5":
            menu_matriculas()
        elif opcao == "0":
            print("Saindo...")
            session.close()
            sys.exit()
        else:
            print("Opção inválida, tente novamente.")

def menu_alunos():
    while True:
        print("""
        ==== Gerenciamento de Alunos ====
        1 - Inserir Aluno
        2 - Listar Alunos
        3 - Atualizar Aluno
        4 - Excluir Aluno
        5 - Listar Alunos por Curso
        0 - Voltar
        """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Aluno.inserir_aluno(session)
        elif opcao == "2":
            Aluno.listar_alunos(session)
        elif opcao == "3":
            Aluno.atualizar_aluno(session)
        elif opcao == "4":
            Aluno.excluir_aluno(session)
        elif opcao == "5":
            Aluno.listar_alunos_por_curso(session)
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_professores():
    while True:
        print("""
        ==== Gerenciamento de Professores ====
        1 - Inserir Professor
        2 - Listar Professores
        3 - Atualizar Professor
        4 - Excluir Professor
        0 - Voltar
        """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Professor.inserir_professor(session)
        elif opcao == "2":
            Professor.listar_professores(session)
        elif opcao == "3":
            Professor.atualizar_professor(session)
        elif opcao == "4":
            Professor.excluir_professor(session)
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_cursos():
    while True:
        print("""
        ==== Gerenciamento de Cursos ====
        1 - Inserir Curso
        2 - Listar Cursos
        3 - Atualizar Curso
        4 - Excluir Curso
        5 - Listar Disciplinas do Curso
        0 - Voltar
        """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Curso.inserir_curso(session)
        elif opcao == "2":
            Curso.listar_cursos(session)
        elif opcao == "3":
            Curso.atualizar_curso(session)
        elif opcao == "4":
            Curso.excluir_curso(session)
        elif opcao == "5":
            Curso.listar_disciplinas_do_curso(session)
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_disciplinas():
    while True:
        print("""
        ==== Gerenciamento de Disciplinas ====
        1 - Inserir Disciplina
        2 - Listar Disciplinas
        3 - Atualizar Disciplina
        4 - Excluir Disciplina
        0 - Voltar
        """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Disciplina.inserir_disciplina(session)
        elif opcao == "2":
            Disciplina.listar_disciplinas(session)
        elif opcao == "3":
            Disciplina.atualizar_disciplina(session)
        elif opcao == "4":
            Disciplina.excluir_disciplina(session)
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_matriculas():
    while True:
        print("""
        ==== Gerenciamento de Matrículas ====
        1 - Matricular Aluno
        2 - Listar Todas Matrículas
        3 - Cancelar Matrícula
        4 - Listar Matrículas por Aluno
        5 - Listar Matrículas por Disciplina
        0 - Voltar
        """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Matricula.matricular_aluno(session)
        elif opcao == "2":
            Matricula.listar_matriculas(session)
        elif opcao == "3":
            Matricula.cancelar_matricula(session)
        elif opcao == "4":
            Matricula.listar_matriculas_por_aluno(session)
        elif opcao == "5":
            Matricula.listar_matriculas_por_disciplina(session)
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")
            
if __name__ == "__main__":
    menu()
# sistema.academico-poo
# 🎓 Sistema Acadêmico com Python e SQLAlchemy

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-green)
![License](https://img.shields.io/badge/license-MIT-orange)

Um sistema completo para gerenciamento acadêmico com cadastro de alunos, professores, cursos, disciplinas e matrículas.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git (para clonar o repositório)

## 🛠️ Configuração do Ambiente

### 1. Clonar o repositório
```bash
git clone <URL>
cd sistema-de-gerenciamento-acad-mico
```
2. Criar e ativar ambiente virtual
   
```bash

# Windows
python -m venv venv
venv\Scripts\activate

```
3. Instalar dependências
   
```bash
pip install sqlalchemy

```
4. Como Executar
   
```bash
python main.py


```
## 🗂️ Estrutura do Projeto
   
```bash
sistema-academico/
├── models/
│   ├── __init__.py
│   ├── base.py        # Configuração do banco de dados
│   ├── aluno.py       # Modelo de Aluno
│   ├── professor.py   # Modelo de Professor
│   ├── curso.py       # Modelo de Curso
│   ├── disciplina.py  # Modelo de Disciplina
│   └── matricula.py   # Modelo de Matrícula
├── main.py            # Programa principal
└── README.md          # Este arquivo

```

## ✨ Funcionalidades
✅ Cadastro de Alunos

✅ Cadastro de Professores

✅ Gerenciamento de Cursos

✅ Controle de Disciplinas

✅ Sistema de Matrículas

✅ Relacionamentos entre entidades

✅ Interface por linha de comando

## Integrantes do Grupo
- Ana Carolina Guedes Bueno
- Maria Eduarda Gomes Romera
- Suzana Kelly Guedes Vieira

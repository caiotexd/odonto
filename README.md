🦷 OdontoSys - Sistema de Gestão Odontológica

O OdontoSys é uma aplicação web moderna e responsiva desenvolvida para simplificar e otimizar a gestão de clínicas odontológicas. O sistema oferece suporte a múltiplos utilizadores e clínicas, controlo e listagem de pacientes, histórico de evoluções clínicas por atendimento e autenticação segura de utilizadores.

🛠️ Tecnologias Utilizadas

Back-end: Python 3.11+, Flask (Blueprints, Application Factory Pattern)

Base de Dados: PostgreSQL, Flask-SQLAlchemy (ORM)

Autenticação: Flask-Login, Werkzeug Security (Hashing de Senhas)

Front-end: HTML5, CSS3, JavaScript (AJAX/Fetch API), Bootstrap 5

Gerenciamento de Dependências: pip e ambiente virtual (venv)

📌 Funcionalidades Principais

🔐 Autenticação & Multitenancy:

Registo de clínicas e administradores/dentistas.

Login seguro com redirecionamento automático de utilizadores não autenticados.

Isolamento de dados: cada clínica acede apenas aos seus próprios pacientes e registos.

👥 Gestão de Pacientes:

Listagem paginada com barra de pesquisa dinâmica (busca por nome, CPF ou telefone).

Cadastro e edição completa de pacientes.

Exclusão lógica (soft delete) para preservar o histórico e a integridade da base de dados.

📝 Prontuário e Evolução Clínica:

Registo de evoluções médicas em tempo real via AJAX sem recarregar a página.

Histórico cronológico decrescente detalhando data, hora e o profissional responsável pelo atendimento.

Visualização rápida dos dados de contacto e observações gerais do paciente.

📂 Estrutura do Projeto

```text
odonto/
│
├── app/
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── pacientes/
│   │   │   ├── lista.html
│   │   │   ├── novo.html
│   │   │   └── editar.html
│   │   └── base.html
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
│
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── README.md
```


🚀 Como Executar o Projeto Localmente

Pré-requisitos

Python 3.10 ou superior instalado.

Servidor PostgreSQL ativo.

1. Clonar o Repositório

git clone https://github.com/seu-usuario/odonto.git
cd odonto


2. Criar e Ativar o Ambiente Virtual

No Windows (PowerShell):

python -m venv .venv
.\.venv\Scripts\Activate.ps1


No Linux/Mac:

python3 -m venv .venv
source .venv/bin/activate


3. Instalar Dependências

pip install -r requirements.txt


4. Configurar a Base de Dados

Certifique-se de alterar a URL de conexão com a base de dados no ficheiro app/__init__.py ou definir a variável de ambiente DATABASE_URL:

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost:5432/nome_do_banco'


5. Executar a Aplicação

python run.py


Aceda à aplicação no seu navegador: http://127.0.0.1:5000/

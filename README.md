User API

API REST para cadastro, autenticação e gerenciamento de usuários. Desenvolvida com FastAPI como parte do meu portfólio de back-end.

🔧 Tecnologias

Python 3.12

FastAPI

SQLite (banco de dados)

Pydantic (validação de dados)

Uvicorn (servidor ASGI)


🚀 Funcionalidades

Registro de usuários

Autenticação com login

Listagem de usuários

Consulta de usuário por ID

Atualização de dados

Exclusão de usuários


▶️ Como rodar o projeto localmente

# Clone o repositório
git clone https://github.com/ManoFlorest/user_api.git
cd user_api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
uvicorn main:app --reload

📫 Endpoints principais

Método	Rota	Descrição

POST	/register	Criação de novo usuário
POST	/login	Autenticação de usuário
GET	/users	Lista todos os usuários
GET	/users/{id}	Retorna usuário específico
PUT	/users/{id}	Atualiza dados do usuário
DELETE	/users/{id}	Remove o usuário do sistema


🧪 Testes

Você pode testar os endpoints diretamente acessando a documentação automática gerada pelo FastAPI:

Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc


👤 Autor

Desenvolvido por ManoFlorest

LinkedIn: https://www.linkedin.com/in/gabriel-floresta-405a17350?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

Email: gabrielfloresta01@gmail.com
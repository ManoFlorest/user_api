# 🚀 User API

Uma API de gerenciamento de usuários construída com *FastAPI*. Este projeto é uma base sólida para quem está começando no desenvolvimento back-end com Python, focando em autenticação, criação de usuários e organização em rotas.

---

## 🔧 Funcionalidades

- ✅ Cadastro de novos usuários
- 🔐 Login com autenticação JWT
- 🔑 Criptografia de senhas com bcrypt
- 📬 Validação de e-mails com email-validator
- 🗄️ Integração com banco de dados SQLite
- 🧩 Estrutura modular e organizada com FastAPI

---

## 📂 Estrutura do Projeto

User_api/ ├── app/ │   ├── main.py              # Ponto de entrada da aplicação │   ├── models.py            # Modelos do banco de dados │   ├── schemas.py           # Schemas (validação com Pydantic) │   ├── database.py          # Conexão com o banco de dados │   ├── auth.py              # Lógica de autenticação │   └── routers/ │       └── users.py         # Rotas relacionadas aos usuários ├── .gitignore               # Arquivos e pastas ignoradas pelo Git ├── README.md                # Documentação do projeto ├── requirements.txt         # Dependências do projeto └── venv/                    # Ambiente virtual (não subir para o GitHub)

---

## 📦 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [bcrypt](https://pypi.org/project/bcrypt/)
- [email-validator](https://pypi.org/project/email-validator/)
- [Uvicorn](https://www.uvicorn.org/) – servidor ASGI

---

## ▶️ Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SeuUsuario/User_api.git
cd User_api

2. Criar e ativar o ambiente virtual

python -m venv venv
venv\Scripts\activate   # No Windows

3. Instalar as dependências

pip install -r requirements.txt

4. Rodar o servidor

uvicorn app.main:app --reload

Acesse em: http://127.0.0.1:8000
A documentação interativa estará em: http://127.0.0.1:8000/docs


---

📝 Requisitos

Python 3.11 ou superior



---

🙋‍♂️ Autor

Desenvolvido por Gabriel como parte do seu portfólio back-end.
Fique à vontade para abrir issues ou sugerir melhorias!


---

🛡️ Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
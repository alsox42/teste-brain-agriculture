# Teste Brain Agriculture
## Clone do Sistema

### Faço o clone da aplicação no github
#### git clone https://github.com/alsox42/teste-brain-agriculture.git
## Criar Ambiente Virtual
#### python -m venv venv
## Instalar Dependencias
#### pip install -r requirements.txt
## Popular Banco de dados
#### Crie o banco de dados no Postgres
#### python manage.py migrate
#### python manage.py populate_data
## Testar Aplicação
#### python manage.py runserver

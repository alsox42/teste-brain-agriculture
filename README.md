# Teste Brain Agriculture - Sistema Clone
## Clonagem do Repositório

Para clonar a aplicação do repositório no GitHub, utilize o seguinte comando:

```bash
git clone https://github.com/alsox42/teste-brain-agriculture.git
```

## Configuração do Ambiente Virtual

Para criar um ambiente virtual, execute o seguinte comando:

```bash
python -m venv venv
```

## Instalação das Dependências

Para instalar as dependências necessárias, utilize o comando abaixo:

```bash
pip install -r requirements.txt
```

## Populando o Banco de Dados

Antes de prosseguir, certifique-se de criar o banco de dados no
PostgreSQL. Em seguida, migre as alterações necessárias com o comando:

```bash
python manage.py migrate
```

Após a migração, popule o banco de dados com dados de exemplo, serão
1000 registro para testar a aplicação, execute:

```bash
python manage.py populate_data
```

## Testando a Aplicação

Para iniciar o servidor de desenvolvimento e testar a aplicação localmente, utilize o seguinte comando:

```bash
python manage.py runserver
``` 

Este comando iniciará o servidor localmente, permitindo que você acesse a aplicação em seu navegador.
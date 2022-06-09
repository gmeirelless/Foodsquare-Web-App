# FoodSquare
## Qual o foco desta aplicação?
Com o crescente número de restaurantes nas grandes cidades, tornou-se uma parte indispensável para os restaurantes terem um site onde possam não apenas gerenciar seus negócios, mas também anunciar seus produtos. E o Covid-19 acaba de mostrar o quanto é necessário ter uma presença online mesmo para uma pequena organização.


Mas não é fácil para todos os restaurantes construir e gerenciar seus próprios sites. É aí que o FoodSquare entra em cena.

Ele oferece aos restaurantes uma plataforma para gerenciar seus próprios restaurantes e expor seus produtos. Por outro lado, os amantes da comida têm a oportunidade de procurar itens alimentares de acordo com seu gosto e orçamento em centenas de restaurantes.


## Sobre este repositório:
Este repositório contém o aplicativo web para este sistema implementado no Django-2.2 com o padrão de design Model-View-Template. Este foi um projeto parte de um curso acadêmico. Portanto, algumas das melhores práticas de design de sistema não puderam ser mantidas adequadamente.
  
**Especificação:**
  - Web Framework: Django 2.2
  - Database Server: PostgreSQL 12.3
  
**Como executar:**
 - Clone o [github repo](https://github.com/gmeirelless/Foodsquare-Web-App)
 - Agora você pode executar em [docker containers](https://www.docker.com/) de um [pre-built image on docker hub](https://hub.docker.com/r/subangkar/foodsquare) of deste repositório **ou** crie você mesmo um ambiente python e de banco de dados
    - **Docker**
        - Instale [docker](https://docs.docker.com/engine/install/) e [docker-compose](https://docs.docker.com/compose/install/) no seu sistema (se não estiver instalado)
        - mova para o diretório do projeto e inicie os contêineres do docker usando os seguintes comandos:
        ```shell
        docker-compose build
        docker-compose up
        ```
        - agora navegue no site em http://localhost:8000/

    - Ou, **Configuração do Ambiente Python/Banco de Dados**
        - instalar banco de dados postgres
        - crie um novo banco de dados em seu servidor postgres chamado `foodsquare` com o admnistrador como `postgres`, senha como `postgres`
        - inicie o servidor postgres na porta 5432
        - mover para o diretório do projeto
        - crie um ambiente virtual e ative-o
        ```shell
        python3 -m pip install --upgrade pip
        python3 -m venv venv
        source venv/bin/activate
        ```
        - instalar dependências e fazer migrações
        ```shell
        python3 -m pip install -r requirements.txt
        python3 manage.py makemigrations
        python3 manage.py migrate
        ```
        - por fim execute o servidor
        ```shell
        python3 manage.py runserver
        ```
        - agora navegue no site em http://localhost:8000/
        - um aplicativo de login do Facebook precisa ser configurado e suas credenciais devem ser adicionadas ao banco de dados corretamente para acessar as páginas de login.
           Para facilitar, um aplicativo é criado e suas credenciais são fornecidas em um arquivo json despejado que pode ser carregado no banco de dados usando:
        ```shell
        python3 manage.py loaddata data.json
        ``      
         


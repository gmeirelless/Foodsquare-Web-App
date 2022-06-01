# FoodSquare
## Quais problemas essa aplicação resolve?
Com o crescente número de restaurantes nas grandes cidades, tornou-se uma parte indispensável para os restaurantes terem um site onde possam não apenas gerenciar seus negócios, mas também anunciar seus produtos. E o Covid-19 acaba de mostrar o quanto é necessário ter uma presença online mesmo para uma pequena organização.


Mas não é fácil para todos os restaurantes construir e gerenciar seus próprios sites. É aí que o FoodSquare entra em cena.

Ele oferece aos restaurantes uma plataforma para gerenciar seus próprios restaurantes e expor seus produtos. Por outro lado, os amantes da comida têm a oportunidade de procurar itens alimentares de acordo com seu gosto e orçamento em centenas de restaurantes.


## About This Repository:
This repo contains the web app for this system implemented in Django-2.2 with Model-View-Template design pattern. This was an Information System Design project, part of an academic course of CSE, BUET. So some of the best practices of system design could not be maintained properly.
  
**Spec:**
  - Web Framework: Django 2.2
  - Database Server: PostgreSQL 12.3
  
**How to run:**
 - Clone the [github repo](https://github.com/Subangkar/Foodsquare-Web-App)
 - Now you can either run in [docker containers](https://www.docker.com/) of a [pre-built image on docker hub](https://hub.docker.com/r/subangkar/foodsquare) of this repo **or** create an python & database environment yourself
    - **Docker**
        - install [docker](https://docs.docker.com/engine/install/) & [docker-compose](https://docs.docker.com/compose/install/) on your system (if not installed)
        - move to the project directory & start the docker containers using the following commands
        ```shell
        docker-compose build
        docker-compose up
        ```
        - now browse the site at http://localhost:8000/ 
        - **N.B.** Here [remote docker image](https://hub.docker.com/r/subangkar/foodsquare) is used in docker compose. Alternately, you can build a new docker image using `Dockerfile` & use it in composer.

    - Or, **Python Environment/Database setup**
        - install postgres database
        - create a new database in your postgres server named `foodsquare` with owner as `postgres`, password as  `postgres`   
        - start the postgres server on port 5432 
        - move to the project directory 
        - create a virtual environment & activate it
        ```shell
        python3 -m pip install --upgrade pip
        python3 -m venv venv
        source venv/bin/activate
        ```
        - install dependencies & make migrations
        ```shell
        python3 -m pip install -r requirements.txt
        python3 manage.py makemigrations
        python3 manage.py migrate
        ```
        - now run the server finally
        ```shell
        python3 manage.py runserver
        ```
        - now browse the site at http://localhost:8000/ 
        - **N.B.** a facebook login app needs to be set up & its credentials are to be addded into database properly to access login pages.  
          For ease, an app is created & its credentials are provided into a dumped json file which can be loaded into the database using:
        ```shell
        python3 manage.py loaddata data.json
        ```
 - **N.B.** Facebook/Google login may not work properly as those login apps credentials might be outdated now.          
          
          
**Some Basic Functionalities Implemented:**
- User Session Handling
- Third Party Authentication
- Sub-domain Handling
- Shopping Cart Management
- Local Storage Handling
- Online Payment Handling
- Review-Rating Management

Docker Hub Repo: https://hub.docker.com/r/subangkar/foodsquare

***

## Sample Usage:
***Homepage*** ![Homepage](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/website_homepage.png?token=AHSCFFTRYRD66DB3CGMUMKK7HAKDY)





***Browse Cuisines***
![Browse Cuisines](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/filter.png?token=AHSCFFUMKSH2Z5K6QVYXGOC7HALZW)

***Payment***

<img src="https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/bkash.png?token=AHSCFFTSZANDZAQZ5BJ6GUC7HAN5G" alt="Payment" width="500" height="400"/>

***Branch Open***
![Branch Open](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/rest_branch_reg.png?token=AHSCFFSFY4IOR3WV7VFXAJ27HALL4)
***Add Items***
![Add Items](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/additem.png?token=AHSCFFQ2SC7HM7GV5FJBBEC7HALMK)



***Manage and Accept Orders***
![Manage and Accept Orders](https://raw.githubusercontent.com/Subangkar/Foodsquare-Web-App/master/Foodsquare_Screenshots/accept_branch.png?token=AHSCFFUV6AGWFLXQIMFCX427HAMPG)




***Please, find the detailed report and manual of this project*** @[FoodSquare-Report](https://github.com/Subangkar/Foodsquare-Web-App/blob/master/FoodSquareReport.pdf)


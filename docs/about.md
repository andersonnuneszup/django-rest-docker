# django-rest-docker
Stack of a django rest framework project in docker

## Objective
* Stack intended to be an architecture of a backend project for creating api's. This project uses Python Django and the Postgresql DBMS. It also uses Docker to facilitate the implementation of the project in the development environment. This stack streamlines the development process allowing the developer to save time setting up the environment, allowing the team to move on to the next steps.

## Prerequisites
- Programming Language: Python :snake:
- Framework: Django :snake:
- SGBD: PostgresSQL :elephant:
- Docker :whale2:

### Python
- Python installation and configuration is required, which can be obtained from the following link: https://www.python.org/downloads/

### Install Docker
- If you do not have the docker installed on your machine, follow the steps contained in the tutorial for that link: https://docs.docker.com/docker-for-windows/install/


## How to use

### Docker Compose Commands

```bash
python -m venv venv
. ./venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
docker-compose build
docker-compose up  
```
- Break the execution with Ctrl+c and run this commands
```bash
docker-compose run djangostack python manage.py migrate
docker-compose up 
```

### Access the interface
```bash
http://localhost:8000/

## Routs
 Rout                      |     HTTP (Verb)   |      Description      | 
-------------------------  | ----------------- | --------------------- | 
/about                     |       GET         | Sample of api method  | 



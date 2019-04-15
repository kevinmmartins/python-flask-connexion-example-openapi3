# Basic project with Flask , Connexion and OpenApi 3

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d768904f2be345dfa475ae58b8d8fd99)](https://app.codacy.com/app/kevinmmartins/python-flask-swagger-basic?utm_source=github.com&utm_medium=referral&utm_content=kevinmmartins/python-flask-swagger-basic&utm_campaign=Badge_Grade_Dashboard)

[![Build Status](https://travis-ci.org/kevinmmartins/python-flask-connexion-example.svg?branch=master)](https://travis-ci.org/kevinmmartins/python-flask-connexion-example)

Basic Python project using Flask and Connexion by Zalando

```http
https://github.com/zalando/connexion
```

## Requirements

* Docker Compose 1.21.2+
* Python 3.6 +

## Run with Docker Compose

```bash
# building the container
sudo docker-compose build

# starting up a container
sudo docker-compose up
```

## Build the virtual environment

```bash
virtualenv -p /usr/bin/python3.6 venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r test-requirements.txt
```

## Swagger definition:

```http
http://localhost:8081/v1/swagger.json
```

## Health Check

```http
http://localhost:8081/v1/basic/ping
```

## Launch tests:

```bash
source venv/bin/activate
tox
```

# Basic project with Flask, Connexion and OpenApi 3

[![Build Status](https://travis-ci.org/kevinmmartins/python-flask-connexion-example-openapi3.svg?branch=master)](https://travis-ci.org/kevinmmartins/python-flask-connexion-example-openapi3)

Basic Python project using Connexion and Flask

```http
https://github.com/spec-first/connexion
```

## Requirements

* Docker Compose 1.21.2+
* Python 3.9 +

## Run with Docker Compose

```bash
# building the container
sudo docker-compose build

# starting up a container
sudo docker-compose up
```

## Build the virtual environment

```bash
pip3 install virtualenv
virtualenv -p python3.9 venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r test-requirements.txt
```

## Launch the server

```bash
python3 -m basic
```

You should see output similar to this:

```bash
`ConnexionMiddleware.run` is optimized for development. For production, run using a dedicated ASGI server.
INFO:     Started server process [5753]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8081 (Press CTRL+C to quit)
```

## Swagger definition

View the generated Swagger UI at this URL:

```http
http://localhost:8081/v1/basic/ui/
```

## Health Check

Check the server health at this URL:

```http
http://localhost:8081/v1/basic/ping
```

## Launch tests

```bash
source venv/bin/activate
pip3 install tox
tox
```

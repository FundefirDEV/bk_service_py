#!/bin/bash

COMMAND=$1

export COMPOSE_FILE=local.yml
echo $COMMAND 
docker-compose run --rm django python manage.py $COMMAND 
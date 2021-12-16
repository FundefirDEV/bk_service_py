#!/bin/bash

COMMAND=$1
NAME=$2

export COMPOSE_FILE=local.yml
echo $COMMAND 
docker-compose run --rm django python manage.py $COMMAND $NAME
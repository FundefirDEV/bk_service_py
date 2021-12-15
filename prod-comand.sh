#!/bin/bash

COMMAND=$1

export COMPOSE_FILE=production.yml

case $COMMAND in
  "run-env")
    echo "runing env..."
    docker-compose up
    ;;
  "down-containers")
    echo "downing containers..."
    docker-compose down
    ;;
  "build-containers")
    echo "build containers..."
    docker-compose build
    ;;
  "test")
    echo "runing test..."
    docker-compose run --rm django pytest
    ;;
  *)

    echo "command no found:"
    echo ""
    echo "The available commands:"
    echo ""

    echo -e "- run-env"
    echo -e "- run-django"
    echo -e "- down-containers"
    echo -e "- build-containers"
    echo -e "- test"

esac


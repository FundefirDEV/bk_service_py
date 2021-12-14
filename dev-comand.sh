#!/bin/bash

COMMAND=$1

export COMPOSE_FILE=local.yml

case $COMMAND in
  "loaddata")
    # echo "load data from circle.json and create super user... "
    # docker-compose run --rm django python manage.py loaddata bk_service/circles/fixtures/circles.json
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'admin1234')" | docker-compose run --rm django python manage.py shell
    ;;
  "clear-db")
    echo "cleaning db..."
    docker-compose down
    echo 'database deleted: '
    docker volume rm bk_service_py_local_postgres_data
    ;;
  "run-django")
    echo "runing django..."
    docker rm -f bk_service_py_django_1
    docker-compose run --rm --service-ports django
    ;;
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
  *)

    echo "command no found:"
    echo ""
    echo "The available commands:"
    echo ""

    echo -e "- loaddata"
    echo -e "- run-env"
    echo -e "- clear-db"
    echo -e "- run-django"
    echo -e "- down-containers"
    echo -e "- build-containers"
    
esac


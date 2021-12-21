#!/bin/bash

COMMAND=$1
ARGS=$2

export COMPOSE_FILE=local.yml

delete_migrations(){
  local app=$1

  sudo find ./bk_service/$app/migrations/* -delete
  sudo touch ./bk_service/$app/migrations/__init__.py
}


case $COMMAND in
  "loaddata")
    echo "runing django makemigrations..."
    docker-compose run --rm django python manage.py makemigrations 
    echo "runing django migrate..."
    docker-compose run --rm django python manage.py migrate 
    echo "load data from location.json and create super user... "
    docker-compose run --rm django python manage.py loaddata bk_service/locations/fixtures/locations.json  
    docker-compose run --rm django python manage.py loaddata bk_service/users/fixtures/users.json
    echo "from django.contrib.auth import get_user_model ; User = get_user_model(); User.objects.create_superuser(username='admin' , first_name= 'admin' , last_name= 'admin', email='admin@admin.com', password='admin1234', phone_number='+123456789',city_id = 0, gender='M' , is_verified=True)" | docker-compose run --rm django python manage.py shell 
    ;;
  "clear-db")
    echo "cleaning db..."
    echo "deleting migrations files..."
    delete_migrations "users"
    delete_migrations "banks"
    delete_migrations "locations"
    delete_migrations "requests"

    echo "downing containers..."
    docker-compose down
    echo 'database deleted: '
    docker volume rm -f $(docker volume ls -q)
    echo 're-build containers : '
    docker-compose build
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
  "test")
    echo "runing test..."
    docker-compose run --rm django pytest $ARGS
    ;;
  "makemigrations")
    echo "runing django makemigrations..."
    docker-compose run --rm django python manage.py makemigrations 
    ;;
  "migrate")
    echo "runing django migrate..."
    docker-compose run --rm django python manage.py migrate 
    ;;

  "shell")
    echo "runing django shell..."
    docker-compose run --rm django python manage.py shell_plus
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
    echo -e "- test"
    echo -e "- makemigrations"
    echo -e "- migrate"

esac





#!/bin/bash

COMMAND=$1

ENV="_$COMMAND"

echo "*************************************"
echo $ENV
echo "*************************************"

if [[ $COMMAND == ''  ]]; then
    ENV=''
fi

envdir=.envs/.production

mkdir -m 777 $envdir
cd $envdir
touch -m .django .postgres .caddy

# Set postgres env
echo "POSTGRES_HOST=\${{secrets.POSTGRES_HOST$ENV}}" >> .postgres
echo "POSTGRES_PORT=\${{secrets.POSTGRES_PORT$ENV}}" >> .postgres
echo "POSTGRES_DB=\${{secrets.POSTGRES_DB$ENV}}" >> .postgres
echo "POSTGRES_USER=\${{secrets.POSTGRES_USER$ENV}}" >> .postgres
echo "POSTGRES_PASSWORD=\${{secrets.POSTGRES_PASSWORD$ENV}}" >> .postgres

# Set django env
echo "DJANGO_SETTINGS_MODULE=\${{secrets.DJANGO_SETTINGS_MODULE$ENV}}" >> .django
echo "DJANGO_SECRET_KEY=\${{secrets.DJANGO_SECRET_KEY$ENV}}" >> .django
echo "DJANGO_ADMIN_URL=\${{secrets.DJANGO_ADMIN_URL$ENV}}" >> .django
echo "DJANGO_ALLOWED_HOSTS=\${{secrets.DJANGO_ALLOWED_HOSTS$ENV}}" >> .django
echo "REDIS_URL=\${{secrets.REDIS_URL$ENV}}" >> .django
echo "CELERY_FLOWER_USER=\${{secrets.CELERY_FLOWER_USER$ENV}}" >> .django
echo "CELERY_FLOWER_PASSWORD=\${{secrets.CELERY_FLOWER_PASSWORD$ENV}}" >> .django

# # Set caddy envs
echo "POSTGRES_HOST=\${{secrets.POSTGRES_HOST$ENV}}" >> .caddy
echo "POSTGRES_PORT=\${{secrets.POSTGRES_PORT$ENV}}" >> .caddy
echo "POSTGRES_DB=\${{secrets.POSTGRES_DB$ENV}}" >> .caddy
echo "POSTGRES_USER=\${{secrets.POSTGRES_USER$ENV}}" >> .caddy
echo "POSTGRES_PASSWORD=\${{secrets.POSTGRES_PASSWORD$ENV}}" >> .caddy

cd ..
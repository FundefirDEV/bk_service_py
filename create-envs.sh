#!/bin/bash

COMMAND=$1

ENV="_$COMMAND"

if [[ $COMMAND != ''  ]]; then
    ENV=''
fi

envdir=.envs/.production

mkdir -m 777 $envdir
cd $envdir
touch -m .django .postgres .caddy

# Set postgres env
echo "POSTGRES_HOST$ENV=\${{secrets.POSTGRES_HOST}}" >> .postgres
echo "POSTGRES_PORT$ENV=\${{secrets.POSTGRES_PORT}}" >> .postgres
echo "POSTGRES_DB$ENV=\${{secrets.POSTGRES_DB}}" >> .postgres
echo "POSTGRES_USER$ENV=\${{secrets.POSTGRES_USER}}" >> .postgres
echo "POSTGRES_PASSWORD$ENV=\${{secrets.POSTGRES_PASSWORD}}" >> .postgres

# Set django env
echo "DJANGO_SETTINGS_MODULE$ENV=\${{secrets.DJANGO_SETTINGS_MODULE}}" >> .django
echo "DJANGO_SECRET_KEY$ENV=\${{secrets.DJANGO_SECRET_KEY}}" >> .django
echo "DJANGO_ADMIN_URL$ENV=\${{secrets.DJANGO_ADMIN_URL}}" >> .django
echo "DJANGO_ALLOWED_HOSTS$ENV=\${{secrets.DJANGO_ALLOWED_HOSTS}}" >> .django
echo "REDIS_URL$ENV=\${{secrets.REDIS_URL}}" >> .django
echo "CELERY_FLOWER_USER$ENV=\${{secrets.CELERY_FLOWER_USER}}" >> .django
echo "CELERY_FLOWER_PASSWORD$ENV=\${{secrets.CELERY_FLOWER_PASSWORD}}" >> .django

# # Set caddy envs
echo "POSTGRES_HOST$ENV=\${{secrets.POSTGRES_HOST}}" >> .caddy
echo "POSTGRES_PORT$ENV=\${{secrets.POSTGRES_PORT}}" >> .caddy
echo "POSTGRES_DB$ENV=\${{secrets.POSTGRES_DB}}" >> .caddy
echo "POSTGRES_USER$ENV=\${{secrets.POSTGRES_USER}}" >> .caddy
echo "POSTGRES_PASSWORD$ENV=\${{secrets.POSTGRES_PASSWORD}}" >> .caddy
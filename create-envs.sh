#!/bin/bash

envdir=.envs/.production

mkdir -m 777 .envs/
mkdir -m 777 $envdir
cd $envdir
touch -m .django .postgres .caddy

# Set postgres env
echo "POSTGRES_HOST=\${{secrets.POSTGRES_HOST}}" >> .postgres
echo "POSTGRES_PORT=\${{secrets.POSTGRES_PORT}}" >> .postgres
echo "POSTGRES_DB=\${{secrets.POSTGRES_DB}}" >> .postgres
echo "POSTGRES_USER=\${{secrets.POSTGRES_USER}}" >> .postgres
echo "POSTGRES_PASSWORD=\${{secrets.POSTGRES_PASSWORD}}" >> .postgres

# Set django env
echo "DJANGO_SETTINGS_MODULE=\${{secrets.DJANGO_SETTINGS_MODULE}}" >> .django
echo "DJANGO_SECRET_KEY=\${{secrets.DJANGO_SECRET_KEY}}" >> .django
echo "DJANGO_ADMIN_URL=\${{secrets.DJANGO_ADMIN_URL}}" >> .django
echo "DJANGO_ALLOWED_HOSTS=\${{secrets.DJANGO_ALLOWED_HOSTS}}" >> .django
echo "REDIS_URL=\${{secrets.REDIS_URL}}" >> .django
echo "CELERY_FLOWER_USER=\${{secrets.CELERY_FLOWER_USER}}" >> .django
echo "CELERY_FLOWER_PASSWORD=\${{secrets.CELERY_FLOWER_PASSWORD}}" >> .django

# # Set caddy envs
echo "POSTGRES_HOST=\${{secrets.POSTGRES_HOST}}" >> .caddy
echo "POSTGRES_PORT=\${{secrets.POSTGRES_PORT}}" >> .caddy
echo "POSTGRES_DB=\${{secrets.POSTGRES_DB}}" >> .caddy
echo "POSTGRES_USER=\${{secrets.POSTGRES_USER}}" >> .caddy
echo "POSTGRES_PASSWORD=\${{secrets.POSTGRES_PASSWORD}}" >> .caddy
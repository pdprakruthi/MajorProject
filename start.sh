#!/bin/bash 
python manage.py migrate 
python manage.py collectstatic --noinput 
gunicorn crop_backend.wsgi:application 

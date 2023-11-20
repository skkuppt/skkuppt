#!/bin/bash

if [ -z "$WORKERS" ]; then
  CORES=$(grep -c ^processor /proc/cpuinfo)
  WORKERS=$(( 2 * CORES + 1 ))
fi

python3 manage.py makemigrations
python3 manage.py migrate
exec gunicorn --bind 0.0.0.0:8080 config.wsgi:application
#exec gunicorn --workers $WORKERS --bind 0.0.0.0:8080 config.wsgi:application


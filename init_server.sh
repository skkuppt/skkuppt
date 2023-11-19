#!/bin/bash

cd ./frontend
virtualenv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate # db.sqlite 생성 



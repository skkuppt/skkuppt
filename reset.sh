#!/bin/bash

sudo docker stop skkuppt_backend_1
sudo docker stop skkuppt_frontend_1 
sudo docker rm skkuppt_backend_1
sudo docker rm skkuppt_frontend_1 

sudo docker-compose up -d --build backend
sudo docker-compose up -d --build frontend 


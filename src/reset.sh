#!/bin/bash

sudo docker stop src_backend_1
sudo docker stop src_frontend_1 
sudo docker rm src_backend_1
sudo docker rm src_frontend_1 

sudo docker-compose up -d --build backend
sudo docker-compose up -d --build frontend 


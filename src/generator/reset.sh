#!/bin/bash

sudo docker stop generator_backend_1
sudo docker stop generator_frontend_1 
sudo docker rm generator_backend_1
sudo docker rm generator_frontend_1 

sudo docker-compose up -d --build backend
sudo docker-compose up -d --build frontend 


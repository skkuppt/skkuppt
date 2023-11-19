#!/bin/bash

sudo docker stop backend 
sudo docker stop frontend 
sudo docker rm backend 
sudo docker rm frontend 

sudo docker-compose up -d --build backend
sudo docker-compose up -d --build frontend 



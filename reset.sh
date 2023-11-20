#!/bin/bash

make down service=frontend
make down service=backend

#make pull service=frontend
#make pull service=backend
make build service=frontend
make build service=backend

make up service=frontend
make up service=backend

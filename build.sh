#!/bin/bash

IMAGE_NAME="django-example"

poetry export --without-hashes --format=requirements.txt > requirements.txt

docker build -t $IMAGE_NAME .
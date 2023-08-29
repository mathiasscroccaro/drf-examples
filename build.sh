#!/bin/bash

IMAGE_NAME="django-example"

poetry export --without-hashes --format=requirements.txt > requirements.txt
poetry export --without-hashes --with dev --format=requirements.txt > requirements-dev.txt

docker build -t $IMAGE_NAME .
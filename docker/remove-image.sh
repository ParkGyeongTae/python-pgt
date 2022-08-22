#!/bin/bash

source .env

docker rmi ${PYTHON_IMAGE_NAME}:${PYTHON_IMAGE_VERSION}
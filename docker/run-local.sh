#!/bin/bash

source .env

CONTAINER_NAME=${PYTHON_CONTAINER_NAME}

IMAGE_NAME_TAG=$PYTHON_IMAGE_NAME:$PYTHON_IMAGE_VERSION

if [[ "$(docker images -f "dangling=true" -q 2> /dev/null)" != "" ]]; then
    echo "Remove dangling images"
    docker rmi $(docker images -f "dangling=true" -q)
fi

if [[ "$(docker container ls -q --filter "name=${CONTAINER_NAME}" 2> /dev/null)" != "" ]]; then
    echo "Stop & Remove Container ${CONTAINER_NAME}"
    docker stop $(docker container ls -q --filter "name=${CONTAINER_NAME}")
    docker rm $(docker container ls -q --filter "name=${CONTAINER_NAME}")
fi

docker run -it --rm \
    -v $(pwd)/code:/code \
    -v $(pwd)/result:/result \
    --name ${CONTAINER_NAME} ${IMAGE_NAME_TAG}

# --net=host \
# --pid host \
# -v $(pwd)/../code:/code \
# -v $(pwd)/../script:/script \
# -v $(pwd)/../log:/log \
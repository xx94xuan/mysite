#!/usr/bin/env bash

IMAGE_NAME=${IMAGE_NAME}
DOCKERFILE=${DOCKERFILE}

docker build -f $DOCKERFILE -t $IMAGE_NAME .

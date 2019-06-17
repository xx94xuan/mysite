#!/usr/bin/env bash

BASE_IMAGE=${BASE_IMAGE}
DOCKERFILE=${DOCKERFILE}
FORCE_BUILD=${FORCE_BUILD}

if $FORCE_BUILD == "true"
then
    echo "force build..."
    docker build --no-cache -f $DOCKERFILE -t $BASE_IMAGE .
else
    docker build -f $DOCKERFILE -t $BASE_IMAGE .
fi
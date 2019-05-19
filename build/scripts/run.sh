#!/usr/bin/env bash

TAGGED_IMAGE=${TAGGED_IMAGE}

docker run --rm -p 0.0.0.0:8000:8000 $TAGGED_IMAGE
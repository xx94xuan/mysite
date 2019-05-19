#!/usr/bin/env bash

COMPOSE_PATH=${COMPOSE_PATH}
LOCAL_APP_NAME=${LOCAL_APP_NAME}

docker-compose -p $LOCAL_APP_NAME -f $COMPOSE_PATH build app_base
docker-compose -p $LOCAL_APP_NAME -f $COMPOSE_PATH build app

echo "launching app...."

docker-compose -p $LOCAL_APP_NAME -f $COMPOSE_PATH up app
docker-compose -p $LOCAL_APP_NAME -f $COMPOSE_PATH stop app

echo "done."

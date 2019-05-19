dockerhub_user:=dockerforxxx
docker_host:=0.0.0.0:8000
port:=8000
base_image:=app-base:latest
git_hash=$(shell git rev-parse HEAD)
image_name:=xxx-app:latest
tag?=$(git_hash)
repository:=$(dockerhub_user)/xxx-app
tagged_image:=$(repository):$(tag)
force_build?=false
local_app_name?=app-localhost

build_base:
	BASE_IMAGE=$(base_image) \
	DOCKERFILE=./build/Dockerfile.base \
	sh ./build/scripts/build_base.sh

build_app: build_base
	DOCKERFILE=./build/Dockerfile.app \
	IMAGE_NAME=$(image_name) \
	sh ./build/scripts/build_app.sh

tag:
	IMAGE_NAME=$(image_name) \
	TAGGED_IMAGE=$(tagged_image) \
	sh ./build/scripts/tag.sh
	
push:
	TAG=$(image_name) \
	TAGGED_IMAGE=$(tagged_image) \
	sh ./build/scripts/push.sh

run:
	TAGGED_IMAGE=$(tagged_image) \
	sh ./build/scripts/run.sh

run_development:
	COMPOSE_PATH=build/docker-compose.yml \
	LOCAL_APP_NAME=$(local_app_name) \
	sh ./build/scripts/run_development.sh
	# bind mount a volume - local project
	# docker run -it -p 0.0.0.0:8000:8000 -v $(PWD):/mysite IMAGE_ID bash

push_new_image: build_app tag push
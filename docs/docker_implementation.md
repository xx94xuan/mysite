# Integrate with Docker

## Build the Image

1. Create `Makefile` under the root path of the project - [mysite/Makefile](https://github.com/xx94xuan/mysite/blob/master/Makefile)

    + Setup a target named 'build_app' to build an image of the project, 'build_base'(Install system dependencies) as the prerequisite to build app(project)
    
    + Setup another target named 'run_development' contains commands to run the server locally

2. Create `build_app.sh` and `build_base.sh` on the path defined in 'Makefile',
these files would run docker commands to build images. - [build_app.sh](https://github.com/xx94xuan/mysite/blob/master/build/scripts/build_app.sh) & [build_base.sh](https://github.com/xx94xuan/mysite/blob/master/build/scripts/build_base.sh)

    + `docker build -f ${DockerfilePath} ${IMAGE_NAME}` -- will build an image named 'IMAGE_NAME' with the system that Dockerfile set.

3. Create `Dockerfile.app` to runs certain shell commands to completed building the app - [Dockerfile.base](https://github.com/xx94xuan/mysite/blob/master/build/Dockerfile.base) & [Dockerfile.app](https://github.com/xx94xuan/mysite/blob/master/build/Dockerfile.app). _Here is an offical doc for [dockerfile leaning](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)_

4. Once steps above finished, run `make build_app` and it will build the app, then run `docker images` to show the image just created named as 'IMAGE_NAME'

## Interact with the created image

5. Setup a container with the image by IMAGE_ID or IMAGE_NAME:IMAGE_TAG, use `-it` to interact with the container to run `sh` in container:
    + `docker run -it $IMAGE_ID sh`

    do something in the container by running shell command as usual.

## Tagged the image

6. Tag the image with a TAGGED_NAME - [tag.sh](https://github.com/xx94xuan/mysite/blob/master/build/scripts/tag.sh) *${dockerhub_user}/${ImageName}:${tag}* by running docker command:  

    + `docker tag $IMAGE_NAME $TAGGED_NAME`

## Push the image to dockerhub

7. Push the image to dockerhub, _this operation requests the user and password of dockerhub which were setting while creating dockerhub account_ - [push.sh](https://github.com/xx94xuan/mysite/blob/master/build/scripts/push.sh)

    + `docker push $TAGGED_NAME`

8. visit [dockerhub](https://hub.docker.com/) on browser to see the pushed image


## Set up this project locally
After `make build_app`, run `docker images` to get the latest image and run command: `docker run -it -p 0.0.0.0:8000:8000 IMAGE_ID sh` to interact with the image. Once get into the `sh` mode, run `python manage.py runserver 0.0.0.0:8000` to start the server.visit `localhost:8000/gallery` to test if the server is running.
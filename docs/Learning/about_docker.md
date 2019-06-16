Docker

## docker build ...
<<<<<<< Updated upstream

### Dockerfile

> A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image.Using `docker build` users can create an automated build that executes several command-line instructions in succession.

> Note that each instruction is run independently, and causes a new image to be created 

The `docker build` command builds an image from a Dockerfile and a context.
To increase build's performance, adding a `.dockerignore` file to exclude files be built in the image.
+ docker build (-t docker_user/myapp) CONTEXT
+ docker build -f path/to/Dockerfile

> The build is run by the Docker daemon, not by the CLI. The first thing a build process does is send the entire context (recursively) to the daemon. In most cases, it’s best to start with an empty directory as context and keep your Dockerfile in that directory. Add only the files needed for building the Dockerfile.

=======
### docker build DOCKERFILE CONTEXT

>The build is run by the Docker daemon, not by the CLI. The first thing a build process does is send the entire context (recursively) to the daemon. In most cases, it’s best to start with an empty directory as context and keep your Dockerfile in that directory. Add only the files needed for building the Dockerfile.
>>>>>>> Stashed changes

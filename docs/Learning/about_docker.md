# Docker
属于Linux容器的一种封装，提供简单易用的容器接口。
Linux容器：不是模拟一个完整的操作系统，而是对进程进行隔离。
image 文件生成的容器实例，本身也是一个文件，称为容器文件。

## docker build ...

### Dockerfile

> A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image.Using `docker build` users can create an automated build that executes several command-line instructions in succession.

> Note that each instruction is run independently, and causes a new image to be created 

### docker build DOCKERFILE CONTEXT

The `docker build` command builds an image from a Dockerfile and a context.
To increase build's performance, adding a `.dockerignore` file to exclude files be built in the image.
+ docker build (-t docker_user/myapp) CONTEXT
+ docker build -f path/to/Dockerfile

> The build is run by the Docker daemon, not by the CLI. The first thing a build process does is send the entire context (recursively) to the daemon. In most cases, it’s best to start with an empty directory as context and keep your Dockerfile in that directory. Add only the files needed for building the Dockerfile.






## Container

### docker container
```
# show running containers
$ docker container ls

# same as: 
$ docker ps


# show all containers
$ docker container ls -a

#same as:
$ docker ps -a


# filter the dangling containers
$ docker container -f "dangling=true"


# only display the numeric IDs
$ docker container -q


# stop container by contaner id(use "docker ps" to get the container ids)
$ docker container stop CONTANIER_ID


# delete all dangling containers
$ docker container prune
```



## Running a kubernetes cluster by minikube

### create a cluster by minikube
`$ minikube start --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers --cache-images`


```
# check the minikube version
$ minikube version

# create the cluster
# "--image-repository" to fix Unable to pull images error
# "--cache-images" to fix Unable to load cached images error
# referrence: https://github.com/kubernetes/minikube/issues/3860
```

### kubectl: CLI to interact with kubenetes

```
# check if kubectl is installed
$ kubectl verison

# get cluster info
$ kubectl cluster-info

# to view the nodes in the cluster
$ kubectl get nodes
# NAME       STATUS    ROLES     AGE       VERSION
# minikube   Ready     master    37m       v1.14.1

# STATUS Ready means it is ready to accept applications for deployment
```

#### deploy an app
`$ kubectl run k8s-app-deployment --image=IMAGE_NAME:TAG`

```
# get info of the deployment
$ kubectl get deployment
```

#### view nodes and pods
`kubectl get/describe/logs/exec`

```
# show the running pods/nodes/deployments
$ kubectl get pods

# show detailed info of the resources
# pods, nodes, deployments
$ kubectl describe pods

# show all info of the pod use JSON format
$ kubectl get pods -o json

# print logs from a container in a pod
# kubectl logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER] [options]
$ kubectl logs POD_NAME

# execute commands on a container in a pod
# kubectl exec POD [-c CONTAINER] -- COMMAND [args...] [options]
$ kubectl exec POD_NAME -it -- sh

# to view data from apis on browser(port 8001 as default)
$ kubectl proxy
```

#### expose the app publicy by Service
`$ kubectl expose deployment/k8s-app-deployment --type="NodePort" --port 8000`

`curl $(minikube ip):$NODE_PORT`

```
$ kubectl get service

# get service's NodePort:
$ kubectl describe service
# or:
$ export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT

kubectl describe deployment

kubectl get pods -l run=k8s-app-deployment

kubectl get services -l run=k8s-app-deployment

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
```

### label the pods
```
kubectl label pod $POD_NAME app=label-test

kubectl describe pods $POD_NAME

kubectl get pods -l app=label-test

kubectl delete service -l run=k8s-app-deployment


kubectl get services

curl $(minikube ip):$NODE_PORT

kubectl exec -ti $POD_NAME curl localhost:8000

```

### scale the deployment
`kubectl scale DEPLOYMENT --replicas=4`

```
# 4 pods
kubectl scale deployments/k8s-app-deployment --replicas=4

kubectl get pods -o wide

kubectl describe deployment/wip-xxx-app-dep

kubectl describe service

```


### Rolling updates ???
update:
`kubectl set image OLD_DEPLOYMENT CONTAINER_NAME?=NEW_IMAGE_NAME`
OR:
`kubectl rollout status DEPOLYMENT`

rollback:
`kubectl rollout undo DEPLOYMENT`

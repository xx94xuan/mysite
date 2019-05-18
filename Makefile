build:
	docker build . -t app:latest

tag:
	docker tag app:latest dockerforxxx/app:latest

push:
	docker push dockerforxxx/app:latest

run:
	docker run --rm -p 0.0.0.0:8000:8000

run_local: build
	docker run --rm -p 0.0.0.0:8000:8000 app:latest
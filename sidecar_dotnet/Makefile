#!make
include dev.env
export $(shell sed 's/=.*//' dev.env)
export IMAGE_NAME=sidecar_dotnet
export VERSION=latest
export CONTAINER=$(IMAGE_NAME)_container

default: run

build:
	dotnet built
	$(PYTHON) -m pip install -r ./requirements.txt

run:
	dotnet run

publish:
	dotnet publish -c Release

buildc:
	docker build --tag $(IMAGE_NAME):${VERSION} . -f Dockerfile

stopc:
	-docker rm --force $(CONTAINER)
	-docker rmi --force $(IMAGE_NAME)

runbash:
	docker exec -it ${CONTAINER} /bin/bash

runc:
	docker run --name ${CONTAINER} -p ${SIDECAR_GRPC_PORT}:${SIDECAR_GRPC_PORT} --env-file dev.env  $(IMAGE_NAME):${VERSION}

br: stopc buildc runc


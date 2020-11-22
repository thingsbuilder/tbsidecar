#!make
include dev.env
export $(shell sed 's/=.*//' dev.env)
export WORKER_NAME=worker
export PYTHON=/usr/bin/python3
export IMAGE_NAME=sidecar_python
export VERSION=latest
export CONTAINER=$(IMAGE_NAME)_container

default: run

build:
	$(PYTHON) -m pip install -r ./requirements.txt

run:
	$(PYTHON)  ./run.py

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

upload-pip:
	# https://dzone.com/articles/executable-package-pip-install
	python setup.py bdist_wheel
	python -m twine upload dist/*

pip-upload:
	cd dist && twistd -n web  --path .

install-local:
	pip install -e .

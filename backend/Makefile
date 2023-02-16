SHELL := /bin/bash

include .config
export
include ../.env
export

run-local:
	python server.py

test:
	curl -i -H "Content-Type: application/json" -X POST -d '{"text":"some text"}' http://localhost:5004/

test-get:
	curl -i -X GET http://localhost:5004/

build:
	docker build -t ${IMG_NAME} .

run-container:
	docker events & docker run --network="host" --env-file .config -e OPENAI_API_KEY=${OPENAI_API_KEY} --publish ${PORT_MAP} -d ${IMG_NAME}

kill:
	docker container kill $(docker container ls -q)
include .config
export
include ../.env
export

KAFKA_VERSION = 2.12
KAFKA_RELEASE = 3.3.2
IMG_NAME = kafka
KAFKA_FILE = ${IMG_NAME}_${KAFKA_VERSION}-${KAFKA_RELEASE}
QUESTION_TOPIC = questions
ANSWER_TOPIC = answers

build-image:
	docker build -t ${IMG_NAME} .

run-container:
	docker events & docker run --network="host" --env-file .config -e OPENAI_API_KEY=${OPENAI_API_KEY} -d ${IMG_NAME}

run-local:
	python rmq_get.py

read-question:
	cd ./downloads/${KAFKA_FILE} ; \
	bin/kafka-console-producer.sh --topic ${QUESTION_TOPIC} --bootstrap-server localhost:9092

write-answer:
	cd ./downloads/${KAFKA_FILE}; \
	bin/kafka-console-consumer.sh --topic ${ANSWER_TOPIC} --from-beginning --bootstrap-server localhost:9092 
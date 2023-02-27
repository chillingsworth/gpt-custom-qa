FROM ubuntu:18.04
FROM python:3.9.15

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD . /app

ENTRYPOINT [ "python" ]

CMD ["kafka_get.py" ]
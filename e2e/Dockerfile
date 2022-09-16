FROM python:3.9

COPY . /python-test
WORKDIR /python-test

RUN apt-get update && apt-get install -y
RUN pip install -r requirements.txt
RUN pytest -sv

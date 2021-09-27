FROM python:3.9

WORKDIR /app

RUN pip install git+https://github.com/stevegbrooks/jqdatasdk.git@steve/waffle-wrap


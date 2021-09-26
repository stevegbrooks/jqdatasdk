FROM python:3.9

WORKDIR /app

RUN pip install git+https://github.com/stevegbrooks/jqdatasdk@waffle-wrap.git

RUN mkdir /app/work
COPY work/ /app/


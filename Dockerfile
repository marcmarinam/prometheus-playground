FROM python:3.12-slim

WORKDIR /usr/src/app

COPY ./.python-version ./
COPY ./uv.lock ./
COPY ./pyproject.toml ./

RUN pip install uv

RUN uv sync

COPY ./src ./src
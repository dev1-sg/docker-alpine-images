# syntax=docker.io/docker/dockerfile:1

FROM docker.io/python:3.13.3-bookworm AS base

USER root

ARG POETRY_VERSION=2.1.3

ENV TZ=Asia/Singapore \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VENV="/opt/poetry/venv" \
    POETRY_CACHE_DIR="/opt/poetry/cache" \
    POETRY_CONFIG_DIR="/opt/poetry/config" \
    POETRY_DATA_DIR="/opt/poetry/data"

ENV PATH="${POETRY_HOME}/bin:${PATH}"

WORKDIR /app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates locales-all \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry

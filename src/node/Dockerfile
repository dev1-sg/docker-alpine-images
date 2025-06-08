# syntax=docker.io/docker/dockerfile:1

FROM docker.io/node:22.16.0-bookworm AS base

USER root

ARG YARN_VERSION=1.22.19
ARG PNPM_VERSION=10.11.0

ENV TZ=Asia/Singapore \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    PNPM_HOME="/opt/pnpm"

ENV PATH="${PNPM_HOME}:${PATH}"

WORKDIR /app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates locales-all \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN corepack enable \
    && corepack prepare pnpm@${PNPM_VERSION} --activate \
    && corepack prepare yarn@${YARN_VERSION} --activate

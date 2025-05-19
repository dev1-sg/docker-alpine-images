# syntax=docker.io/docker/dockerfile:1

FROM docker.io/ubuntu:jammy AS base
FROM docker.io/node:24.0.2-bookworm AS build

FROM base AS final

ARG YARN_VERSION=1.22.19
ARG PNPM_VERSION=10.11.0

ENV TZ=Asia/Singapore \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    PNPM_HOME="/opt/pnpm"

ENV PATH="${PNPM_HOME}:${PATH}"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ca-certificates locales-all

COPY --from=build /usr/local/bin/node /usr/local/bin/node
COPY --from=build /usr/local/lib /usr/local/lib
COPY --from=build /usr/local/include /usr/local/include
COPY --from=build /usr/local/share /usr/local/share

RUN ln -s /usr/local/lib/node_modules/corepack/dist/corepack.js /usr/local/bin/corepack \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs \
    && ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && ln -s /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx

RUN corepack enable \
    && corepack prepare pnpm@${PNPM_VERSION} --activate \
    && corepack prepare yarn@${YARN_VERSION} --activate

WORKDIR /app

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

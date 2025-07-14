# syntax=docker.io/docker/dockerfile:1

FROM docker.io/python:3.13.5-alpine3.21 AS base

USER root

ENV TZ=Asia/Singapore \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    LAMBDA_RUNTIME_DIR=/var/runtime \
    LAMBDA_TASK_ROOT=/var/task \
    VIRTUAL_ENV=/var/task/.venv

ENV PATH="/var/runtime:$VIRTUAL_ENV/bin:${PATH}"

WORKDIR /var/task

RUN apk add --no-cache \
    sudo bash curl ca-certificates jq \
    && rm -rf /var/cache/apk/* \
    && ln -s /var/cache/apk /etc/apk/cache

FROM base AS build

ARG AWSRIE_VERSION=1.26

RUN apk add --no-cache \
    build-base cmake unzip curl-dev autoconf automake libtool elfutils-dev

RUN mkdir -p "${LAMBDA_TASK_ROOT}" "${LAMBDA_RUNTIME_DIR}" \
    && curl -fsSL "https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/download/v${AWSRIE_VERSION}/aws-lambda-rie-$(case $(uname -m) in x86_64) echo x86_64 ;; aarch64) echo arm64 ;; esac)" -o /var/runtime/aws-lambda-rie \
    && chmod +x /var/runtime/aws-lambda-rie \
    && python3 -m venv .venv \
    && source .venv/bin/activate \
    && pip install awslambdaric

FROM base AS final

COPY --from=build /var/runtime/aws-lambda-rie /var/runtime/aws-lambda-rie
COPY --from=build /var/task/.venv /var/task/.venv

ENTRYPOINT [ "/var/runtime/aws-lambda-rie", "python3", "-m", "awslambdaric" ]

CMD [ "handler.lambda_handler" ]

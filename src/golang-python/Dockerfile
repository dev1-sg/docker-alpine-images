# syntax=docker.io/docker/dockerfile:1

FROM docker.io/golang:1.24.5-alpine3.21 AS golang
FROM docker.io/python:3.13.5-alpine3.21 AS python
FROM docker.io/alpine:3.22 AS base

USER root

ENV TZ=Asia/Singapore \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

ENV PATH="/usr/local/go/bin:${PATH}"

RUN apk add --no-cache \
    sudo bash git aws-cli curl ca-certificates jq \
    && rm -rf /var/cache/apk/* \
    && ln -s /var/cache/apk /etc/apk/cache

COPY --from=golang /usr/local/go /usr/local/go
COPY --from=python /usr/local/bin /usr/local/bin
COPY --from=python /usr/local/lib /usr/local/lib

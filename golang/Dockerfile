# syntax=docker.io/docker/dockerfile:1

FROM docker.io/golang:1.23.9-bookworm AS base

USER root

ENV TZ=Asia/Singapore \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    GOPATH="/go" \
    GOTOOLCHAIN="local"

ENV PATH="${GOPATH}/bin:/usr/local/go/bin:${PATH}"

WORKDIR /go

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ca-certificates locales-all \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#!/usr/bin/env bash

version=$(sed -n 's|.*eclipse-temurin:\([0-9.]*\)-jre-alpine-\([0-9.]*\).*|\1-\2|p' Dockerfile)

if [ -n "$version" ]; then
    echo "$version"
else
    echo "latest"
fi

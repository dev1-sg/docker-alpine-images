#!/usr/bin/env bash

version=$(sed -n 's|.*golang:\([0-9.]*\)-alpine\([0-9.]*\).*|\1-\2|p' Dockerfile)

if [ -n "$version" ]; then
    echo "$version"
else
    echo "latest"
fi

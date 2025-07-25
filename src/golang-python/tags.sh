#!/usr/bin/env bash

versions=($(sed -n 's/^FROM .*:\([^ -]*\).*/\1/p' Dockerfile | head -2))

if [[ -n "${versions[0]}" && -n "${versions[1]}" ]]; then
    echo "${versions[0]}-${versions[1]}"
else
    echo "latest"
fi

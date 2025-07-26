#!/usr/bin/env bash

alpine=($(sed -n 's/^FROM .*:\([^ -]*\).*/\1/p' Dockerfile | head -1))
python=($(sed -n 's/^ARG PYTHON_VERSION=\(.*\)/\1/p' Dockerfile | head -1))

if [[ -n "${python}" && -n "${alpine}" ]]; then
    echo "${python}-${alpine}"
else
    echo "latest"
fi

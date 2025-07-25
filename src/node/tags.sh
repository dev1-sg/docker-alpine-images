#!/usr/bin/env bash

alpine=$(sed -n 's|.*node:[0-9.]*-alpine\([0-9.]*\).*|\1|p' Dockerfile)
node=$(sed -n 's|.*node:\([0-9.]*\)-alpine[0-9.]*.*|\1|p' Dockerfile)

if [[ -n "${node}" && -n "${alpine}" ]]; then
    echo "${node}-${alpine}"
else
    echo "latest"
fi

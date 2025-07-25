#!/usr/bin/env bash

alpine=($(sed -n 's|.*golang:[0-9.]*-alpine\([0-9.]*\).*|\1|p' Dockerfile))
golang=($(sed -n 's|.*golang:\([0-9.]*\)-alpine[0-9.]*.*|\1|p' Dockerfile))

if [[ -n "${golang}" && -n "${alpine}" ]]; then
    echo "${golang}-${alpine}"
else
    echo "latest"
fi

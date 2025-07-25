#!/usr/bin/env bash

alpine=($(sed -n 's|.*python:[0-9.]*-alpine\([0-9.]*\).*|\1|p' Dockerfile))
python=($(sed -n 's|.*python:\([0-9.]*\)-alpine[0-9.]*.*|\1|p' Dockerfile))

if [[ -n "${python}" && -n "${alpine}" ]]; then
    echo "${python}-${alpine}"
else
    echo "latest"
fi

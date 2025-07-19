#!/usr/bin/env bash

alpine=$(sed -n 's|.*node:[0-9.]*-alpine\([0-9.]*\).*|\1|p' Dockerfile)
node=$(sed -n 's|.*node:\([0-9.]*\)-alpine[0-9.]*.*|\1|p' Dockerfile)

echo "${node:-dev}-${alpine:-null}"

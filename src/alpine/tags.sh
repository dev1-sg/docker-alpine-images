#!/usr/bin/env bash

alpine=($(sed -n 's/^FROM .*:\([^ -]*\).*/\1/p' Dockerfile | head -1))

echo "${alpine:-latest}"

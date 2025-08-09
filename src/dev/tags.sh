#!/usr/bin/env bash

version=($(sed -n 's/^FROM .*:\([^ -]*\).*/\1/p' Dockerfile | head -1))

echo "${version:-latest}"

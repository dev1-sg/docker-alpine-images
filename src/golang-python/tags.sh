#!/usr/bin/env bash

versions=($(sed -n 's/^FROM .*:\([^ -]*\).*/\1/p' Dockerfile | head -2))

echo "${versions[0]}-${versions[1]}"

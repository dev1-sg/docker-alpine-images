#!/usr/bin/env bash

alpine=($(sed -n 's|.*golang:[0-9.]*-alpine\([0-9.]*\).*|\1|p' Dockerfile))
golang=($(sed -n 's|.*golang:\([0-9.]*\)-alpine[0-9.]*.*|\1|p' Dockerfile))

echo "${golang:-dev}-${alpine:-null}"

#!/usr/bin/env bash

submodules() {
  echo "Updating git submodules..."
  git submodule update --init --recursive
  git config --file .gitmodules --get-regexp path | while read -r key submodule_path; do
    echo "Updating submodule at path: $submodule_path"
    (
      cd "$submodule_path" && git pull origin main
    )
  done
}

env() {
  echo "Exporting .env..."
  cat .env
  export $(grep -v '^#' .env | xargs)
}

venv() {
  echo "Setting up venv..."
  python3 -m venv .venv \
  && source .venv/bin/activate \
  && pip install -r requirements.txt
}

tests() {
  go test ./... -v
}

declare -f "$1" >/dev/null && "$@"

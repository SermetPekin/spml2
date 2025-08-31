#!/bin/bash
set -e  # Exit on error

if [ -z "$1" ]; then
  echo "Usage: ./commit.sh \"Your commit message\""
  exit 1
fi

black .

git add .
git commit -m "$1"
git push

git status

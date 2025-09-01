#!/bin/bash

set -e  # Exit on error

black .
pytest -v

echo "🧹 Removing dist/..."
rm -rf dist

echo "🔧 Building with uv..."
python -m build

echo "🚀 Publishing with uv..."
uv publish

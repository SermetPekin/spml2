#!/bin/bash

set -e  # Exit on error

echo "🧹 .................. black ................"
black .

echo "🧹 .................. pytest ................"
pytest -v


echo " .................. 🧹 ruff ................"
ruff check .

echo " ..................🧹 Removing dist/..."
rm -rf dist

echo " ..................🔧 Building with uv..."
python -m build

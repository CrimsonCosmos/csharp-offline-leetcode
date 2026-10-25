#!/usr/bin/env bash
# Usage: ./run.sh <problem number or part of the name> [--unordered] [--all] [--stop]
#   ./run.sh 2
#   ./run.sh longest-substring
#   ./run.sh 46 --unordered
set -e
cd "$(dirname "$0")"

q="$1"
if [ -z "$q" ]; then
  echo "usage: ./run.sh <problem number or part of the name> [--unordered] [--all] [--stop]"
  exit 2
fi
shift

if [[ "$q" =~ ^[0-9]+$ ]]; then
  dir=$(ls problems | grep "^$(printf '%04d' "$((10#$q))")-" | head -1 || true)
else
  dir=$(ls problems | grep -i -- "$q" | head -1 || true)
fi
if [ -z "$dir" ]; then
  echo "No problem matching '$q'. See INDEX.md."
  exit 2
fi

echo "== $dir"
dotnet run --project Practice -p:Problem="$dir" --nologo -v q -- "$PWD/problems/$dir" "$@"

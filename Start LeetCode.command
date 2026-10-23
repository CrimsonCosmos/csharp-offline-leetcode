#!/usr/bin/env bash
# macOS: double-click this file. (Also works from a Linux terminal.)
# Resolve symlinks so a shortcut on the Desktop still finds the project folder.
src="$0"; while [ -L "$src" ]; do d="$(cd "$(dirname "$src")" && pwd)"; src="$(readlink "$src")"; [[ "$src" != /* ]] && src="$d/$src"; done
cd "$(dirname "$src")" || exit 1

# Finder starts scripts with a minimal PATH; add the usual .NET locations.
export PATH="$PATH:/usr/local/share/dotnet:/opt/homebrew/bin:/usr/local/bin:$HOME/.dotnet:/usr/share/dotnet"

if ! command -v dotnet >/dev/null 2>&1; then
  echo "The .NET SDK (version 8 or newer) is required but was not found."
  if command -v brew >/dev/null 2>&1; then
    read -r -p "Install it now with Homebrew? [y/N] " a
    if [[ "$a" =~ ^[Yy] ]]; then brew install --cask dotnet-sdk && echo "Done. Run this again." ; read -r -p "Press Enter to close." _; exit; fi
  fi
  echo "Download it from https://dotnet.microsoft.com/download"
  (open https://dotnet.microsoft.com/download 2>/dev/null || xdg-open https://dotnet.microsoft.com/download 2>/dev/null) || true
  read -r -p "Press Enter to close." _
  exit 1
fi

dotnet run --project Server -c Release --nologo -v q -- "$@" || { echo; read -r -p "Press Enter to close." _; }

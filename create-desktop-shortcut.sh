#!/usr/bin/env bash
# macOS / Linux: puts a "C# LeetCode" launcher on your Desktop.
here="$(cd "$(dirname "$0")" && pwd)"
desk="${XDG_DESKTOP_DIR:-$HOME/Desktop}"; mkdir -p "$desk"
if [ "$(uname)" = Darwin ]; then
  ln -sf "$here/Start LeetCode.command" "$desk/C# LeetCode.command"
  echo "Created $desk/C# LeetCode.command (double-click it)."
else
  f="$desk/csharp-leetcode.desktop"
  printf '[Desktop Entry]\nType=Application\nName=C# LeetCode\nExec=bash "%s/start-leetcode.sh"\nPath=%s\nTerminal=true\nIcon=utilities-terminal\n' "$here" "$here" > "$f"
  chmod +x "$f"; command -v gio >/dev/null && gio set "$f" metadata::trusted true 2>/dev/null
  echo "Created $f (right-click > Allow Launching if your desktop asks)."
fi

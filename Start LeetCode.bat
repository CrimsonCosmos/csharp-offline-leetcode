@echo off
setlocal
title C# LeetCode (offline)
cd /d "%~dp0"

where dotnet >nul 2>nul
if errorlevel 1 (
  echo The .NET SDK ^(version 8 or newer^) is required but was not found.
  where winget >nul 2>nul
  if not errorlevel 1 (
    choice /M "Install it now with winget"
    if not errorlevel 2 (
      winget install --id Microsoft.DotNet.SDK.8 -e --accept-source-agreements --accept-package-agreements
      echo.
      echo Done. Close this window and double-click "Start LeetCode" again.
      pause
      exit /b
    )
  )
  echo Download it from https://dotnet.microsoft.com/download then run this again.
  start "" https://dotnet.microsoft.com/download
  pause
  exit /b 1
)

dotnet run --project Server -c Release --nologo -v q -- %*
if errorlevel 1 pause

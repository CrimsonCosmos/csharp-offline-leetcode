@echo off
cd /d "%~dp0"
powershell -NoProfile -Command "$d=[Environment]::GetFolderPath('Desktop'); $s=(New-Object -ComObject WScript.Shell).CreateShortcut(\"$d\C# LeetCode.lnk\"); $s.TargetPath='%~dp0Start LeetCode.bat'; $s.WorkingDirectory='%~dp0'; $s.IconLocation='shell32.dll,13'; $s.Save()"
echo Created "C# LeetCode" on your Desktop. Double-click it to start.
pause

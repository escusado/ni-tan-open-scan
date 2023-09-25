#!/bin/bash

cd /app || exit
echo "🌳 Starting app..."
python3 -m http.server 8000 &>/dev/null &

if pgrep -f "sudo python3 index.py" &>/dev/null; then
    echo "scanner code already running ⚠"
    exit
else
    sudo python3 index.py
fi
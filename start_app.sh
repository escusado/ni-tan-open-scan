#!/bin/bash

cd /app || exit
sudo python3 index.py &
python3 -m http.server 8000 &
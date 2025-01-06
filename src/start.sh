#!/bin/bash


cd "$(dirname "$0")"

session_name="temnomor_website"

python_script="main.py"

screen -S "$session_name" -dm bash -c '
    /home/confi/.local/bin/uv run python3 "'"$python_script"'"
'

echo "Screen session '$session_name' создана и запущена."
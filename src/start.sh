#!/bin/bash

cd "$(dirname "$0")"

session_name="temnomor_website"

screen -S "$session_name" -dm bash -c '

    /home/confi/.local/bin/poetry run gunicorn
'

echo "Screen session '$session_name' создана и запущена."
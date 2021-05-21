#! /bin/bash

# set -e

# name: docker container name
name="$1"
did="$2"

year="$3"
month="$4"

echo "[open wallet]"

docker exec -iu 0 "$name" python3 /home/indy/get_attrib.py "${did}" "${year}" "${month}"

docker cp "$name":/home/indy/attrib.json /home/deploy

echo "<< Process End >>"
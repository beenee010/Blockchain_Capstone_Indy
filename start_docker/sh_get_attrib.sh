#! /bin/bash

# set -e

# name: docker container name
name="$1"
admin_did="$2"
user_did="$3"

year="$4"
month="$5"

echo "[open wallet]"

# Get Attrib info with params & Export ouput file
docker exec -iu 0 "$name" python3 /home/indy/get_attrib.py "${admin_did}" "${user_did}" "${year}" "${month}"

# Copy output file to Deploy folder
docker cp "$name":/home/indy/attrib.json /home/deploy

echo "<< Process End >>"
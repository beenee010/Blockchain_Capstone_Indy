#!/bin/bash

# set -e

# name: docker container name
name="$1"
wallet_name="$2"
wallet_key="$3"
did="$4"

building="$5"
year="$6"
month="$7"
day="$8"

echo "[open wallet]"

echo "\twallet_name: ${wallet_name}"
echo "\twallet_key: ${wallet_key}"

docker exec -iu 0 "$name" python3 /home/indy/generate_attrib.py "${wallet_name}" "${wallet_key}" "${did}" "${building}" "${year}" "${month}" "${day}"

docker cp "$name":/home/indy/gen_attrib.json /home/deploy
# docker cp "$name":/home/indy/gen_attrib.json ./
docker exec -iu 0 "$name" rm gen_attrib.json

echo [Log File Copy}

echo "<< Process End >>"

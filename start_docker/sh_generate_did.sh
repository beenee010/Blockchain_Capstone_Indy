#!/bin/bash

# set -e

# name: docker container name
name="$1"
wallet_name="$2"
wallet_key="$3"
seed="$4"

echo create wallet and did !!

echo "${wallet_name}"
echo "${wallet_key}"

# Generate DID with params & Export ouput file
docker exec -iu 0 "$name" python3 /home/indy/generate_did.py "${wallet_name}" "${wallet_key}" "${seed}"

# Copy output file to Deploy folder
docker cp "$name":/home/indy/data.json /home/deploy
echo file copy !!

echo "<process end>"

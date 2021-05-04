#!/bin/bash

set -e

name="$1"
email="$2"
wallet_name="$3"
wallet_key="$4"

echo create wallet and did !!

echo "${wallet_name}"
echo "${wallet_key}"

docker exec -itu 0 "$name" python3 /home/indy/generate_did.py "${email}" "${wallet_name}" "${wallet_key}"

echo file copy !!
docker cp "$name":/home/indy/data.json ./

echo "<process end>"

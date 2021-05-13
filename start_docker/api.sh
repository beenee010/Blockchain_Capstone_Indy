#!/bin/bash

set -e

name="$1"
wallet_name="$2"
wallet_key="$3"

echo create wallet and did !!

echo "${wallet_name}"
echo "${wallet_key}"

docker exec -iu 0 "$name" python3 /home/indy/generate_did.py "${wallet_name}" "${wallet_key}"

echo file copy !!
sudo docker cp "$name":/home/indy/data.json /home/caps/

echo "<process end>"

#!/bin/bash

set -e

name="$1"
email="$2"

echo create wallet and did !!

docker exec -itu 0 "$name" python3 /home/indy/generate_did.py "${email}"

echo file copy !!
docker cp "$name":/home/indy/data.json ./

echo "<process end>"

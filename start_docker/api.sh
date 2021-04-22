#!/bin/bash

set -e

name="$1"
email="$2"

echo create wallet and did !!

docker exec -it "$name" sh /home/indy/start.sh "${email}"

echo file copy !!
docker cp "$name":/home/indy/data.json /Users/beenie/

echo "<process end>"

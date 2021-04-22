#!/bin/bash

set -e

name="$1"

echo create wallet and did !!

docker exec -it "$name" sh /home/indy/test.sh

echo file copy !!
docker cp "$name":/home/indy/a.txt /home/test/

echo "<process end>"

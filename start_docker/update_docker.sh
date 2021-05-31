#!/bin/bash

# email=""
# passwd=""

docker_list="8982c855f98c 893deb256104" # 도커 컨테이너 ID 입력해주세요

echo "<< Process Start >>\n"

# for var in $docker_list
# do
#     docker exec -iu 0 $var git push 

for var in $docker_list
do
    # docker exec -iu 0 $var rm "$var":/home/indy/*
    docker cp /home/caps/indy/in_docker/. "$var":/home/indy/
    # docker cp ../in_docker/. "$var":/home/indy/
    echo "[Python File Copied]"
done
# Copy output file to Deploy folder

echo "<< Process End >>\n"

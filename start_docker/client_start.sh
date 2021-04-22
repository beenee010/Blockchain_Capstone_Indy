#!/bin/bash

set -e

IMAGE_NAME="$1"

sudo docker run -tid "$IMAGE_NAME" /bin/bash
# docker exec -itu 0 31a942d3ef43 /bin/bash


#docker build --tag indy-client .
#docker run -d -rm --name=$IMAGE_NAME
#docker run -itd --rm --name=$IMAGE_NAME --security-opt seccomp=unconfined --tmpfs /run --tmpfs /run/lock -v /sys/fs/cgroup:/sys/fs/cgroup:ro $IMAGE_NAME

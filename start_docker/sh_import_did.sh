#!/bin/bash

# set -e

# name: docker container name
name="$1"
wallet_name="$2"
wallet_key="$3"
new_key="$4"
seed="$5"

# Import DID to new wallet with params & Export ouput file
docker exec -iu 0 "${name}" python3 /home/indy/import_did.py "${wallet_name}" "${wallet_key}" "${new_key}" "${seed}"

# Write command file for indy-cli
echo "pool connect testpool"
echo "wallet attach" "${wallet_name}" >> wow.txt
echo "wallet open ""${wallet_name}" "key=""${new_key}" >> wow.txt
echo "did import /home/indy/did.json" >> wow.txt
echo "exit" >> wow.txt

# Copy output file to docker container
docker cp ./wow.txt "${name}":/home/indy

# Control indy-cli with command file
docker exec -iu 0 "${name}" indy-cli /home/indy/wow.txt

rm wow.txt

echo "<process end>"

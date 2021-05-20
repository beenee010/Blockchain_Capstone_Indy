#!/bin/bash

# set -e

name="$1"
did="$2"
seed="$3"
email="$4"
wallet_name="$5"
wallet_key="$6"

# export did
docker exec -iu 0 "${name}" python3 /home/indy/export_did.py "${did}" "${seed}"

# did import
echo "pool connect testpool" >> new_wallet_command.txt
echo "wallet create ""${wallet_name}" "key=""${wallet_key}" >> new_wallet_command.txt
echo "wallet open ""${wallet_name}" "key=""${wallet_key}" >> new_wallet_command.txt
echo "did import /home/indy/""${seed}""did.json" >> new_wallet_command.txt
echo "wallet close " >> new_wallet_command.txt
echo "wallet detach" "${wallet_name}" >> new_wallet_command.txt
echo "exit" >> new_wallet_command.txt

docker cp ./new_wallet_command.txt "${name}":/home/indy
docker exec -iu 0 "${name}" indy-cli /home/indy/new_wallet_command.txt

# set metadata
docker exec -iu 0 "${name}" python3 /home/indy/set_metadata.py "${wallet_name}" "${wallet_key}"

# export new wallet id
docker exec -iu 0 "${name}" python3 /home/indy/export_wallet_id.py "${email}" "${wallet_name}" "${seed}"

rm new_wallet_command.txt

docker cp "$name":/home/indy/"${seed}"NewWalletID.json /home/deploy
echo file copy !!

echo "<process end>"
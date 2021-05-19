#!/bin/bash

# set -e

name="$1"
wallet_name="$2"
wallet_key="$3"
new_key="$4"
seed="$5"

# wallet attach
echo "pool connect testpool" >> attach_command.txt
echo "wallet attach" "${wallet_name}" >> attach_command.txt
echo "exit" >> attach_command.txt

docker cp ./attach_command.txt "${name}":/home/indy
docker exec -iu 0 "${name}" indy-cli /home/indy/attach_command.txt

# wallet recreate
docker exec -iu 0 "${name}" python3 /home/indy/recreate_wallet.py "${wallet_name}" "${wallet_key}" "${new_key}" "${seed}"

# did import
echo "pool connect testpool" >> did_import_command.txt
echo "wallet open ""${wallet_name}" "key=""${new_key}" >> did_import_command.txt
echo "did import /home/indy/did.json" >> did_import_command.txt
echo "wallet close " >> did_import_command.txt
echo "wallet detach" "${wallet_name}" >> did_import_command.txt
echo "exit" >> did_import_command.txt

docker cp ./did_import_command.txt "${name}":/home/indy
docker exec -iu 0 "${name}" indy-cli /home/indy/did_import_command.txt

# set metadata
docker exec -iu 0 "${name}" python3 /home/indy/set_metadata.py "${wallet_name}" "${new_key}"

rm did_import_command.txt
rm attach_command.txt

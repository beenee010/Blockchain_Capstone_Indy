"""
Example demonstrating how to add DID with the role of Trust Anchor to ledger.
Uses seed to obtain Steward's DID which already exists on the ledger.
Then it generates new DID/Verkey pair for Trust Anchor.
Using Steward's DID, NYM transaction request is built to add Trust Anchor's DID and Verkey
on the ledger with the role of Trust Anchor.
Once the NYM is successfully written on the ledger, it generates new DID/Verkey pair that represents
a client, which are used to create GET_NYM request to query the ledger and confirm Trust Anchor's Verkey.
For the sake of simplicity, a single wallet is used. In the real world scenario, three different wallets
would be used and DIDs would be exchanged using some channel of communication
"""

import asyncio
from collections import OrderedDict
import json
import pprint
import sys

from indy import pool, ledger, wallet, did
from indy.error import IndyError, ErrorCode

from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION

pool_name = 'testpool'
steward_did = 'Th7MpTaRZVRYnPiabds81Y'
genesis_file_path = get_pool_genesis_txn_path(pool_name)

user_data = OrderedDict()

# User E-Mail Address
email = sys.argv[1]
wallet_name = sys.argv[2]
wallet_key = sys.argv[3]

wallet_config = json.dumps({"id": wallet_name})
wallet_credentials = json.dumps({"key": wallet_key})

def print_log(value_color="", value_noncolor=""):
    """set the colors for text."""
    HEADER = '\033[92m'
    ENDC = '\033[0m'
    print(HEADER + value_color + ENDC + str(value_noncolor))


async def write_nym_and_query_verkey():
    try:
        await pool.set_protocol_version(PROTOCOL_VERSION)

        print_log('genesis_txn: ', genesis_file_path)

        # 2.
        print_log('\n1. Open pool ledger and get handle from libindy\n')
        pool_handle = await pool.open_pool_ledger(config_name=pool_name, config=None)
       
        # 3.
        print_log('\n2. Creating new secure wallet\n')
        try:
            await wallet.create_wallet(wallet_config, wallet_credentials)
        except IndyError as ex:
            if ex.error_code == ErrorCode.WalletAlreadyExistsError:
                pass

        # 4.
        print_log('\n3. Open wallet and get handle from libindy\n')
        wallet_handle = await wallet.open_wallet(wallet_config, wallet_credentials)

        #5.
        print_log('\n4. Generating and storing DID and verkey representing a Client\n')
        client_did, client_verkey = await did.create_and_store_my_did(wallet_handle, "{}")
        print_log('Client DID: ', client_did)
        print_log('Client Verkey: ', client_verkey)
        # Step 5 code goes here.

        # Make Json File to docker
        user_data["email"] = email
        user_data["did"] = client_did
        # user_data["date"] = now.YEAR
        print_log('\n5. Make User EMail, DID Json File\n')
        print(json.dumps(user_data, ensure_ascii=False, indent="\t"))

        with open('data.json','w',encoding="utf-8") as make_file:
            json.dump(user_data, make_file, ensure_ascii=False, indent="\t")
        
        ########################
        nym_transaction_request = await ledger.build_nym_request(steward_did,client_did,'~7TYfekw4GUagBnBVCqPjiC','','')
        print_log(nym_transaction_request)

        nym_transaction_response = await ledger.sign_and_submit_request(pool_handle=pool_handle,
                                                                        wallet_handle=wallet_handle,
                                                                        submitter_did=steward_did,
                                                                        request_json=nym_transaction_request)
        print_log(nym_transaction_response)
        ########################
        print_log('\n6. End of Process\n')

    except IndyError as e:
        print('Error occurred: %s' %e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(write_nym_and_query_verkey())
    loop.close()


if __name__ == '__main__':
    main()

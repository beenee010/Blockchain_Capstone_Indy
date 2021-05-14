import asyncio
from collections import OrderedDict
import json
import pprint
import sys

from indy import pool, ledger, wallet, did
from indy.error import IndyError, ErrorCode

from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION, add_error, print_log

pool_name = 'testpool'
steward_did = 'Th7MpTaRZVRYnPiabds81Y'
genesis_file_path = get_pool_genesis_txn_path(pool_name)

user_data = OrderedDict()

# User E-Mail Address
email = sys.argv[1]
wallet_name = sys.argv[2]
wallet_key = sys.argv[3]
user_did = sys.argv[4]

att_building = sys.argv[5]
att_year = sys.argv[6]
att_month = sys.argv[7]
att_day = sys.argv[8]


wallet_config = json.dumps({"id": wallet_name})
wallet_credentials = json.dumps({"key": wallet_key})


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
            add_error("attrib.json")
            if ex.error_code == ErrorCode.WalletAlreadyExistsError:
                pass

        # 4.
        print_log('\n3. Open wallet and get handle from libindy\n')
        wallet_handle = await wallet.open_wallet(wallet_config, wallet_credentials)

        #5.
        print_log('\n4. Get DID and Verkey From wallet\n')
        did_result = await did.get_my_did_with_meta(wallet_handle, user_did)
        print_log('DID_Result ', did_result)
        
        # 6.
        print_log('\n5. Generate Attrib Transaction\n')
        attrib_transaction_request = await ledger.build_attrib_request(user_did, user_did,None, '{"'+user_did + '_' + att_building + '_' + att_year + att_month + att_day + '":{"name":"' + user_did + '"}}', None)
        # # user_data["date"] = now.YEAR
        # print_log('\n5. Make User EMail, DID Json File\n')
        # print(json.dumps(user_data, ensure_ascii=False, indent="\t"))

        # with open('data.json','w',encoding="utf-8") as make_file:
        #     json.dump(user_data, make_file, ensure_ascii=False, indent="\t")
        
        ########################

        attrib_transaction_response = await ledger.sign_and_submit_request(pool_handle=pool_handle,
                                                                        wallet_handle=wallet_handle,
                                                                        submitter_did=user_did,
                                                                        request_json=attrib_transaction_request)
        print_log(attrib_transaction_response)
        ########################
        print_log('\n6. End of Process\n')

    except IndyError as e:
        add_error("attrib.json")
        print('Error occurred: %s' %e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(write_nym_and_query_verkey())
    loop.close()


if __name__ == '__main__':
    main()

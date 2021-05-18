import asyncio
from collections import OrderedDict
import time
import json
import pprint
import sys
import logging
from indy import pool, ledger, wallet, did
from indy.error import IndyError, ErrorCode
from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION

wallet_name = sys.argv[1]
wallet_key = sys.argv[2]
user_did = sys.argv[3]

# att_building = sys.argv[4]
att_year = sys.argv[4]
att_month = sys.argv[5]
att_day = sys.argv[6]

pool_name = 'testpool'
steward_did = 'Th7MpTaRZVRYnPiabds81Y'
genesis_file_path = get_pool_genesis_txn_path(pool_name)

wallet_config = json.dumps({"id": wallet_name})
wallet_credentials = json.dumps({"key": wallet_key})

def print_log(value_color="", value_noncolor=""):
    """set the colors for text."""
    HEADER = '\033[92m'
    ENDC = '\033[0m'
    print(HEADER + value_color + ENDC + str(value_noncolor))

async def get_attrib_transaction():
    try:
        await pool.set_protocol_version(PROTOCOL_VERSION)

        print_log('genesis_txn: ', genesis_file_path)

        # 2.
        print_log('\n1. Open pool ledger and get handle from libindy\n')
        pool_handle = await pool.open_pool_ledger(config_name=pool_name, config=None)

        # 4.
        print_log('\n3. Open wallet and get handle from libindy\n')
        wallet_handle = await wallet.open_wallet(wallet_config, wallet_credentials)

        #5.
        print_log('\n4. Get DID and Verkey From wallet\n')
        did_result = await did.get_my_did_with_meta(wallet_handle, user_did)
        print_log('DID_Result ', did_result)

        # 6. 
        with open('attrib.json','w',encoding="utf-8") as make_file:
            for building in range(1, 10):
                for i in range(1, int(att_day) + 1):
                    if i < 10:
                        raw = user_did + '_' + str(building) + '_' + att_year + att_month + "0" + str(i)
                    else:
                        raw = user_did + '_' + str(building) + '_' + att_year + att_month + str(i)
                    try:
                        get_attrib_request = await ledger.build_get_attrib_request(user_did,user_did,raw, None, None)
                        get_attrib_response = json.loads(await ledger.submit_request(pool_handle, get_attrib_request))

                        if get_attrib_response['result']['data'] is not None:
                            # print_log(raw)
                            print_log("Success")
                            print_log(get_attrib_response['result']['data'])                     
                            json.dump(json.loads(get_attrib_response['result']['data']), make_file, ensure_ascii=False, indent="\t")
                            make_file.write(",\n")
                        else:
                            # print_log(raw)
                            pass

                    except IndyError as ex:
                        if ex.error_code == ErrorCode.LedgerInvalidTransaction:
                            print_log(ex.error_code)
                            pass
                        else:
                            with open('attrib.json','w',encoding="utf-8") as make_file:
                                json.dump(json.loads(response), make_file, ensure_ascii=False, indent="\t")
            # temp = make_file.read()
            # make_file.write()

        print_log('\n6. End of Process\n')

    except IndyError as e:
        print('Error occurred: %s' %e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_attrib_transaction())
    loop.close()


if __name__ == '__main__':
    main()


import asyncio
from collections import OrderedDict
import json
import pprint
import sys
from indy import pool, ledger, wallet, did
from indy.error import IndyError, ErrorCode
from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION

email = sys.argv[1]
wallet_name = sys.argv[2]
wallet_key = sys.argv[3]
user_did = sys.argv[4]

att_building = sys.argv[5]
att_year = sys.argv[6]
att_month = sys.argv[7]
att_day = sys.argv[8]

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

        # 3.


        # 4.
        print_log('\n3. Open wallet and get handle from libindy\n')
        wallet_handle = await wallet.open_wallet(wallet_config, wallet_credentials)

        #5.
        print_log('\n4. Get DID and Verkey From wallet\n')
        did_result = await did.get_my_did_with_meta(wallet_handle, user_did)
        print_log('DID_Result ', did_result)
        
        # 6.
        for i in range(1, int(att_day)):
            try:
                get_attrib_request = await ledger.build_get_attrib_request(user_did,user_did,'{"'+user_did + '_' + att_building + '_' + att_year + att_month + str(i) + '":{"name":"' + user_did + '"}}', None, None)
                # get_attrib_response = await ledger.sign_and_submit_request(pool_handle=pool_handle,
                #                                                         wallet_handle=wallet_handle,
                #                                                         submitter_did=user_did,
                #                                                         request_json=get_attrib_request)
                
                pprint.pprint(json.loads(get_attrib_request))
            except IndyError as ex:
                if ex.error_code == ErrorCode.LedgerInvalidTransaction:
                    pass
                else:
                    with open('attrib.json','w',encoding="utf-8") as make_file:
                        json.dump(json.loads(get_attrib_request), make_file, ensure_ascii=False, indent="\t")
                        
            

        # print_log('\n5. Generate Attrib Transaction\n')
        # attrib_transaction_request = await ledger.build_attrib_request(user_did, user_did,None, '{"'+user_did + '_' + att_building + '_' + att_year + att_month + att_day + '":{"name":"' + user_did + '"}}', None)
        # # # user_data["date"] = now.YEAR
        # # print_log('\n5. Make User EMail, DID Json File\n')
        # # print(json.dumps(user_data, ensure_ascii=False, indent="\t"))

        # # with open('data.json','w',encoding="utf-8") as make_file:
        # #     json.dump(user_data, make_file, ensure_ascii=False, indent="\t")
        
        # ########################


        # print_log(get_attrib_response)
        ########################
        print_log('\n6. End of Process\n')

    except IndyError as e:
        print('Error occurred: %s' %e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_attrib_transaction())
    loop.close()


if __name__ == '__main__':
    main()

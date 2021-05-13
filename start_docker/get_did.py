import asyncio
import json
import pprint
import sys
import re

from indy import pool, ledger, wallet, did
from indy.error import IndyError, ErrorCode

from utils import get_pool_genesis_txn_path, PROTOCOL_VERSION

pool_name = 'test_pool'
genesis_file_path = get_pool_genesis_txn_path(pool_name)

wallet_name = sys.argv[1]
wallet_key = sys.argv[2]

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

        print_log('\n1. Creates a new local pool ledger configuration that is used '
                  'later when connecting to ledger.\n')
        pool_config = json.dumps({'genesis_txn': str(genesis_file_path)})
        try:
            await pool.create_pool_ledger_config(config_name=pool_name, config=pool_config)
        except IndyError as ex:
            if ex.error_code == ErrorCode.PoolLedgerConfigAlreadyExistsError:
                pass
        
        print_log('\nOpen pool ledger and get handle from libindy\n')
        pool_handle = await pool.open_pool_ledger(config_name=pool_name, config=None)
                
        print_log('\nOpen wallet and get handle from libindy\n')
        wallet_handle = await wallet.open_wallet(wallet_config, wallet_credentials)

        print_log('\nList my DID\n')
        my_did = await did.list_my_dids_with_meta(wallet_handle)
        list_did = my_did.split("},{")

        for i in list_did:
            print(i + "\n\n")
            if "StudentID" in i:
                i = re.sub("\[|\'|\]","", i)
                if i.count("{") != 1:
                    i = "{" + i
                elif i.count("}") != 1:
                    i = i + "}"
                print_log(i)
                jsonObject = json.loads(i)
                student_DID = jsonObject.get("did")
                print_log("Student DID: " + student_DID)
                with open('student_did.json','w',encoding="utf-8") as make_file:
                    # make_file.write(student_DID)
                    jsonObject['verkey'] = "None"
                    json.dump(jsonObject, make_file, ensure_ascii=False, indent="\t")
                break
        
        
            
    except IndyError as e:
        print('Error occurred: %s' % e)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(write_nym_and_query_verkey())
    loop.close()


if __name__ == '__main__':
    main()



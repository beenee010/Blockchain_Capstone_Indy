import asyncio
from collections import OrderedDict
import json
import pprint
import sys
import re

# Exported DID
did_db = sys.argv[1]

# User DID's Seed
student_seed = sys.argv[2]

# create DID File.
print('\n4. Parse DID \n')
did_seed = "0000000000000000STUDENT" + student_seed
result = {}
result['version'] = 1
result['dids'] = []
_did = {}
_did['did'] = did_db
_did['seed'] = did_seed
# _did['metadata'] = "StudentID"
result['dids'].append(_did)

('\n5. Export DID \n')

with open(student_seed+'did.json','w',encoding="utf-8") as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\t")

    print('\nExport DID Success!! \n')

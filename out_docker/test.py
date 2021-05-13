from collections import OrderedDict
import json
import sys

user_data = OrderedDict()

email = sys.argv[1]
client_did = sys.argv[2]

user_data["email"] = email
user_data["did"] = client_did

print(json.dumps(user_data, ensure_ascii=False, indent="\t"))

with open('data.json','w',encoding="utf-8") as make_file:
    json.dump(user_data, make_file, ensure_ascii=False, indent="\t")

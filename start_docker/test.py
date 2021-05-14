# from collections import OrderedDict
# import json
import sys

# user_data = OrderedDict()

# email = sys.argv[1]
# client_did = sys.argv[2]

# user_data["email"] = email
# user_data["did"] = client_did

# print(json.dumps(user_data, ensure_ascii=False, indent="\t"))

# with open('data.json','w',encoding="utf-8") as make_file:
#     json.dump(user_data, make_file, ensure_ascii=False, indent="\t")

user_did = sys.argv[1]
att_building = sys.argv[2]
att_year = sys.argv[3]
att_month = sys.argv[4]
att_day = sys.argv[5]

with open('attrib.json','w',encoding="utf-8") as make_file:
    for i in range(1, int(att_day) + 1):
        if i < 10:
            make_file.write("ledger get-attrib did=" + user_did + " raw=" + user_did + att_building + att_year + att_month + "0"+str(i) + "\n")
        else:
            make_file.write("ledger get-attrib did=" + user_did + " raw=" + user_did + att_building + att_year + att_month + str(i) + "\n")


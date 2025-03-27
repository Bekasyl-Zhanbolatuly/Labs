import json

with open("C:/Users/Admin/Downloads/sample-data.json", "r") as f:
    a = json.load(f)
print("Interface Status")
print("="*80)
print("DN", " "*42,"DESCRIPTION", " "*5, "SPEED", " "*4, "MTU")
print("-"*45, '-'*17, '-'*9, '-'*6)
for x in a["imdata"]:
    print(x['l1PhysIf']['attributes']["dn"], end="   "*8)
    print(x['l1PhysIf']['attributes']['speed'], end="   ")
    print(x['l1PhysIf']['attributes']['mtu'])
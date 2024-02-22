import json

def sort_execution():
    with open("operations.json", "r", encoding="utf-8") as f:
        transfers = json.load(f)

    transfers_executed = []

    for transfer in transfers:
        if transfer.get("state") == "EXECUTED":
            transfers_executed.append(transfer)

    return transfers_executed


#print(sort_execution())
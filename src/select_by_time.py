from datetime import datetime
from src.select_execution import sort_execution


def last_sel():
    sel_time = sort_execution()
    for transfer in sel_time:
        if transfer.get('date'):
            transfer['date'] = transfer['date'][:10]

    for transfer in sel_time:
        if transfer.get('date'):
            last_sel_time = sorted(sel_time, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
    last_five = last_sel_time[0:5]
    return last_five

#print(last_sel())
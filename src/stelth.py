from select_by_time import last_sel

transfer_by_stars = last_sel()
def stelth_star():


    for transfer in transfer_by_stars:

        if transfer.get('from'):
            transfer['from'] = transfer['from'][:-10]+"*"*6+transfer['from'][-4:]

        if transfer.get('to'):
            transfer['to'] = transfer['to'][4]+"**"+transfer['to'][-4:]

    # print(transfer_by_stars)
    # print(len(transfer_by_stars))
    return transfer_by_stars

print(stelth_star())
from stelth import stelth_star

def separation_line():
    separation = stelth_star()
    for transfer in separation:
        if transfer.get('from'):
            transfer['from'] = (transfer['from'][:-16]+" "+transfer['from'][-16:-12]+" "
                                   +transfer['from'][-12:-8]+" "+transfer['from'][-8:-4]+" "
                                   +transfer['from'][-4:])

    return separation

#print(separation_line())
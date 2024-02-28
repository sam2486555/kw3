from src.split import separation_line

def output():
    output_display = separation_line()

    for transfer in output_display:
        print(f"""
{transfer['date'][8:10]+'.'+transfer['date'][5:7]+'.'+transfer['date'][:4]} {transfer['description']}
{transfer.get('from', '')} -> {transfer['to']}
{transfer['operationAmount']['amount']} {transfer['operationAmount']['currency']['name']}""")
    return


print(output())

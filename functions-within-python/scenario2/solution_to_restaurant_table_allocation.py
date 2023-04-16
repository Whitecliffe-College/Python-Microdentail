# define a function to allocate tables
# and we should allocate tables to vip customers first
def allocate_tables(tables, customers):
    # allocate tables to vip customers
    for customer in customers:
        if customer['vip']:
            for table in tables:
                if table['capacity'] >= customer['size']:
                    table['available'] = False
                    customer['table'] = table['number']
                    break
    # allocate tables to normal customers
    for customer in customers:
        if not customer['vip']:
            for table in tables:
                if table['capacity'] >= customer['size'] and table['available']:
                    table['available'] = False
                    customer['table'] = table['number']
                    break
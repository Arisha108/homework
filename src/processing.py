def filter_by_state(my_list, state='EXECUTED'):
    new_data = []
    for i in my_list:
        if i['state'] == state:
            new_data.append(i)
    return new_data



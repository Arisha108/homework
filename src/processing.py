def filter_by_state(my_list, state='EXECUTED'):
    new_data = []
    for i in my_list:
        if i['state'] == state:
            new_data.append(i)
    return new_data


def sort_by_date(my_list, reverse=True):
    new_data = sorted(my_list, key=lambda x: x['date'], reverse=reverse)

    return new_data




def filter_by_state(my_list:list, state:str='EXECUTED') -> list:
    """
    Функция, которая принимает на вход список словарей
    и возвращает отфильтрованный список по ключу state
    """
    new_data = []
    for i in my_list:
        if i['state'] == state:
            new_data.append(i)
    return new_data


def sort_by_date(my_list:list, reverse:bool=True) -> list:
    """
    Функция, котооая принимает на вход список словарей
    и возвращает отсортированный список по ключу date
    """
    new_data = sorted(my_list, key=lambda x: x['date'], reverse=reverse)

    return new_data




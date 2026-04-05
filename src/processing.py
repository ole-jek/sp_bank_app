def filter_by_state(id_list: list, state: str = 'EXECUTED') -> list:
    new_list = []
    for item in id_list:
        if item['state'] == state:
            new_list.append(item)
    return new_list



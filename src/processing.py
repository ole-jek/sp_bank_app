def filter_by_state(id_list: list, state: str = "EXECUTED") -> list:
    """Возвращает новый лист со словарями соответствующими ключу"""
    new_list = []
    for item in id_list:
        if item["state"] == state:
            new_list.append(item)
    return new_list


def get_iem_date(item: dict) -> str:
    """Вспомогательная функция для нахождения даты из словаря и передачи в функцию sorted"""
    return item["date"]


def sort_by_date(id_list: list, decreasing: bool = True) -> list:
    """Сортировка списка по датам"""
    return sorted(id_list, key=get_iem_date, reverse=decreasing)

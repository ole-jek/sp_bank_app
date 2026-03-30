from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_num: str) -> str:
    """Маскирует номер карты или счета, отделяя название от цифр."""
    input_length = len(input_num)
    name = ""
    acc_num = ""
    for i in range(input_length):
        if not input_num[i].isdigit():
            name += input_num[i]
        else:
            acc_num += input_num[i]
    name = name.strip()
    if len(acc_num) <= 16:
        return f"{name} {get_mask_card_number(acc_num)}"
    else:
        return f"{name} {get_mask_account(acc_num)}"

def get_date(date_str: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
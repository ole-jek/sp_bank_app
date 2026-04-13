def get_mask_card_number(card_num: str) -> str:
    """Маскирует номер карты"""
    if not card_num:
        return ""
    num_length = len(card_num)
    masked_num = card_num[:6] + "*" * (num_length - 10) + card_num[-4:]
    final_masked_num = ""
    for i in range(num_length):
        final_masked_num += masked_num[i]
        if (i + 1) % 4 == 0 and (i + 1) != num_length:
            final_masked_num += " "
    return final_masked_num


def get_mask_account(acc_num: str) -> str:
    """Маскирует номер аккаунта"""
    if not acc_num:
        return ""
    if len(acc_num) < 4:
        return f"**{acc_num}"
    return f"**{acc_num[-4:]}"

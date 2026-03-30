def get_mask_card_number(card_num: str) -> str:
    return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"


def get_mask_account(acc_num: str) -> str:
    return f"**{acc_num[-4:]}"

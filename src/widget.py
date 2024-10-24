import masks


def mask_account_card(card_account: str) -> str:
    """Функция, которая выводит тип и замаскированный номер карты или счета"""
    card_account_clean = ""
    for i in card_account:
        if i.isdigit():
            card_account_clean += i

    if len(card_account_clean) == 16:
        result_digits = masks.get_mask_card_number(card_account_clean)
    else:
        result_digits = masks.get_mask_account(card_account_clean)

    card_account_name = ""
    for i in card_account:
        if i.isalpha() or i == " ":
            card_account_name += i

    result = str(card_account_name + result_digits)
    return result


def get_date(i):
    result = i[8] + i[9] + "." + i[5] + i[6] + "." + i[0] + i[1] + i[2] + i[3]
    return result


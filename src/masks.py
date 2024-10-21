def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход 16-значный номер карты
     и возвращает в формате XXXX XX** **** XXXX
    """
    mask_number = str(card_number)
    mask_number = mask_number[:6] + "******" + mask_number[12:]
    mask_number = mask_number[:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:]
    return mask_number


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает на вход 20-значный номер счета
     и возвращает в формате **XXXX
    """
    mask_account = str(account_number)
    mask_account = "**" + mask_account[-4:]
    return mask_account

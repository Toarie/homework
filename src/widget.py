def mask_account_card(card_info):
    # Разделяем строку на тип карты/счета и номер
    type_number = card_info.split(" ")[1]
    # Проверяем, является ли первая цифра нулем (если да, то это счет)
    if type_number[0] == "0":
        return f"Счет ***{type_number[-4:]}"
    else:
        return f"{card_info[:12]} {card_info[12:-4]} **** {card_info[-4:]}"

    import datetime

    def get_date(dt_str):
        dt_obj = datetime.datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%S.%f')
        return dt_obj.strftime('%d.%m.%Y')

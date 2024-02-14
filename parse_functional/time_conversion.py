import datetime


def month_number(month_name:str) -> str:
    """Функция предназначена для преобразования названия
    месяца (полное или сокращенное) в численную форму"""
    if len(month_name) > 3:
        month_num = datetime.datetime.strptime(month_name, '%B').month
    else:
        month_num = datetime.datetime.strptime(month_name, '%b').month
    return f"{month_num:02}"


def date_conversion(date_string:str)->str:
    """Функция предназначена для преобразования строки с датой публикации
    из вида 'February 15 2023 - 15:50' в строку вида: '15|02|2023'"""
    date_elements = date_string.split()
    print(date_elements)
    day_number = int(date_elements[1])
    month_num = month_number(date_elements[0])
    year_number = date_elements[2]
    return f"{day_number:02}/{month_num}/{year_number}"


def conversion_str_date_to_datetimeformat(date_string: str):
    """Функция предназначена для преобразования строки к формату date, с помощью модуля datetime"""
    try:
        date = datetime.datetime.strptime(date_string, '%d/%m/%Y').date()
        return date
    except:
        return None
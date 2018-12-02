#!/usr/bin/python3

from random import randint
from datetime import datetime, timedelta

class LS(object):
    """docstring for LS"""
    def __init__(self):
        super(LS, self).__init__()

    def object(self, is_mane=False):

        number = randint(10_000_000_000,99_999_999_999)

        content_json =  {
            "billing_object_id": randint(100000,399999),
            "billing_object_number": str(number),
            "main_ls": str(1 if is_mane else 0)
        }

        return content_json

    def details(self):

        delta = randint(1,30)
        dolgna = (datetime.now()).isoformat(timespec='milliseconds')
        delo = (datetime.now() - timedelta(days=delta)).isoformat(timespec='milliseconds')

        content_json = {
            "EMAILVCHEK": "enable2005@yandex.ru",
            "ADRES": "г Тверь, ул Оснабрюкская, д 27к1, кв 14",
            "BALANS": randint(-999999,999999),
            "VHPENI": 0,
            "DELO": "{}".format(delo) if randint(0,3) == 3 else "",
            "DOKSOBS": "",
            "DOLGNA": "{}".format(dolgna),
            "ZHILPLOSCH": "0",
            "ISHPENI": randint(0,99),
            "KACHESTVO": randint(0,99),
            "KOMNATY": str(randint(1,9)),
            "KOPLATE": randint(0,99),
            "KOPLATESPENI": randint(100_000,999_999),
            "LS": str(randint(10_000_000_000,99_999_999_999)),
            "NACHISLENO": randint(-9_999_999,9_999_999),
            "OBSCHPLOSCH": "42.3",
            "OPLACHENO": randint(0,99),
            "OPLACHENOZAKRMES": randint(0,99),
            "OPLACHENOPENI": randint(0,99),
            "OPLACHENOPENIZAKRMES": randint(0,99),
            "OPLACHENOSPENI": randint(0,99),
            "OPLPENI": randint(0,99),
            "PVHSALDO": randint(0,99),
            "PENI": randint(0,99),
            "PERERASCHET": randint(0,99),
            "TELEFONVCHEK": "+79157053345",
            "TELNANIM": "89610165800",
            "FIONANIM": "Фамилия Имя Отчество",
            "CHISLPROP": "1"
        }

        return content_json

#-----------------------------------------------------------------------

if __name__ == '__main__':
    # print(datetime.now().isoformat(timespec='milliseconds'))
    # print(LS().details())
    pass

#-----------------------------------------------------------------------
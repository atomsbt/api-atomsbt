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
                    "EMAILVCHEK": "",
                    "ADRES": "г Тверь,ул Оснабрюкская,д.27к1 кв.14",
                    "BALANS": randint(10,9999999),
                    "VHPENI": 0,
                    "DELO": "{}".format(delo) if randint(0,3) == 3 else "",
                    "DOKSOBS": "",
                    "DOLGNA": "{}".format(dolgna),
                    "ZHILPLOSCH": "0",
                    "ISHPENI": 0,
                    "KACHESTVO": 0,
                    "KOPLATE": 489,
                    "KOPLATESPENI": 489,
                    "LS": "69100614420",
                    "NACHISLENO": 489,
                    "OBSCHPLOSCH": "42.3",
                    "OPLACHENO": 0,
                    "OPLACHENOZAKRMES": 27416,
                    "OPLACHENOPENI": 0,
                    "OPLACHENOPENIZAKRMES": 0,
                    "OPLACHENOSPENI": 0,
                    "OPLPENI": 0,
                    "PVHSALDO": 27416,
                    "PENI": 0,
                    "PERERASCHET": 0,
                    "TELEFONVCHEK": "",
                    "TELNANIM": "89610165800,",
                    "FIONANIM": "Фамилия И.О.",
                    "CHISLPROP": "1"
        }

        return content_json

#-----------------------------------------------------------------------

if __name__ == '__main__':
    # print(datetime.now().isoformat(timespec='milliseconds'))
    # print(LS().details())
    pass

#-----------------------------------------------------------------------
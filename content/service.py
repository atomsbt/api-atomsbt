#!/usr/bin/python3

from random import randint

class Service(object):
    """docstring for Service"""
    def __init__(self):
        super(Service).__init__()

        self.form_field_type = [
            "TEXT" #просто текст
            "NUMERIC" #цифры 12345678
            "MONEY" #поле ввода денежных единиц с разбивкой по разрядам
            "DATE" #ввод даты, на север уходит unixtime
            "COMBO_BOX" #поле с возможными значениями из values
            "CHECK_BOX" #поле имеет значение 0/1
            "PRINTED_TEXT" #поле нередактируемого текста, информационной надобности
        ]

    def element(self, e_name=None, e_type=None, e_params=False):

        service_id = randint(10_000_000_000,99_999_999_999)
        image_url = "https://via.placeholder.com/48x48"

        content = {
            "amount": 0,
            "amount_peni": 0,
            "nds": 18,
            "image_url": image_url if randint(0,3) != 3 else '',
            "id": service_id,
            "codeInBilling": service_id,
            "is_active": True if randint(0,5) != 5 else False,
            "name": e_name,
            "priority": 1,
            "type": e_type,
            "params": {
                "services": True if randint(0,5) != 5 else False,
                "counters": True if randint(0,5) != 5 else False,
                "payments": True if randint(0,5) != 5 else False
            } if e_params else {}
        }

        return content

    def form(self):
        pass

#-----------------------------------------------------------------------

if __name__ == '__main__':
    pass

#-----------------------------------------------------------------------


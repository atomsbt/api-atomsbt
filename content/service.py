#!/usr/bin/python3

from random import randint, choice


class Service(object):
    def __init__(self):
        super(Service).__init__()

        self.image_url = "https://via.placeholder.com/48x48"

    def element(self, e_name=None, e_type=None, e_params=False, e_image_url=None, e_codeInBilling=None):

        service_id = randint(10_000_000, 99_999_999)
        amount = randint(0, 999_999)
        image_url = e_image_url if not None else (
            self.image_url if randint(0, 3) != 3 else '')

        content = {
            "amount": amount,
            "amount_peni": int(amount*0.12),
            "nds": 18,
            "image_url": image_url,
            "id": service_id,
            "codeInBilling": e_codeInBilling or service_id,
            "is_active": True if randint(0, 5) != 5 else False,
            "name": e_name,
            "priority": 1,
            "type": e_type,
            "params": {
                "services": True if randint(0, 5) != 5 else False,
                "counters": True if randint(0, 5) != 5 else False,
                "payments": True if randint(0, 5) != 5 else False
            } if e_params else {}
        }

        return content


class Form(object):
    def __init__(self):
        super(Form, self).__init__()

        self.image_url = "https://via.placeholder.com/48x48"
        self.form_field_type = [
            "TEXT",  # просто текст
            "NUMERIC",  # цифры 12345678
            "MONEY",  # поле ввода денежных единиц с разбивкой по разрядам
            #"DATE",  # ввод даты, на север уходит unixtime
            "COMBO_BOX",  # поле с возможными значениями из values
            "CHECK_BOX",  # поле имеет значение 0/1
            "PRINTED_TEXT"  # поле нередактируемого текста
        ]

    def form(self, form_name: str, form_image=None, form_fields_count=1):
        """
        return {
            "id": str,
            "name": str,
            "image_url": str,
            "fields": [
                {

                }
            ]
        }
        """
        fields = list()
        for x in range(randint(1, form_fields_count if form_fields_count > 0 else 1)):
            field_type = self.form_field_type[randint(
                0, len(self.form_field_type)-1)]
            combo_count = 0 if field_type != 'COMBO_BOX' else randint(1, 10)
            field = Form().field('Поле типа {0} с номером {1}'.format(
                field_type, x), field_type, combo_count)
            fields.append(field)

        content = {
            "id": str(randint(10_000, 99_999)),
            "name": form_name,
            "image_url": form_image if not None else (self.image_url if randint(0, 3) != 3 else ''),
            "fields": fields
        }

        return content

    def field(self, field_name: str, field_type=None, field_values_count=0):
        """
        return {
            "id": str,
            "name": str,
            "type": str,
            "regexp": str,
            "error_msg": str,
            "values": [
                {
                    "id": str,
                    "value": str
                }
            ],
            "value": str
        }
        """
        array = list()
        for _ in range(randint(1, field_values_count)):
            guid = randint(100, 999)
            value = {
                "id": str(guid),
                "value": f'Значение {guid}' + choice([' тестовый текст для проверки 2х строчной выпадалки', ''])
            }
            array.append(value)

        regexp = '^(\\w{1,10}|\\d{1,10})'
        content = {
            "id": str(randint(1_000, 9_999)),
            "name": field_name,
            "type": field_type,
            "regexp": None if randint(0, 3) != 3 else regexp,
            "error_msg": "Указаны не верные данные",
            "values": array if len(array) > 0 else None,
            "value": (array[0]['id'] if randint(0, 5) > 2 else None) if len(array) > 0 else None
        }

        return content


# -----------------------------------------------------------------------

if __name__ == '__main__':
    # print(Form().form(form_name='Tect', form_fields_count=3))
    pass

# -----------------------------------------------------------------------

#!/usr/bin/python3

from random import randint

class Service(object):
    """docstring for Service"""
    def __init__(self):
        super(Service).__init__()

        self.image_url = "https://via.placeholder.com/48x48" if randint(0,3) != 3 else ''

    def element(self, e_name=None, e_type=None, e_params=False, e_image_url=None, e_codeInBilling=None):

        service_id = randint(10_000_000_000,99_999_999_999)
        amount = randint(0,999999)
        image_url = e_image_url if not None else self.image_url

        content = {
            "amount": amount,
            "amount_peni": int(amount*0.12),
            "nds": 18,
            "image_url": image_url,
            "id": service_id,
            "codeInBilling": e_codeInBilling or service_id,
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

class Form(object):
    """docstring for Form"""
    def __init__(self):
        super(Form, self).__init__()

        self.image_url = "https://via.placeholder.com/48x48"
        self.form_field_type = [
            "TEXT", #просто текст
            "NUMERIC", #цифры 12345678
            "MONEY", #поле ввода денежных единиц с разбивкой по разрядам
            "DATE", #ввод даты, на север уходит unixtime
            "COMBO_BOX", #поле с возможными значениями из values
            "CHECK_BOX", #поле имеет значение 0/1
            "PRINTED_TEXT" #поле нередактируемого текста, информационной надобности
        ]

    def form(self, form_name=None, form_fields_count=1):
        """
        1..1 form_name string
        1..1 form_fields array
        """
        fields = []
        for x in range(0, randint(1,form_fields_count if form_fields_count>0 else 1)):
            field_type = self.form_field_type[randint(0,len(self.form_field_type)-1)]
            combo_count = 0 if field_type != 'COMBO_BOX' else randint(0,10)
            field = Form().field('Поле типа {0} с номером {1}'.format(field_type, x), field_type, combo_count)
            fields.append(field)

        content = {
            "id": "{}".format(randint(10_000_000_000,99_999_999_999)),
            "name": form_name,
            "image_url": self.image_url if randint(0,3) != 3 else '',
            "fields": fields
        }

        return content

    def field(self, field_name=None, field_type=None, field_values_count=0):

        array = []
        for _ in range(0, randint(0,field_values_count)):
            guid = randint(10_000,99_999)
            value = {
                "id": guid,
                "value": "Значение {}".format(guid)
            }
            array.append(value)

        content = {
            "id": '{}'.format(randint(10_000_000_000,99_999_999_999)),
            "name": field_name,
            "type": field_type,
            "regexp": None if randint(0,3) != 3 else '^(\\w{1,10})',
            "error_msg": "Указаны не верные данные",
            "values": array if len(array)>0 else None,
            "value": ('{}'.format(array[0]['id']) if randint(0,5)>2 else None) if len(array)>0 else None
        }

        return content


#-----------------------------------------------------------------------

if __name__ == '__main__':
    # print(Form().form(form_name='Tect', form_fields_count=3))
    pass

#-----------------------------------------------------------------------
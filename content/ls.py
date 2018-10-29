#!/usr/bin/python3

from random import randint

class LS(object):
    """docstring for LS"""
    def __init__(self):
        super(LS, self).__init__()

    def content(self):

        number = randint(10_000_000_000,99_999_999_999)

        content_json =  {
            "billing_object_id": randint(100000,399999),
            "billing_object_number": str(number),
            "binding_status": 1,
            "main_ls": str(number)
        }

        return content_json

#-----------------------------------------------------------------------

if __name__ == '__main__':
    # print(LS().content())
    pass

#-----------------------------------------------------------------------
#!/usr/bin/python3

from random import randint
from datetime import datetime, timedelta

class Payment(object):
    """
    {
        "result": true,
        "page": 1,
        "pages": 1,
        "rowPerPage": 4,
        "totalRowsCount": 15,
        "data": [
            {
                "ROW_ID": "21973462",
                "DATA": "2017-12-05T00:00:00.000",
                "DATAVREMYA": "",
                "ISTOCHNIK": "Билинг",
                "SUMMA": 24577,
                "TRANZAKCIYA": ""
            },
            {
                "ROW_ID": "21436098",
                "DATA": "2017-11-10T00:00:00.000",
                "DATAVREMYA": "2017-11-10T12:12:34.000",
                "ISTOCHNIK": "Интернет Газпромбанк",
                "SUMMA": 100,
                "TRANZAKCIYA": "5a056d22f1031"
            }
        ]
    }
    """
    def __init__(self):
        super(Payment, self).__init__()

        self.url_pdf = "https://static.tinkoff.ru/documents/docs/terms_of_integrated_banking_services.pdf"

    def payment(self):

        delta = randint(1,30)
        date = (datetime.now() - timedelta(days=delta)).isoformat(timespec='milliseconds')

        content = {
                "ROW_ID": str(randint(1_000,9_999)),
                "DATA": date,
                "DATAVREMYA": date,
                "ISTOCHNIK": "Билинг",
                "SUMMA": randint(10,999999),
                "TRANZAKCIYA": str(randint(10_000,99_999)) if randint(0,3) != 3 else ""
        }

        return content

    def check(self, tranzakciya=None):
        return self.url_pdf

#-----------------------------------------------------------------------

if __name__ == '__main__':
    # print(Payment().payment())
    # print(Payment().check())
    pass

#-----------------------------------------------------------------------




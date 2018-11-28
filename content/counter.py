#!/usr/bin/python3

from random import randint
from datetime import datetime, timedelta

class Counter(object):
    """
    {
        "result": true,
        "data": [
            {
                "RowID": "1050194",
                "Tarifnost": 2,
                "NomerUslugi": 100,
                "NazvanieUslugi": "Электроснабжение ",
                "ZavodNomer": "112233",
                "Razradnost": "4",
                "KoefTrans": "1",
                "MaxPok": "3000",
                "result": "ЭЛ",
                "errorCode": "ЭЛ",
                "errorMessage": "ЭЛ",
                "ASKUE": "1",
                "DateCheck": "2018-11-01T00:00:00.000",
                "DateNextCheck": "2018-11-01T00:00:00.000",
                "NomerUslugiForBilling": "0100",
                "Tarif": [
                    {
                        "DatePok": "2018-11-01T00:00:00.000",
                        "NomerTarifa": 0,
                        "NazvanieTarifa": "День",
                        "PredPok": "0"
                    },
                    {
                        "DatePok": "2018-11-01T00:00:00.000",
                        "NomerTarifa": "1",
                        "NazvanieTarifa": "Ночь",
                        "PredPok": "0"
                    }
                ]
            }
        ],
        "PeriodSch": {
            "ot": "2018-11-01T00:00:00.000",
            "do": "2018-11-30T23:59:59.000"
        }
    }
    """
    def __init__(self, ls=None):
        super(Counter, self).__init__()

        self.ls = ls

    def counter(self, codeInBilling=None):

        tarifnost = randint(1,3)

        array = []
        for x in range(0,tarifnost):
            tarif = {
                "DatePok": "2018-11-01T00:00:00.000",
                "NomerTarifa": "{}".format(x+1),
                "NazvanieTarifa": "День",
                "PredPok": "{}".format(randint(100,9_999))
            }
            array.append(tarif)

        content = {
                "RowID": "1050194",
                "Tarifnost": tarifnost,
                "NomerUslugi": 100,
                "NazvanieUslugi": "Электроснабжение",
                "ZavodNomer": "{}".format(randint(10_000,99_999)),
                "Razradnost": "4",
                "KoefTrans": "1",
                "MaxPok": "3000",
                "result": "ЭЛ",
                "errorCode": "ЭЛ",
                "errorMessage": "ЭЛ",
                "ASKUE": "{}".format(randint(0,1)), # автомат или нет
                "DateCheck": "2018-11-01T00:00:00.000",
                "DateNextCheck": "2018-11-01T00:00:00.000",
                "NomerUslugiForBilling": "{}".format(randint(10_000,99_999)),
                "Tarif": array
            }

        return content

    def history(self, RowID=None):

        tarifnost = randint(1,3)
        date = (datetime.now() - timedelta(days=randint(20,30))).isoformat(timespec='milliseconds')

        array = []
        for x in range(0,tarifnost):
            tarif = {
                    "TARIF": x+1,
                    "NAZVTAR": "Ночь",
                    "POKAZANIE": randint(100,99_999),
                    "RASHOD": randint(100,99_999),
                    "RASHODRASPR": "0",
                    "SOSTOYANIE": "1",
                    "TIPVVODA": "Абонентское показание (интернет)"
            }
            array.append(tarif)

        content = {
            "DATA": date,
            "ZAVNOM": str(randint(10_000,99_999)),
            "NAZVANIEUSL": "Электроснабжение",
            "Tarifnost": tarifnost,
            "RowID": randint(10_000,99_999),
            "pokazaniya": array
        }

        return content


#-----------------------------------------------------------------------

if __name__ == '__main__':
    # print(Counter().counter())
    # print(Counter().history())
    pass

#-----------------------------------------------------------------------















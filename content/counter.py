#!/usr/bin/python3

from random import randint
from datetime import datetime, timedelta


class Counter(object):
    def __init__(self, ls=None):
        super(Counter, self).__init__()

        self.ls = ls

    def counter(self, codeInBilling=None):

        tarifnost = randint(1, 3)

        array = list()
        for x in range(0, tarifnost):
            tarif = {
                "DatePok": "2018-11-01T00:00:00.000",
                "NomerTarifa": x,
                "NazvanieTarifa": f'T{x+1}',
                "PredPok": str(randint(100, 9_999))
            }
            array.append(tarif)

        askue = randint(0, 1)

        content = {
            "RowID": str(randint(10_000, 99_999)),
            "Tarifnost": tarifnost,
            "NomerUslugi": 100,
            "NazvanieUslugi": "Электроснабжение",
            "ZavodNomer": f'ZN-{randint(10, 99)}-{randint(10_000, 99_999)}' + ' ASKUE' * askue,
            "Razradnost": "4",
            "KoefTrans": "1",
            "MaxPok": "3000",
            "result": "ЭЛ",
            "errorCode": "ЭЛ",
            "errorMessage": "ЭЛ",
            "ASKUE": str(askue),  # автомат или нет
            "DateCheck": "2018-11-01T00:00:00.000",
            "DateNextCheck": "2018-11-01T00:00:00.000",
            "NomerUslugiForBilling": str(randint(10_000, 99_999)),
            "Tarif": array
        }

        return content

    def history(self, RowID=None):

        tarifnost = randint(1, 3)
        date = datetime.now() - timedelta(days=randint(20, 30))

        array = list()
        for x in range(tarifnost):
            tarif = {
                "NomerTarifa": x,
                "NazvanieTarifa": f'T{x+1}',
                "POKAZANIE": str(randint(10, 99_999)),
                "RASHOD": str(randint(10, 99_999)),
                "RASHODRASPR": "0",
                "SOSTOYANIE": "1",
                "TIPVVODA": "Показание"
            }
            array.append(tarif)

        content = {
            "DATA": date.isoformat(timespec='milliseconds'),
            "ZavodNomer": f'ZN-{randint(10, 99)}-{randint(10_000, 99_999)}',
            "NazvanieUslugi": "Услуга",
            "Tarifnost": tarifnost,
            "RowID": RowID if not None else str(randint(100, 99_999)),
            "Rashod": randint(10, 99_999),
            "pokazaniya": array
        }

        return content

    def ascue(self, count, discretization, date):

        _count = None
        if discretization.lower() == 'h':
            _count = count if count < 23 else randint(0, 23)
        if discretization.lower() == 'd':
            _count = count if count < 29 else randint(0, 29)
        if discretization.lower() == 'm':
            _count = count if count < 12 else randint(0, 12)

        array = list()
        for x in range(_count):

            _date = None
            _max = None
            if discretization.lower() == 'h':
                _date = datetime.fromisoformat(date) + timedelta(hours=x)
                _max = 99
            if discretization.lower() == 'd':
                _date = datetime.fromisoformat(date) + timedelta(days=x)
                _max = 9900
            if discretization.lower() == 'm':
                _date = datetime.fromisoformat(date) + timedelta(days=31*x)
                _max = 99900

            content = {
                "date": _date.isoformat(timespec='milliseconds'),
                "value": randint(0, _max) / 100
            }
            array.append(content)

        return array


# -----------------------------------------------------------------------

if __name__ == '__main__':
    # print(Counter().counter())
    # print(Counter().history())
    # print(Counter().ascue(3,'d'))
    pass

# -----------------------------------------------------------------------

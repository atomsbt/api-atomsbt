#!/usr/bin/python3

# heroku logs -a api-atomsbt -t --source app

import os

from flask import Flask
from flask import request
from flask import jsonify as json

from random import choice
from random import randint
from time import sleep

from content.ls import LS

app = Flask(__name__)

#-----------------------------------------------------------------------

def request_logger(url, request):
    at = request.headers.get('token')

    json_headers = {
        'token': at
    }

    json_body = request.get_json()

    app.logger.info('REQUEST {0}\nHEADERS {1}\nBODY {2}'.format(url, json_headers, json_body))

#-----------------------------------------------------------------------

url_register = '/api/user/register/tel'
@app.route(url_register, methods=['POST'])
def register():

    request_logger(url_register, request)

    success = {
        "result": True,
        "message": "Код подтверждения отправлен на телефон"
    }

    error = {
        "result": False,
        "errorCode": 6010,
        "errorText": "Ошибка отправки СМС"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_confirm = '/api/user/confirm/tel'
@app.route(url_confirm, methods=['POST'])
def confirm():

    request_logger(url_confirm, request)

    success = {
        "result": True,
        "message": "Пользователь успешно зарегистрирован"
    }

    error = {
        "result": False,
        "errorCode": 5010,
        "errorText": "Пользователь с указанным логином уже зарегистрирован"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_reset = '/api/user/reset/tel'
@app.route(url_reset, methods=['POST'])
def reset():

    request_logger(url_reset, request)

    success = {
        "result": True,
        "message": "Новый пароль отправлен на телефон"
    }

    error = {
        "result": False,
        "errorCode": 401,
        "errorText": "Указаны неверные учетные данные"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_agreement = '/api/agreement'
@app.route(url_agreement, methods=['GET'])
def agreement():

    success = {
        "result": True,
        "link": "https://api-tver.atomsbt.ru/agreement.html"
    }

    error = {
        "result": False,
        "errorCode": 500,
        "errorText": "Нет нифига ссылки на сервере"
    }

    sleep(5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_auth = '/api/user/auth'
@app.route(url_auth, methods=['POST'])
def auth():

    request_logger(url_auth, request)

    success = {
        "result": True,
        "token": "312b9d11cae6a18ad78cfd34d6d39cfa"
    }

    error = {
        "result": False,
        "errorCode": 401,
        "errorText": "Указаны неверные учетные данные"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls = '/api/ls'
@app.route(url_ls, methods=['GET'])
def ls():

    ls_array = []
    ls_count = randint(0,5)
    for x in range(0,ls_count):
        ls_array.append(LS().object(True if x==0 else False))

    success = {
        "result": True,
        "data": ls_array
    }

    error = {
        "result": False,
        "errorCode": 401,
        "errorText": "Указаны неверные учетные данные"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls_option = '/api/ls/<option>'
@app.route(url_ls_option, methods=['GET', 'POST'])
def ls_option(option=None):

    success = None
    error = None

    request_logger(url_ls_option, request)

    if option == 'bind':

        success = {
            "result": True,
            "message": "Лицевой счет успешно привязан"
        }
        error = {
            "result": False,
            "errorCode": 7030,
            "errorText": "Введена некорректная сумма"
        }

    elif option == 'remove':

        success = {
            "result": True,
            "message": "Лицевой счет успешно отвязан"
        }
        error = {
            "result": False,
            "errorCode": 6070,
            "errorText": "Нет прав на данный лицевой счет"
        }

    else:

        success = {
            "result": True,
            "data": LS().details()
        }
        error = {
            "result": False,
            "errorCode": 6070,
            "errorText": "Нет прав на данный лицевой счет"
        }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls_services = '/api/ls/<ls>/services'
@app.route(url_ls_services, methods=['GET'])
def ls_services(ls=None):

    success = {
          "result": True,
          "data": [
                    {
                              "amount": 43216,
                              "amount_peni": 0,
                              "nds": 18,
                              "image_url": "https://via.placeholder.com/48x48",
                              "id": 1,
                              "codeInBilling": 100,
                              "is_active": True,
                              "name": "Электроэнергия",
                              "priority": 1,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": True,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 2,
                              "codeInBilling": 200,
                              "is_active": True,
                              "name": "Тепло",
                              "priority": 1,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": True,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 3,
                              "codeInBilling": 300,
                              "is_active": True,
                              "name": "Вода",
                              "priority": 1,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": True,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 10,
                              "codeInBilling": 1000,
                              "is_active": True,
                              "name": "Газоснабжение",
                              "priority": 1,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": True,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "https://via.placeholder.com/48x48",
                              "id": 4,
                              "codeInBilling": 400,
                              "is_active": True,
                              "name": "Жилищные услуги",
                              "priority": 2,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": False,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "https://via.placeholder.com/48x48",
                              "id": 5,
                              "codeInBilling": 500,
                              "is_active": True,
                              "name": "Техническое обслуживание",
                              "priority": 2,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": False,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 6,
                              "codeInBilling": 600,
                              "is_active": True,
                              "name": "Домофон",
                              "priority": 2,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": False,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 7,
                              "codeInBilling": 700,
                              "is_active": True,
                              "name": "Капитальный ремонт",
                              "priority": 2,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": False,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 8,
                              "codeInBilling": 800,
                              "is_active": True,
                              "name": "Вывоз ТКО",
                              "priority": 2,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": False,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 9,
                              "codeInBilling": 900,
                              "is_active": True,
                              "name": "Антена",
                              "priority": 2,
                              "type": "standart",
                              "params": {
                                        "services": True,
                                        "counters": False,
                                        "payments": True
                              }
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 11,
                              "codeInBilling": 1100,
                              "is_active": True,
                              "name": "Видеонаблюдение",
                              "priority": 1,
                              "type": "smart_home",
                              "params": {}
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 12,
                              "codeInBilling": 1200,
                              "is_active": True,
                              "name": "Система солнечного электроснабжения",
                              "priority": 1,
                              "type": "smart_home",
                              "params": {}
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "https://via.placeholder.com/48x48",
                              "id": 13,
                              "codeInBilling": 1300,
                              "is_active": True,
                              "name": "Система учета энергоресурсов",
                              "priority": 1,
                              "type": "smart_home",
                              "params": {}
                    },
                    {
                              "amount": 0,
                              "amount_peni": 0,
                              "nds": 0,
                              "image_url": "",
                              "id": 14,
                              "codeInBilling": 1400,
                              "is_active": True,
                              "name": "Аналитика",
                              "priority": 1,
                              "type": "smart_home",
                              "params": {}
                    }
            ]
    }

    error = {
        "result": False,
        "errorCode": 6070,
        "errorText": "Нет прав на данный лицевой счет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls_service_id = '/api/ls/<ls>/services/<id>'
@app.route(url_ls_service_id, methods=['GET'])
def ls_service_id(ls=None, id=None):

    success = {
        "result": True,
        "data": [
                    {
                              "id": "1",
                              "name": "Регистрация заявки на замену приборов учета",
                              "image_url": "https://via.placeholder.com/48x48",
                              "fields": [
                                        {
                                                  "id": "field1",
                                                  "name": "Регион",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный регион"
                                        },
                                        {
                                                  "id": "field2",
                                                  "name": "Населенный пункт",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный населенный пункт"
                                        },
                                        {
                                                  "id": "field3",
                                                  "name": "Улица",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная улица"
                                        },
                                        {
                                                  "id": "field4",
                                                  "name": "Дом",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный дом"
                                        },
                                        {
                                                  "id": "field5",
                                                  "name": "Корпус(строение)",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный корпус"
                                        },
                                        {
                                                  "id": "field6",
                                                  "name": "Квартира (комната)",
                                                  "type": "NUMERIC",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная квартира"
                                        },
                                        {
                                                  "id": "field7",
                                                  "name": "Фамилия",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная фамилия"
                                        },
                                        {
                                                  "id": "field8",
                                                  "name": "Имя",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное имя"
                                        },
                                        {
                                                  "id": "field9",
                                                  "name": "Отчество",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное отчество"
                                        },
                                        {
                                                  "id": "field10",
                                                  "name": "Лицевой счет",
                                                  "type": "NUMERIC",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный лс"
                                        },
                                        {
                                                  "id": "field11",
                                                  "name": "Контактный телефон",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный контактный телефон"
                                        },
                                        {
                                                  "id": "field12",
                                                  "name": "Электронная почта",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная почта"
                                        },
                                        {
                                                  "id": "field13",
                                                  "name": "Способ оплаты",
                                                  "type": "COMBOBOX",
                                                  "values": [
                                                            {
                                                                      "id": 1,
                                                                      "value": "Получить счёт"
                                                            },
                                                            {
                                                                      "id": 2,
                                                                      "value": "Оплатить онлайн"
                                                            },
                                                            {
                                                                      "id": 3,
                                                                      "value": "Оплатить в офисе"
                                                            }
                                                  ],
                                                  "value": 1
                                        },
                                        {
                                                  "id": "field14",
                                                  "name": "Счетчик",
                                                  "type": "COMBOBOX",
                                                  "values": [
                                                            {
                                                                      "id": 1,
                                                                      "value": "У меня свой счётчик"
                                                            },
                                                            {
                                                                      "id": 2,
                                                                      "value": "Однотарифный"
                                                            },
                                                            {
                                                                      "id": 3,
                                                                      "value": "Многотарифный"
                                                            },
                                                            {
                                                                      "id": 4,
                                                                      "value": "http://yandex.ru"
                                                            }
                                                  ],
                                                  "value": 1
                                        }
                              ]
                    },
                    {
                              "id": "2",
                              "name": "Повторный ввод в эксплуатацию прибора учёта",
                              "image_url": "",
                              "fields": [
                                        {
                                                  "id": "field1",
                                                  "name": "Регион",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный регион"
                                        },
                                        {
                                                  "id": "field2",
                                                  "name": "Населенный пункт",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный населенный пункт"
                                        },
                                        {
                                                  "id": "field3",
                                                  "name": "Улица",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная улица"
                                        },
                                        {
                                                  "id": "field4",
                                                  "name": "Дом",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный дом"
                                        },
                                        {
                                                  "id": "field5",
                                                  "name": "Корпус(строение)",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный корпус"
                                        },
                                        {
                                                  "id": "field6",
                                                  "name": "Квартира (комната)",
                                                  "type": "NUMERIC",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная квартира"
                                        },
                                        {
                                                  "id": "field7",
                                                  "name": "Фамилия",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная фамилия"
                                        },
                                        {
                                                  "id": "field8",
                                                  "name": "Имя",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное имя"
                                        },
                                        {
                                                  "id": "field9",
                                                  "name": "Отчество",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное отчество"
                                        },
                                        {
                                                  "id": "field10",
                                                  "name": "Лицевой счет",
                                                  "type": "NUMERIC",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный лс"
                                        },
                                        {
                                                  "id": "field11",
                                                  "name": "Контактный телефон",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный контактный телефон"
                                        },
                                        {
                                                  "id": "field12",
                                                  "name": "Электронная почта",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная почта"
                                        },
                                        {
                                                  "id": "field13",
                                                  "name": "Способ оплаты",
                                                  "type": "COMBOBOX",
                                                  "values": [
                                                            {
                                                                      "id": 1,
                                                                      "value": "Получить счёт"
                                                            },
                                                            {
                                                                      "id": 2,
                                                                      "value": "Оплатить онлайн"
                                                            },
                                                            {
                                                                      "id": 3,
                                                                      "value": "Оплатить в офисе"
                                                            }
                                                  ],
                                                  "value": 1
                                        },
                                        {
                                                  "id": "field14",
                                                  "name": "Счетчик",
                                                  "type": "COMBOBOX",
                                                  "values": [
                                                            {
                                                                      "id": 1,
                                                                      "value": "У меня свой счётчик"
                                                            },
                                                            {
                                                                      "id": 2,
                                                                      "value": "Однотарифный"
                                                            },
                                                            {
                                                                      "id": 3,
                                                                      "value": "Многотарифный"
                                                            },
                                                            {
                                                                      "id": 4,
                                                                      "value": "http://yandex.ru"
                                                            }
                                                  ],
                                                  "value": 1
                                        }
                              ]
                    },
                    {
                              "id": "3",
                              "name": "Страхование",
                              "image_url": "",
                              "fields": [
                                        {
                                                  "id": "field1",
                                                  "name": "Фамилия",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная фамилия"
                                        },
                                        {
                                                  "id": "field2",
                                                  "name": "Имя",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное имя"
                                        },
                                        {
                                                  "id": "field3",
                                                  "name": "Отчество",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное отчество"
                                        },
                                        {
                                                  "id": "field4",
                                                  "name": "Адрес (места страхования)",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный адрес"
                                        },
                                        {
                                                  "id": "field5",
                                                  "name": "Контактный телефон",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный контактный телефон"
                                        },
                                        {
                                                  "id": "field6",
                                                  "name": "Электронная почта",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная почта"
                                        },
                                        {
                                                  "id": "field17",
                                                  "name": "Паспортные данные",
                                                  "type": "PRINTED_TEXT"
                                        },
                                        {
                                                  "id": "field8",
                                                  "name": "Место рождения",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное место рождения"
                                        },
                                        {
                                                  "id": "field9",
                                                  "name": "Место регистрации",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное место регистрации"
                                        },
                                        {
                                                  "id": "field10",
                                                  "name": "Кем и когда выдан",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верно кем и когда выдан"
                                        },
                                        {
                                                  "id": "field11",
                                                  "name": "Код подразделения",
                                                  "type": "NUMERIC",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верно код подразделения"
                                        },
                                        {
                                                  "id": "field12",
                                                  "name": "Серия",
                                                  "type": "NUMERIC",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верно серия"
                                        },
                                        {
                                                  "id": "field13",
                                                  "name": "Номер",
                                                  "type": "NUMERIC",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верно номер"
                                        },
                                        {
                                                  "id": "field14",
                                                  "name": "Полюс",
                                                  "type": "COMBOBOX",
                                                  "values": [
                                                            {
                                                                      "id": 1,
                                                                      "value": "Домашний"
                                                            },
                                                            {
                                                                      "id": 2,
                                                                      "value": "Умный дом"
                                                            },
                                                            {
                                                                      "id": 3,
                                                                      "value": "Анти-клещ"
                                                            }
                                                  ],
                                                  "value": 1
                                        },
                                        {
                                                  "id": "field15",
                                                  "name": "Комментарий",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верно комментарий"
                                        }
                              ]
                    },
                    {
                              "id": "4",
                              "name": "Электролаборатория",
                              "image_url": "https://via.placeholder.com/48x48",
                              "fields": [
                                        {
                                                  "id": "field1",
                                                  "name": "Электролаборатория",
                                                  "type": "COMBOBOX",
                                                  "values": [
                                                            {
                                                                      "id": 1,
                                                                      "value": "лаб1"
                                                            },
                                                            {
                                                                      "id": 2,
                                                                      "value": "лаб2"
                                                            },
                                                            {
                                                                      "id": 3,
                                                                      "value": "лаб3"
                                                            }
                                                  ],
                                                  "value": 1
                                        },
                                        {
                                                  "id": "field2",
                                                  "name": "Адрес",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный адрес"
                                        },
                                        {
                                                  "id": "field3",
                                                  "name": "Фамилия",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная фамилия"
                                        },
                                        {
                                                  "id": "field4",
                                                  "name": "Имя",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное имя"
                                        },
                                        {
                                                  "id": "field5",
                                                  "name": "Отчество",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное отчество"
                                        },
                                        {
                                                  "id": "field6",
                                                  "name": "Контактный телефон",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный контактный телефон"
                                        },
                                        {
                                                  "id": "field7",
                                                  "name": "Электронная почта",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная почта"
                                        },
                                        {
                                                  "id": "field8",
                                                  "name": "Комментарий",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верно комментарий"
                                        }
                              ]
                    },
                    {
                              "id": "5",
                              "name": "Поверка измерительных комплексов",
                              "image_url": "",
                              "fields": [
                                        {
                                                  "id": "field1",
                                                  "name": "Адрес",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный адрес"
                                        },
                                        {
                                                  "id": "field2",
                                                  "name": "Фамилия",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная фамилия"
                                        },
                                        {
                                                  "id": "field3",
                                                  "name": "Имя",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное имя"
                                        },
                                        {
                                                  "id": "field4",
                                                  "name": "Отчество",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указано не верное отчество"
                                        },
                                        {
                                                  "id": "field5",
                                                  "name": "Контактный телефон",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный контактный телефон"
                                        },
                                        {
                                                  "id": "field6",
                                                  "name": "Электронная почта",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указана не верная почта"
                                        },
                                        {
                                                  "id": "field7",
                                                  "name": "Комментарий",
                                                  "type": "TEXT",
                                                  "regexp": None,
                                                  "error_msg": "Указан не верный комментарий"
                                        }
                              ]
                    }
        ]
    }

    error = {
        "result": False,
        "errorCode": 6070,
        "errorText": "Нет прав на данный лицевой счет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_services = '/api/user/services'
@app.route(url_services, methods=['POST'])
def services():

    request_logger(url_services, request)

    point = {
        "INDEKS": "215430",
        "ADDRESS": "Смоленская область п.Угра Новоселов 1",
        "TELEFON": [
            "+7 (4813) 74-1869"
        ],
        "EMAIL": "client@smolensk.atomsbt.ru",
        "REZHIM_RABOTY": [
            "пн - чт: с 09:00 по 18:00 Обед с 13:00 по 13:45",
            "пт: с 09:00 по 16:45 Обед с 13:00 по 13:45"
        ],
        "SHIROTA": 54.777993,
        "DOLGOTA": 34.319726
    }

    array = []
    for x in range(0, randint(0,10)):
        array.append(point)

    success = {
        "result": True,
        "data": array
    }

    error = {
        "result": False,
        "errorCode": 401,
        "errorText": "Указаны неверные учетные данные"
    }

    sleep(2)
    return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

#-----------------------------------------------------------------------
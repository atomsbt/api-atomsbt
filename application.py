#!/usr/bin/python3

"""

heroku logs -a api-atomsbt -t --source app


resorces
icons: https://cloudinary.com


"""

import os
import uuid

from flask import Flask
from flask import request
from flask import jsonify as json
from flask import render_template

from random import choice, random, randint
from time import sleep
from datetime import datetime, timedelta

from content.ls import LS
from content.service import Service, Form
from content.map import Map
from content.counter import Counter
from content.payment import Payment

app = Flask(__name__)

#-----------------------------------------------------------------------

def request_logger(url, request):

    jh = {'token': request.headers.get('token')}
    jb = request.get_json()

    body = '\nREQUEST {0}\nHEADERS {1}\nBODY {2}\n'.format(url, jh, jb)
    app.logger.info('\n'+'-'*80+body+'-'*80)

#-----------------------------------------------------------------------

url_user = '/api/user'
@app.route(url_user, methods=['GET'])
def request_user():

    success = {
        "result": True,
        "data": {
            "id": 23,
            "account_type_id": None,
            "billing_account_id": None,
            "account_login": "70000000004",
            "account_email": "test4@test.ru",
            "account_mphone": "70000000004",
            "account_password": "5f4dcc3b5aa765d61d8327deb882cf99",
            "account_status": None,
            "flag_sync": None,
            "remember_token": "b2ce18bf8089edf8d5872dc5bbb0bcec",
            "created_at": "2018-10-11T09:41:17.000",
            "updated_at": "2018-11-25T11:59:48.000",
            "account_pdn": None,
            "account_notify": None
        }
    }

    error = {
        "result": False,
        "errorCode": 6010,
        "errorText": "Ошибка"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_auth = '/api/user/auth'
@app.route(url_auth, methods=['POST'])
def request_auth():

    request_logger(url_auth, request)

    success = {
        "result": True,
        "token": str(uuid.uuid4().hex)
    }

    # error = {
    #     "result": False,
    #     "errorCode": 401,
    #     "errorText": "Указаны неверные учетные данные"
    # }

    sleep(0.5)
    return json(success), 200
    # return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_user_changeemail = '/api/user/changeemail'
@app.route(url_user_changeemail, methods=['POST'])
def request_url_user_changeemail():

    request_logger(url_user_changeemail, request)

    success = {
        "result": True,
        "message": "Емаил изменен"
    }
    error = {
        "result": False,
        "errorCode": 7030,
        "errorText": "Введена некорректная данные"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_user_changepassword = '/api/user/changepassword'
@app.route(url_user_changepassword, methods=['POST'])
def request_url_user_changepassword():

    request_logger(url_user_changepassword, request)

    success = {
        "result": True,
        "message": "Пароль изменен"
    }
    error = {
        "result": False,
        "errorCode": 7030,
        "errorText": "Введена некорректная данные"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_user_tel_change = '/api/user/tel/change'
@app.route(url_user_tel_change, methods=['POST'])
def request_url_user_tel_change():

    request_logger(url_user_tel_change, request)

    success = {
        "result": True,
        "message": "Код подтверждения отправлен на телефон"
    }
    error = {
        "result": False,
        "errorCode": 7030,
        "errorText": "Введена некорректная"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_user_tel_change_confirm = '/api/user/tel/change/confirm'
@app.route(url_user_tel_change_confirm, methods=['POST'])
def request_url_user_tel_change_confirm():

    request_logger(url_user_tel_change_confirm, request)

    success = {
        "result": True,
        "message": "Телефон изменен"
    }
    error = {
        "result": False,
        "errorCode": 7030,
        "errorText": "Введена некорректная"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_register = '/api/user/register/tel'
@app.route(url_register, methods=['POST'])
def request_url_register():

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
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_confirm = '/api/user/confirm/tel'
@app.route(url_confirm, methods=['POST'])
def request_confirm():

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
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_reset = '/api/user/reset/tel'
@app.route(url_reset, methods=['POST'])
def request_reset():

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
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_agreement = '/api/agreement'
@app.route(url_agreement, methods=['GET'])
def request_url_agreement():

    success = {
        "result": True,
        "link": "https://api-atomsbt.herokuapp.com/policy"
    }

    error = {
        "result": False,
        "errorCode": 500,
        "errorText": "Нет нифига ссылки на сервере"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls = '/api/ls'
@app.route(url_ls, methods=['GET'])
def request_ls():

    ls_min = 1
    ls_array = []
    for i in range(ls_min,randint(ls_min,5)):
        ls_array.append(LS().object(True if i == ls_min else False))

    success = {
        "result": True,
        "data": ls_array
    }

    # error = {
    #     "result": False,
    #     "errorCode": 401,
    #     "errorText": "Указаны неверные учетные данные"
    # }

    sleep(0.5)
    return json(success), 200
    # return (json(success), 200) if randint(0,5) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls_option = '/api/ls/<option>'
@app.route(url_ls_option, methods=['GET', 'POST'])
def request_ls_option(option=None):

    success = None
    error = None

    request_logger(url_ls_option, request)

    if option == 'change':

        success = {
            "result": True,
            "message": "Основной лицевой счет изменен"
        }
        error = {
            "result": False,
            "errorCode": 7030,
            "errorText": "Введена некорректная сумма"
        }

    elif option == 'bind':

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
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls_services = '/api/ls/<ls>/services'
@app.route(url_ls_services, methods=['GET'])
def request_url_ls_services(ls=None):

    standart = [
        {
            'name': "Электроэнергия",
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543782462/atom/services/El.png'
        },
        {
            'name': "Тепло",
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543783046/atom/services/Te.png'
        },
        {
            'name': "Вода",
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543783673/atom/services/Vd.png'
        },
        {
            'name': "Газоснабжение",
            'image_url': None
        },
        {
            'name': "Жилищные услуги",
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543783767/atom/services/Hm.png'
        },
        {
            'name': "Техническое обслуживание",
            'image_url': None
        },
        {
            'name': "Домофон",
            'image_url': None
        },
        {
            'name': "Капитальный ремонт",
            'image_url': None
        },
        {
            'name': "Вывоз ТКО",
            'image_url': None
        },
        {
            'name': "Антена",
            'image_url': None
        }
    ]

    smart_home = [
        {
            'name': "Видеонаблюдение",
            'codeInBilling': 1100,
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543788073/atom/services/Vn.png'
        },
        {
            'name': "Система солнечного электроснабжения",
            "codeInBilling": 1200,
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543788096/atom/services/Ss.png'
        },
        {
            'name': "Система учета энергоресурсов",
            "codeInBilling": 1300,
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543788085/atom/services/Su.png'
        },
        {
            'name': "Аналитика",
            "codeInBilling": 1400,
            'image_url': 'https://res.cloudinary.com/dlr1k3h7l/image/upload/c_scale,w_48/v1543788066/atom/services/An.png'
        }
    ]

    array = []
    for x in range(0, randint(0,len(standart))):
        name = standart[x].get('name')
        image = standart[x].get('image_url')
        array.append(Service().element(name, 'standart', True, image, None))

    for x in range(0, randint(0,len(smart_home))):
        name = smart_home[x].get('name')
        image = smart_home[x].get('image_url')
        codeInBilling = smart_home[x].get('codeInBilling')
        array.append(Service().element(name, 'smart_home', False, image, codeInBilling))

    success = {
          "result": True,
          "data": array
    }

    error = {
        "result": False,
        "errorCode": 6070,
        "errorText": "Нет прав на данный лицевой счет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_counters = '/api/ls/<ls>/counters/list/<codeInBilling>'
@app.route(url_counters, methods=['GET'])
def request_ls_counters(ls=None, codeInBilling=None):

    array = []
    for _ in range(1,randint(1,5)):
        array.append(Counter(ls=ls).counter(codeInBilling=codeInBilling))

    dn = datetime.now()
    ot = dn - timedelta(days=15)
    do = (dn - timedelta(days=3)) if randint(0,1)>0 else (dn + timedelta(days=3))

    success = {
        "result": True,
        "data": array,
        "PeriodSch": {
            "ot": ot.isoformat(timespec='milliseconds'),
            "do": do.isoformat(timespec='milliseconds')
        }
    }

    error = {
        "result": False,
        "errorCode": 401,
        "errorText": "Указаны неверные учетные данные"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_counters_add = '/api/ls/counters/add'
@app.route(url_counters_add, methods=['POST'])
def request_counters_add():

    request_logger(url_counters_add, request)

    success = {
        "result": True,
        "message": "Данные успешно поданы"
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату платежей нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_counters_history = '/api/ls/counters/history'
@app.route(url_counters_history, methods=['POST'])
def request_counters_history():

    request_logger(url_counters_history, request)

    array = []
    for _ in range(0,randint(0,15)):
        array.append(Counter().history())

    success = {
        "page": 1,
        "pages": 1,
        "rowPerPage": 100,
        "totalRowsCount": 100,
        "result": True,
        "data": array
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату платежей нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ls_service_id = '/api/ls/<ls>/services/<id>'
@app.route(url_ls_service_id, methods=['GET'])
def request_url_ls_service_id(ls=None, id=None):

    array = []
    for x in range(0, randint(0,15)):
        array.append(Form().form('Форма с номером {}'.format(x), randint(3,10)))

    success = {
        "result": True,
        "data": array
    }

    error = {
        "result": False,
        "errorCode": 6070,
        "errorText": "Нет прав на данный лицевой счет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_send_form = '/api/user/send/form'
@app.route(url_send_form, methods=['POST'])
def request_send_form():

    request_logger(url_send_form, request)

    success = {
        "result": True,
        "message": "Данные приняты сервером"
    }

    error = {
        "result": False,
        "errorCode": 6020,
        "errorText": "Ошибка отправки"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_payments = '/api/ls/payments'
@app.route(url_payments, methods=['POST'])
def request_payments():

    request_logger(url_payments, request)

    array = []
    for _ in range(0,randint(0,15)):
        array.append(Payment().payment())

    success = {
        "page": 1,
        "pages": 1,
        "rowPerPage": 100,
        "totalRowsCount": 100,
        "result": True,
        "data": array
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату платежей нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_checks = '/api/ls/<ls>/checks/<tranzakciya>'
@app.route(url_checks, methods=['GET'])
def request_checks(ls=None, tranzakciya=None):

    success = {
        "result": True,
        "data": Payment().check()
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату платежей нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_getpaygateway = '/api/ls/<ls>/pay/getpaygateway'
@app.route(url_getpaygateway, methods=['GET'])
def request_url_getpaygateway(ls=None):

    array = []
    for _ in range(1,randint(1,5)):
        rnd = randint(10_000,99_999)
        pay_gateway = {
            "code": "BN{}".format(rnd),
            "name": "Банк {}".format(rnd)
        }
        array.append(pay_gateway)

    success = {
        "result": True,
        "pay_gateways": array,
        "usls_enabled": False if randint(0,3) != 3 else True
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату платежей нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)


url_getlink = '/api/pay/getlink'
@app.route(url_getlink, methods=['POST'])
def request_getlink():

    request_logger(url_getlink, request)

    success = {
        "result": True,
        "link": "https://api-atomsbt.herokuapp.com/pay"
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату платежей нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_kvtMonths = '/api/ls/<ls>/reports/kvtMonths'
@app.route(url_kvtMonths, methods=['GET'])
def request_url_kvtMonths(ls=None):

    array = []
    for i in range(1, randint(1,15)):
        date = datetime.now() - timedelta(days=31*i)
        array.append(date.isoformat(timespec='milliseconds'))

    success = {
        "result": True,
        "data": array
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату ничего нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

url_reports = '/api/ls/reports/<option>'
@app.route(url_reports, methods=['POST'])
def request_url_reports(option=None):

    request_logger(url_reports, request)

    success = {
        "result": True,
        "url": "https://static.tinkoff.ru/documents/docs/terms_of_integrated_banking_services.pdf"
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату ничего нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_services = '/api/user/services'
@app.route(url_services, methods=['POST'])
def request_url_services():

    request_logger(url_services, request)

    lon = request.get_json()['longitude']
    lat = request.get_json()['latitude']
    dis = request.get_json()['distance']

    success = {
        "result": True,
        "data": Map().places(float(lon), float(lat), float(dis))
    }

    error = {
          "result": False,
          "errorCode": 9090,
          "errorText": "Центры обслуживания в указанном радиусе не найдены"
    }

    sleep(1)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_getInstallation = '/api/ls/<ls>/victronenergy/getInstallation'
@app.route(url_getInstallation, methods=['GET'])
def request_url_getInstallation(ls=None):

    success = {
        "result": True,
        "OV1": "232.9 VAC" if randint(0,3)>1 else None,
        "OV2": "22.3 VAC" if randint(0,3)>1 else None,
        "OV3": "5 VAC" if randint(0,3)>1 else None,
        "bs": "84.5 %",
        "solar_yield": "140 W"
    }

    error = {
          "result": False,
          "errorCode": 9090,
          "errorText": "Центры обслуживания в указанном радиусе не найдены"
    }

    sleep(1)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_camera = '/api/ls/<ls>/camera'
@app.route(url_camera, methods=['GET'])
def request_url_camera(ls=None):

    success = {
        "result": True,
        "data": [
            {
                "place": "КУХНЯ",
                "link": "rtsp//admin12345@84.42.31.48/00"
            },
            {
                "place": "ПОДЪЕЗД",
                "link": "rtsp//admin12345@84.42.31.48/10"
            },
            {
                "place": "ДВОР",
                "link": "rtsp//admin12345@84.42.31.48/20"
            }
        ]
    }

    error = {
        "result": False,
        "errorCode": 9040,
        "errorText": "Нет камер"
    }

    sleep(1)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_ontime = '/api/ls/counter/ontime'
@app.route(url_ontime, methods=['POST'])
def request_url_ontime():

    request_logger(url_ontime, request)

    disc = request.get_json().get('discretization')

    success = {
        "result": True,
        "data": Counter().ascue(randint(1,24), disc)
    }

    error = {
          "result": False,
          "errorCode": 9090,
          "errorText": "Центры обслуживания в указанном радиусе не найдены"
    }

    sleep(1)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_analytics = '/api/ls/analytics'
@app.route(url_analytics, methods=['POST'])
def request_url_analytics():

    request_logger(url_analytics, request)
    current = choice((True, False))

    success = {
        "result": True,
        "data": [        
            {
                "Current": current,
                "Tarif": "1",
                "sum": randint(11100,999900)
            },
            {
                "Current": not current,
                "Tarif": "2",
                "sum": randint(11100,999900)
            }
        ]
    }

    error = {
          "result": False,
          "errorCode": 10040,
          "errorText": "Ошибка при аналитике"
    }

    sleep(1)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

url_feedback = '/api/user/feedback'
@app.route(url_feedback, methods=['POST'])
def request_feedback():

    request_logger(url_feedback, request)

    success = {
        "result": True,
        "message": "Регистрация обращения выполнена"
    }

    error = {
        "result": False,
        "errorCode": 10050,
        "errorText": "За указанную дату платежей нет"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0,10) != 5 else (json(error), 500)

#-----------------------------------------------------------------------

@app.route("/<option>")
def main(option=None):

    template = 'index.html'

    if option == 'pay':
        template = 'pay.html'
    if option == 'policy':
        template = 'policy.html'

    return render_template(template)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

#-----------------------------------------------------------------------
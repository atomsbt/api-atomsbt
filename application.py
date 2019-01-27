#!/usr/bin/python3

"""

heroku logs -a api-atomsbt -t --source app


resorces
icons: https://cloudinary.com


"""

import os
import uuid
import logging

from flask import Flask, request, render_template
from flask import jsonify as json

from random import choice, random, randint
from time import sleep
from datetime import datetime, timedelta

from content.ls import LS
from content.service import Service, Form
from content.map import Map
from content.counter import Counter
from content.payment import Payment

from adapters.dbconnector import AtomDB

app = Flask(__name__)

# -----------------------------------------------------------------------


@app.after_request
def after_request(response):

    if request.method == 'POST':
        req = f'\nREQUEST {request.method} {request.path}'
        hed = '\nHEADERS {}'.format({"token": request.headers.get("token")})
        bod = f'\nBODY {request.get_json()}\n'
        message = '-'*80+req+hed+bod+'-'*80
        print(message)

    return response


def error(errorCode):

    sql = """
        SELECT error_code, error_text 
        FROM atom_errors
        WHERE error_code = {}   
    """
    ex = AtomDB().execute(sql.format(errorCode))

    error = {
        "result": False,
        "errorCode": ex[0].get('error_code') if len(ex) > 0 else 0,
        "errorText": ex[0].get('error_text') if len(ex) > 0 else None,
    }
    return json(error)

# -----------------------------------------------------------------------


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

    sleep(1)
    return (json(success), 200) if randint(0, 20) != 5 else (error(4020), 500)

# -----------------------------------------------------------------------


url_auth = '/api/user/auth'


@app.route(url_auth, methods=['POST'])
def request_auth():

    success = {
        "result": True,
        "token": str(uuid.uuid4().hex)
    }

    sleep(1)
    return (json(success), 200) if randint(0, 20) != 5 else (error(401), 500)

# -----------------------------------------------------------------------


url_user_changeemail = '/api/user/changeemail'


@app.route(url_user_changeemail, methods=['POST'])
def request_url_user_changeemail():

    success = {
        "result": True,
        "message": "Емаил изменен"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5070), 500)

# -----------------------------------------------------------------------


url_user_changepassword = '/api/user/changepassword'


@app.route(url_user_changepassword, methods=['POST'])
def request_url_user_changepassword():

    success = {
        "result": True,
        "message": "Пароль изменен"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(4050), 500)

# -----------------------------------------------------------------------


url_user_tel_change = '/api/user/tel/change'


@app.route(url_user_tel_change, methods=['POST'])
def request_url_user_tel_change():

    success = {
        "result": True,
        "message": "Код подтверждения отправлен на телефон"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5010), 500)

# -----------------------------------------------------------------------


url_user_tel_change_confirm = '/api/user/tel/change/confirm'


@app.route(url_user_tel_change_confirm, methods=['POST'])
def request_url_user_tel_change_confirm():

    success = {
        "result": True,
        "message": "Телефон изменен"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)

# -----------------------------------------------------------------------


url_register = '/api/user/register/tel'


@app.route(url_register, methods=['POST'])
def request_url_register():

    success = {
        "result": True,
        "message": "Код подтверждения отправлен на телефон"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 20) != 5 else (error(6010), 500)

# -----------------------------------------------------------------------


url_confirm = '/api/user/confirm/tel'


@app.route(url_confirm, methods=['POST'])
def request_confirm():

    success = {
        "result": True,
        "message": "Пользователь успешно зарегистрирован"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 20) != 5 else (error(5010), 500)

# -----------------------------------------------------------------------


url_reset = '/api/user/reset/tel'


@app.route(url_reset, methods=['POST'])
def request_reset():

    success = {
        "result": True,
        "message": "Новый пароль отправлен на телефон"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0, 10) != 5 else (error(401), 500)

# -----------------------------------------------------------------------


url_agreement = '/api/agreement'


@app.route(url_agreement, methods=['GET'])
def request_url_agreement():

    success = {
        "result": True,
        "link": "https://api-atomsbt.herokuapp.com/policy"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0, 10) != 5 else (error(500), 500)

# -----------------------------------------------------------------------


url_ls = '/api/ls'


@app.route(url_ls, methods=['GET'])
def request_url_ls():

    array = []
    for i in range(randint(1, 8)):
        array.append(LS().object(1 if i == 0 else 0))

    success = {
        "result": True,
        "data": array
    }

    sleep(1)
    return (json(success), 200) if randint(0, 20) != 5 else (error(7050), 500)

# -----------------------------------------------------------------------


url_ls_option = '/api/ls/<option>'


@app.route(url_ls_option, methods=['GET', 'POST'])
def request_ls_option(option=None):

    success = None
    if option in ['change', 'bind', 'remove']:
        success = {
            "result": True,
            "message": "Основной лицевой счет изменен"
        }
    else:
        success = {
            "result": True,
            "data": LS().details(option)
        }

    sleep(1)
    return (json(success), 200) if randint(0, 20) != 5 else (error(7080), 500)

# -----------------------------------------------------------------------


url_ls_services = '/api/ls/<ls>/services'


@app.route(url_ls_services, methods=['GET'])
def request_url_ls_services(ls=None):

    sql = """
        SELECT id, name, image_url, type, code_in_billing 
        FROM atom_services
        WHERE type LIKE '{}'
        ORDER BY id ASC    
    """

    array = []
    standart = AtomDB().execute(sql.format('standart'))
    for x in range(randint(0, len(standart))):
        name = standart[x].get('name')
        image = standart[x].get('image_url')
        array.append(Service().element(name, 'standart', True, image, None))

    smart_home = AtomDB().execute(sql.format('smart_home'))
    for x in range(len(smart_home)):
        name = smart_home[x].get('name')
        image = smart_home[x].get('image_url')
        billing = smart_home[x].get('code_in_billing')
        array.append(Service().element(
            name, 'smart_home', True, image, billing))

    success = {
        "result": True,
        "data": array
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(9050), 500)

# -----------------------------------------------------------------------


url_counters = '/api/ls/<ls>/counters/list/<codeInBilling>'


@app.route(url_counters, methods=['GET'])
def request_ls_counters(ls=None, codeInBilling=None):

    array = []
    for _ in range(randint(1, 5)):
        array.append(Counter(ls=ls).counter(codeInBilling=codeInBilling))

    dn = datetime.now()
    ot = dn - timedelta(days=15)
    do = (dn - timedelta(days=3)) if randint(0,
                                             1) > 0 else (dn + timedelta(days=3))

    success = {
        "result": True,
        "data": array,
        "PeriodSch": {
            "ot": ot.isoformat(timespec='milliseconds'),
            "do": do.isoformat(timespec='milliseconds')
        }
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(6060), 500)

# -----------------------------------------------------------------------


url_counters_option = '/api/ls/counters/<option>'


@app.route(url_counters_option, methods=['POST'])
def request_counters_option(option):

    success = {}
    err = None

    if option == 'add':
        success = {
            "result": True,
            "message": "Данные успешно поданы"
        }
        err = error(6050)

    if option == 'history':
        array = []
        for _ in range(randint(1, 15)):
            array.append(Counter().history())

        success = {
            "page": 1,
            "pages": 1,
            "rowPerPage": 100,
            "totalRowsCount": 100,
            "result": True,
            "data": array
        }
        err = error(7010)

    sleep(1)
    return (json(success), 200) if randint(0, 20) != 5 else (err, 500)

# -----------------------------------------------------------------------


url_ls_service_id = '/api/ls/<ls>/services/<id>'


@app.route(url_ls_service_id, methods=['GET'])
def request_url_ls_service_id(ls=None, id=None):

    sql = """
        SELECT name, image_url
        FROM atom_forms    
    """

    array = []
    dbarr = AtomDB().execute(sql)
    for x in range(randint(0, len(dbarr))):
        name = dbarr[x].get('name')
        image = dbarr[x].get('image_url')
        array.append(Form().form(name, image, randint(3, 10)))

    for x in range(randint(0, 15)):
        array.append(Form().form(
            'Форма с номером {}'.format(x), None, randint(3, 10)))

    success = {
        "result": True,
        "data": array
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(9050), 500)

# -----------------------------------------------------------------------


url_send_form = '/api/user/send/form'


@app.route(url_send_form, methods=['POST'])
def request_send_form():

    success = {
        "result": True,
        "message": "Данные приняты сервером"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5090), 500)

# -----------------------------------------------------------------------


url_payments = '/api/ls/payments'


@app.route(url_payments, methods=['POST'])
def request_payments():

    array = []
    for _ in range(randint(0, 15)):
        array.append(Payment().payment())

    success = {
        "page": 1,
        "pages": 1,
        "rowPerPage": 100,
        "totalRowsCount": 100,
        "result": True,
        "data": array
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(10050), 500)

# -----------------------------------------------------------------------


url_checks = '/api/ls/<ls>/checks/<tranzakciya>'


@app.route(url_checks, methods=['GET'])
def request_checks(ls=None, tranzakciya=None):

    success = {
        "result": True,
        "data": Payment().check()
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(9030), 500)

# -----------------------------------------------------------------------


url_getpaygateway = '/api/ls/<ls>/pay/getpaygateway'


@app.route(url_getpaygateway, methods=['GET'])
def request_url_getpaygateway(ls=None):

    array = []
    for _ in range(randint(1, 5)):
        rnd = randint(10_000, 99_999)
        pay_gateway = {
            "code": "BN{}".format(rnd),
            "name": "Банк {}".format(rnd)
        }
        array.append(pay_gateway)

    success = {
        "result": True,
        "pay_gateways": array,
        "usls_enabled": False if randint(0, 3) != 3 else True
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


url_getlink = '/api/pay/getlink'


@app.route(url_getlink, methods=['POST'])
def request_getlink():

    success = {
        "result": True,
        "link": "https://api-atomsbt.herokuapp.com/pay"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)

# -----------------------------------------------------------------------


url_kvtMonths = '/api/ls/<ls>/reports/kvtMonths'


@app.route(url_kvtMonths, methods=['GET'])
def request_url_kvtMonths(ls=None):

    array = []
    for i in range(randint(1, 15)):
        date = datetime.now() - timedelta(days=31*i)
        array.append(date.isoformat(timespec='milliseconds'))

    success = {
        "result": True,
        "data": array
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


url_reports = '/api/ls/reports/<option>'


@app.route(url_reports, methods=['POST'])
def request_url_reports(option=None):

    success = {
        "result": True,
        "url": "https://static.tinkoff.ru/documents/docs/terms_of_integrated_banking_services.pdf"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)

# -----------------------------------------------------------------------


url_services = '/api/user/services'


@app.route(url_services, methods=['POST'])
def request_url_services():

    lon = request.get_json()['longitude']
    lat = request.get_json()['latitude']
    dis = request.get_json()['distance']

    success = {
        "result": True,
        "data": Map().places(float(lon), float(lat), float(dis))
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)

# -----------------------------------------------------------------------


url_getInstallation = '/api/ls/<ls>/victronenergy/getInstallation'


@app.route(url_getInstallation, methods=['GET'])
def request_url_getInstallation(ls=None):

    success = {
        "result": True,
        "OV1": "232.9 VAC" if randint(0, 3) > 1 else None,
        "OV2": "22.3 VAC" if randint(0, 3) > 1 else None,
        "OV3": "5 VAC" if randint(0, 3) > 1 else None,
        "bs": "84.5 %",
        "solar_yield": "140 W"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)

# -----------------------------------------------------------------------


url_camera = '/api/ls/<ls>/camera'


@app.route(url_camera, methods=['GET'])
def request_url_camera(ls=None):

    sql = """
        SELECT name, video_url
        FROM atom_video
    """

    array = []
    dbarr = AtomDB().execute(sql)
    if len(dbarr) > 0:
        for x in range(len(dbarr)):
            item = {
                "link": dbarr[x].get('video_url'),
                "place": dbarr[x].get('name')
            }
            array.append(item)

    success = {
        "result": True,
        "data": array
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(9040), 500)

# -----------------------------------------------------------------------


url_ontime = '/api/ls/counter/ontime'


@app.route(url_ontime, methods=['POST'])
def request_url_ontime():

    disc = request.get_json().get('discretization')
    date = request.get_json().get('startdate')

    success = {
        "result": True,
        "data": Counter().ascue(randint(0, 30), disc, date)
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(6080), 500)

# -----------------------------------------------------------------------


url_analytics = '/api/ls/analytics'


@app.route(url_analytics, methods=['POST'])
def request_url_analytics():

    current = choice((True, False))

    success = {
        "result": True,
        "data": [
            {
                "Current": current,
                "Tarif": "1",
                "sum": randint(11100, 999900)
            },
            {
                "Current": not current,
                "Tarif": "2",
                "sum": randint(11100, 999900)
            }
        ]
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(10040), 500)

# -----------------------------------------------------------------------


url_askue = '/api/ls/counter/last'


@app.route(url_askue, methods=['POST'])
def request_url_askue():

    success = {
        "result": True,
        "NAPRYAZHENIE": "220 В",
        "SILATOKA": "0.3 А"
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(10080), 500)

# -----------------------------------------------------------------------


url_getWeatherToLS = '/api/ls/<option>/getWeatherToLS'


@app.route(url_getWeatherToLS, methods=['GET'])
def request_url_getWeatherToLS(option):

    icon = choice([
        "bkn_-sn_n", "bkn_+ra_d", "bkn_+ra_n", "bkn_+sn_d", "bkn_+sn_n",
        "bkn_d", "bkn_n", "bkn_ra_d", "bkn_ra_n", "bkn_sn_d", "bkn_sn_n",
        "bl-", "bl", "fct_-ra", "fct_-sn", "fct_+ra", "fct_+sn", "fct_ra_sn",
        "fct_ra", "fct_sn_dwn", "fct_sn_rs", "fct_sn",
        "fg_d", "fg_n", "ovc_-ra", "ovc_-sn", "ovc_+ra", "ovc_+sn", "ovc_gr",
        "ovc_ra_sn", "ovc_ra", "ovc_sn", "ovc_ts_gr", "ovc_ts_ra", "ovc_ts",
        "ovc", "skc_d", "skc_n"
    ])

    success = {
        "result": True,
        "data": {
            "temp": str(randint(-40, 40)),
            "icon": f"https://yastatic.net/weather/i/icons/blueye/color/svg/{icon}.svg"
        }
    }

    sleep(1)
    return (json(success), 200) if randint(0, 10) != 5 else (error(10080), 500)

# -----------------------------------------------------------------------


url_feedback = '/api/user/feedback'


@app.route(url_feedback, methods=['POST'])
def request_feedback():

    success = {
        "result": True,
        "message": "Регистрация обращения выполнена"
    }

    sleep(0.5)
    return (json(success), 200) if randint(0, 10) != 5 else (error(6020), 500)


url_getTheme = '/api/ls/<option>/getTheme'


@app.route(url_getTheme, methods=['GET'])
def request_url_getTheme(option):

    array = list()
    for i in range(randint(1, 20)):
        item = {
            "theme": f'theme {i}'+choice([' тестовый текст для проверки 2х строчной выпадалки', '']),
            "description": choice(["test", None, ""]),
            "id": f'{i}'
        }
        array.append(item)

    success = {
        "result": True,
        "data": array
    }

    sleep(0.5)
    return (json(success), 200) if randint(0, 10) != 5 else (error(6020), 500)

# -----------------------------------------------------------------------


url_push_chenge = '/api/devices/<option>'


@app.route(url_push_chenge, methods=['POST'])
def request_url_push_chenge(option=None):

    success = {
        "result": True
    }

    sleep(0.5)
    return (json(success), 200) if randint(0, 10) != 5 else (error(10020), 500)

# -----------------------------------------------------------------------


@app.route("/")
@app.route("/<option>")
def main(option='index'):

    temp = f'{option}.html'
    return render_template(temp)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# -----------------------------------------------------------------------

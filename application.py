#!/usr/bin/python3

#mock: heroku logs -a api-atomsbt -t --source app
#icons: https://cloudinary.com
#doc: http://git.stack-it.ru/web/api.atomsbt.ru/blob/maste/CONTRIBUTING.md

import os
import uuid

from flask import Flask, request, render_template, send_from_directory
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

    req = f'REQUEST {request.method} {request.path}'
    hed = 'HEADERS {}'.format({"token": request.headers.get("token")})

    bod = str()
    if request.method == 'POST':
        bod = f'BODY {request.get_json()}'
    else:
        bod = f'BODY {response.get_json()}'
    message = req + '\n' + hed + '\n' + bod
    print(message)

    sleep(1)
    return response


def error(errorCode):

    sql = """
        SELECT error_code, error_text 
        FROM atom_errors
        WHERE error_code = {}
    """.format(errorCode)
    ex = AtomDB().execute(sql)

    path = f'\n\n-> {request.method} {request.path}'
    error = {
        "result": False,
        "errorCode": ex[0].get('error_code') if len(ex) > 0 else 0,
        "errorText": f'{ex[0].get("error_text")}{path}' if len(ex) > 0 else None,
    }
    return json(error)

# -----------------------------------------------------------------------


@app.route('/api/user', methods=['GET'])
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

    return (json(success), 200) if randint(0, 20) != 5 else (error(4020), 500)


@app.route('/api/user/auth', methods=['POST'])
def request_auth():
    # {
    #     "login": "79000000009",
    #     "password": "password"
    # }

    login = request.get_json().get('login')
    sql = f"""
        SELECT login, token 
        FROM atom_users
        WHERE login LIKE '{login}'"""
    user = AtomDB().execute_first(sql)

    success = {
        "result": True,
        "token": user.get('token') if user is not None else str(uuid.uuid4().hex)
    }

    return (json(success), 200) if randint(0, 20) != 5 else (error(401), 500)


@app.route('/api/user/changeemail', methods=['POST'])
def request_url_user_changeemail():

    success = {
        "result": True,
        "message": "Емаил изменен"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5070), 500)


@app.route('/api/user/changepassword', methods=['POST'])
def request_url_user_changepassword():

    success = {
        "result": True,
        "message": "Пароль изменен"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(4050), 500)


@app.route('/api/user/tel/change', methods=['POST'])
def request_url_user_tel_change():

    success = {
        "result": True,
        "message": "Код подтверждения отправлен на телефон"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5010), 500)


@app.route('/api/user/tel/change/confirm', methods=['POST'])
def request_url_user_tel_change_confirm():

    success = {
        "result": True,
        "message": "Телефон изменен"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


@app.route('/api/user/register/tel', methods=['POST'])
def request_url_register():

    success = {
        "result": True,
        "message": "Код подтверждения отправлен на телефон"
    }

    return (json(success), 200) if randint(0, 20) != 5 else (error(6010), 500)


@app.route('/api/user/confirm/tel', methods=['POST'])
def request_confirm():

    success = {
        "result": True,
        "message": "Пользователь успешно зарегистрирован"
    }

    return (json(success), 200) if randint(0, 20) != 5 else (error(5010), 500)


@app.route('/api/user/reset/tel', methods=['POST'])
def request_reset():

    success = {
        "result": True,
        "message": "Новый пароль отправлен на телефон"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(401), 500)


@app.route('/api/agreement', methods=['GET'])
def request_url_agreement():

    success = {
        "result": True,
        "link": "https://api-atomsbt.herokuapp.com/policy"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(500), 500)

@app.route('/api/market', methods=['GET'])
def request_url_market():

    success = {
        "result": True,
        "enable": choice([True, False]),
        "link": "https://api-atomsbt.herokuapp.com/index"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(500), 500)


@app.route('/api/ls', methods=['GET'])
def request_url_ls():

    token = request.headers.get('token')
    if token in ['', None]:
        return (error(4010), 500)

    sql = f"""
        SELECT login, ls 
        FROM atom_users
        WHERE token LIKE '{token}'"""
    ls = AtomDB().execute_first(sql)

    array = list()
    for i in range(len(ls.get('ls')) if ls is not None else randint(1, 8)):
        array.append(LS().object(1 if i == 0 else 0))

    success = {
        "result": True,
        "data": array
    }

    return (json(success), 200) if randint(0, 20) != 5 else (error(7050), 500)


@app.route('/api/ls/<option>', methods=['GET', 'POST'])
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

    return (json(success), 200) if randint(0, 20) != 5 else (error(7080), 500)


@app.route('/api/ls/<ls>/services', methods=['GET'])
def request_url_ls_services(ls=None):

    sql = """
        SELECT id, name, image_url, type, code_in_billing 
        FROM atom_services
        WHERE type LIKE '{}'
        ORDER BY id ASC"""

    array = list()
    standart = AtomDB().execute(sql.format('standart'))
    for x in range(randint(1, 5)):
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

    return (json(success), 200) if randint(0, 10) != 5 else (error(9050), 500)


@app.route('/api/ls/<ls>/counters/list/<codeInBilling>', methods=['GET'])
def request_ls_counters(ls=None, codeInBilling=None):

    array = list()
    for _ in range(randint(1, 5)):
        array.append(Counter(ls=ls).counter(codeInBilling=codeInBilling))

    dn = datetime.now()
    ot = dn - timedelta(days=15)
    do = (dn - timedelta(days=3)) if choice((True, False)) else (dn + timedelta(days=3))

    success = {
        "result": True,
        "data": array,
        "PeriodSch": {
            "ot": ot.isoformat(timespec='milliseconds'),
            "do": do.isoformat(timespec='milliseconds')
        }
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(6060), 500)


@app.route('/api/ls/counters/<option>', methods=['POST'])
def request_counters_option(option):

    success = dict()
    err = None

    if option == 'add':
        success = {
            "result": True,
            "message": "Данные успешно поданы"
        }
        err = error(6050)

    if option == 'history':
        array = list()
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

    return (json(success), 200) if randint(0, 20) != 5 else (err, 500)


@app.route('/api/ls/<ls>/services/<id>', methods=['GET'])
def request_url_ls_service_id(ls=None, id=None):

    sql = """
        SELECT name, image_url
        FROM atom_forms    
    """

    array = list()
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

    return (json(success), 200) if randint(0, 10) != 5 else (error(9050), 500)


@app.route('/api/user/send/form', methods=['POST'])
def request_send_form():

    success = {
        "result": True,
        "message": "Данные приняты сервером"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5090), 500)


@app.route('/api/ls/payments', methods=['POST'])
def request_payments():

    array = list()
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

    return (json(success), 200) if randint(0, 10) != 5 else (error(10050), 500)


@app.route('/api/ls/<ls>/checks/<tranzakciya>', methods=['GET'])
def request_checks(ls=None, tranzakciya=None):

    success = {
        "result": True,
        "data": Payment().check()
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(9030), 500)


@app.route('/api/ls/<ls>/pay/getpaygateway', methods=['GET'])
def request_url_getpaygateway(ls=None):

    array = list()
    for _ in range(randint(1, 5)):
        rnd = randint(10_000, 99_999)
        pay_gateway = {
            "code": "BN-{}".format(rnd),
            "name": "Банк {}".format(rnd)
        }
        array.append(pay_gateway)

    success = {
        "result": True,
        "pay_gateways": array,
        "usls_enabled": False if randint(0, 3) != 3 else True
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


@app.route('/api/pay/getlink', methods=['POST'])
def request_getlink():
    # {
    #   "ls": "69100122131",
    #   "tel": "79000000009",
    #   "email": "test@test.ru",
    #   "payGatewayCode": "",
    #   "summ": 12393,
    #   "usls": [
    #     {
    #       "amount": 266666,
    #       "amount_peni": 1232,
    #       "codeInBilling": 100
    #     }
    #   ]
    # }

    summ = request.get_json().get('summ')
    usls = request.get_json().get('usls')

    total = int()
    if summ is not None: 
        total = int(summ)
    
    if usls is not None:
        for item in usls:
            amount = item.get('amount')
            peni = item.get('amount_peni')
            total = total + int(amount) + int(peni)

    if total == 0:
        err = {
            "result": False,
            "errorCode": -32131,
            "errorText": 'Сумма должна быть больше 0',
        }
        return (json(err), 500)

    amount = f'?amount={total}'

    success = {
        "result": True,
        "link": "https://api-atomsbt.herokuapp.com/pay" + amount
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


@app.route('/api/ls/<ls>/reports/kvtMonths', methods=['GET'])
def request_url_kvtMonths(ls=None):

    array = list()
    for i in range(randint(1, 15)):
        date = datetime.now() - timedelta(days=31*i)
        array.append(date.isoformat(timespec='milliseconds'))

    success = {
        "result": True,
        "data": array
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


@app.route('/api/ls/reports/<option>', methods=['POST'])
def request_url_reports(option=None):

    success = {
        "result": True,
        "url": "https://api-atomsbt.herokuapp.com/page.pdf"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


@app.route('/api/user/services', methods=['POST'])
def request_url_services():

    lon = request.get_json().get('longitude')
    lat = request.get_json().get('latitude')
    dis = request.get_json().get('distance')

    success = {
        "result": True,
        "data": Map().places(float(lon), float(lat), float(dis))
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


@app.route('/api/ls/<ls>/victronenergy/getInstallation', methods=['GET'])
def request_url_getInstallation(ls=None):

    success = {
        "result": True,
        "OV1": "232.9 VAC" if randint(0, 3) > 1 else None,
        "OV2": "22.3 VAC" if randint(0, 3) > 1 else None,
        "OV3": "5 VAC" if randint(0, 3) > 1 else None,
        "bs": "84.5 %",
        "solar_yield": "140 W"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(5050), 500)


@app.route('/api/ls/<ls>/camera', methods=['GET'])
def request_url_camera(ls=None):

    sql = """
        SELECT name, video_url
        FROM atom_video"""

    array = list()
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

    return (json(success), 200) if randint(0, 10) != 5 else (error(9040), 500)


@app.route('/api/ls/counter/ontime', methods=['POST'])
def request_ontime():
    # {
    #     "ls": "69100403061",
    #     "startdate": "2018-10-01T00:00:00.000",
    #     "enddate": "2018-10-30T23:59:59.000",
    #     "RowID": "60139",
    #     "discretization": "d"
    # }

    disc = request.get_json().get('discretization')
    date = request.get_json().get('startdate')

    success = {
        "result": True,
        "data": Counter().ascue(randint(0, 30), disc, date)
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(6080), 500)


@app.route('/api/ls/analytics', methods=['POST'])
def request_analytics():
    # {
    #     "ls": "69100403061",
    #     "startdate": "2018-01-01T00:00:00.000",
    #     "enddate": "2018-11-07T23:59:59.000",
    #     "rowid": "1050194"
    # }

    current = choice([True, False])
    tarifs = ['Одноставочный', 'Двуставочный']
    tarif = choice([True, False])

    success = {
        "result": True,
        "change": choice([True, False]),
        "idTarif": randint(11100, 999900),
        "nameTarif": "Переходный",
        "data": [
            {
                "Current": current,
                "Tarif": tarifs[0 if tarif else 1],
                "sum": randint(11100, 999900)
            },
            {
                "Current": not current,
                "Tarif": tarifs[0 if not tarif else 1],
                "sum": randint(11100, 999900)
            }
        ]
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(10040), 500)


@app.route('/api/user/changeTarif', methods=['POST'])
def request_change_tarif():
    # {
    #     "ls": 69100403061,
    #     "idTarif": 1
    #     "rowid": "1050194"
    # }

    success = {
        "result": True,
        "message": "Ваше сообщение принято"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(6020), 500)


@app.route('/api/ls/counter/last', methods=['POST'])
def request_counter_last():

    success = {
        "result": True,
        "NAPRYAZHENIE": "220 В",
        "SILATOKA": "0.3 А"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(10080), 500)


@app.route('/api/ls/<option>/getWeatherToLS', methods=['GET'])
def request_get_weather_to_ls(option):

    icon = choice([
        "bkn_-sn_n", "bkn_+ra_d", "bkn_+ra_n", "bkn_+sn_d", "bkn_+sn_n",
        "bkn_d", "bkn_n", "bkn_ra_d", "bkn_ra_n", "bkn_sn_d", "bkn_sn_n",
        "bl", "fct_-ra", "fct_-sn", "fct_+ra", "fct_+sn", "fct_ra_sn",
        "fct_ra", "fct_sn_dwn", "fct_sn_rs", "fct_sn", "fg_d", "fg_n", "ovc_-ra",
        "ovc_-sn", "ovc_+ra", "ovc_+sn", "ovc_gr", "ovc_ra_sn", "ovc_ra",
        "ovc_sn", "ovc_ts_gr", "ovc_ts_ra", "ovc_ts", "ovc", "skc_d", "skc_n"
    ])
    icon_url = f"https://yastatic.net/weather/i/icons/blueye/color/svg/{icon}.svg"

    success = {
        "result": True,
        "data": {
            "temp": str(randint(-40, 40)),
            "icon": choice([icon_url, None])
        }
    }

    return (json(success), 200) if randint(0, 20) != 5 else (error(10080), 500)


@app.route('/api/user/feedback', methods=['POST'])
def request_feedback():

    success = {
        "result": True,
        "message": "Регистрация обращения выполнена"
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(6020), 500)


@app.route('/api/ls/<option>/getTheme', methods=['GET'])
def request_url_getTheme(option):

    array = list()
    for i in range(randint(1, 20)):
        item = {
            "theme": f'Тема с номером {i}' + choice([' тестовый текст для проверки 2х строчной выпадалки', '']),
            "description": choice(["test", None, ""]),
            "id": f'{i}'
        }
        array.append(item)

    success = {
        "result": True,
        "data": array
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(6020), 500)


@app.route('/api/devices/<option>', methods=['POST'])
def request_url_push_chenge(option=None):

    success = {
        "result": True
    }

    return (json(success), 200) if randint(0, 10) != 5 else (error(10020), 500)

# -----------------------------------------------------------------------


@app.route("/")
@app.route("/<option>")
def main(option='index'):

    static = {
        'favicon.ico': 'image/vnd.microsoft.icon',
        'page.pdf': 'application/pdf'
    }

    if static.get(option) is not None:
        path = os.path.join(app.root_path, 'static')
        return send_from_directory(path, option, mimetype=static.get(option))

    amount = request.args.get('amount')
    if amount is not None:
        amount = str( int(request.args.get('amount'))/100 ) + ' ₽'
    return render_template(f'{option}.html', amount=amount)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

# -----------------------------------------------------------------------

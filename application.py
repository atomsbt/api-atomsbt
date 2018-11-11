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

url_register = '/api/user/register/tel'
@app.route(url_register, methods=['POST'])
def register():

    app.logger.info('POST ' + url_register + ':\n%s', request.get_json())

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
    if choice([True, False]):
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

url_confirm = '/api/user/confirm/tel'
@app.route(url_confirm, methods=['POST'])
def confirm():

    app.logger.info('POST ' + url_confirm + ':\n%s', request.get_json())

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
    if choice([True, False]):
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

url_reset = '/api/user/reset/tel'
@app.route(url_reset, methods=['POST'])
def reset():

    app.logger.info('POST ' + url_reset + ':\n%s', request.get_json())

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
    if choice([True, False]):
        return json(success), 200
    return json(error), 500

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

    sleep(0.5)
    if choice([True, False]):
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

url_auth = '/api/user/auth'
@app.route(url_auth, methods=['POST'])
def auth():

    app.logger.info('POST ' + url_auth + ':\n%s', request.get_json())

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
    if choice([True, False]):
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

url_ls = '/api/ls'
@app.route(url_ls, methods=['GET'])
def ls():

    ls_array = []
    ls_count = randint(0,5)
    for _ in range(0,ls_count):
        ls_array.append(LS().content())
    success = ls_array

    error = {
        "result": False,
        "errorCode": 401,
        "errorText": "Указаны неверные учетные данные"
    }

    if choice([True, False]):
        return json(success), 200
    return json(error), 500


#-----------------------------------------------------------------------

url_ls_option = '/api/ls/<option>'
@app.route(url_ls_option, methods=['POST'])
def ls_option(option=None):

    success = None
    error = None

    app.logger.info('POST ' + url_ls_option + ':\n%s', request.get_json())

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

    if option == 'remove':

        success = {
            "result": True,
            "message": "Лицевой счет успешно отвязан"
        }
        error = {
            "result": False,
            "errorCode": 6070,
            "errorText": "Нет прав на данный лицевой счет"
        }

    if choice([True, False]):
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

#-----------------------------------------------------------------------
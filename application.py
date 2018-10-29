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

register_url = '/api/user/register/tel'
@app.route(register_url, methods=['POST'])
def register():

    app.logger.info('POST ' + register_url + ':\n%s', request.get_json())

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
    if choice([True, False]) == True :
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

confirm_url = '/api/user/confirm/tel'
@app.route(confirm_url, methods=['POST'])
def confirm():

    app.logger.info('POST ' + confirm_url + ':\n%s', request.get_json())

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
    if choice([True, False]) == True :
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

reset_url = '/api/user/reset/tel'
@app.route(reset_url, methods=['POST'])
def reset():

    app.logger.info('POST ' + reset_url + ':\n%s', request.get_json())

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
    if choice([True, False]) == True :
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

auth_url = '/api/user/auth'
@app.route(auth_url, methods=['POST'])
def auth():

    app.logger.info('POST ' + auth_url + ':\n%s', request.get_json())

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
    if choice([True, False]) == True :
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

bind_url = '/api/ls/bind'
@app.route(bind_url, methods=['POST'])
def bind():

    app.logger.info('POST ' + bind_url + ':\n%s', request.get_json())

    success = {
        "result": True,
        "message": "Лицевой счет успешно привязан"
    }

    error = {
        "result": False,
        "errorCode": 7030,
        "errorText": "Введена некорректная сумма"
    }

    sleep(0.5)
    if choice([True, False]) == True :
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

ls_url = '/api/ls'
@app.route(ls_url, methods=['GET'])
def ls():

    success = []

    ls_count = randint(0,5)
    for _ in range(0,ls_count):
        success.append(LS().content())

    error = {
        "result": False,
        "errorCode": 401,
        "errorText": "Указаны неверные учетные данные"
    }

    sleep(0.5)
    if choice([True, False]) == True :
        return json(success), 200
    return json(error), 500

#-----------------------------------------------------------------------

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

#-----------------------------------------------------------------------
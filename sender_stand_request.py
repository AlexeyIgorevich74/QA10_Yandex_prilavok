import configuration
import requests
import data

#Функция создания нового пользователя
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers,)

#функция добавления авторизации
def get_headers():
    response = post_new_user(data.user_body)
    authToken = "Bearer " + response.json()['authToken']
    current_headers = data.headers.copy()
    current_headers["Authorization"] = authToken
    return current_headers


#Функция создания набора с новым токеном авторизации
def post_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=body,
                         headers=get_headers())
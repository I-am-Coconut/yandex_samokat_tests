import configuration
import requests
import data

#Создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

#Получить номер заказа
def get_order_track():
    track_response = post_new_order(data.order_body)
    return track_response.json()["track"]

#Получить заказ по его номеру 
def get_info_by_track():
    track = get_order_track()
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t": track})

response = get_info_by_track()
print(response.status_code)
print(response.json())

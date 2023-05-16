import requests
import configuration


# Ручка для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.MAIN_URL + configuration.ORDER_CREATE,
                         json=body)


# Ручка для получения заказа по его трек-номеру
def get_order_by_his_number(parameters):
    return requests.get(configuration.MAIN_URL + configuration.ORDER_GET,
                        params=parameters)

import data
import sender_stand_request


# Функция создания заказа, а также сохранения и вывода трек-номера из себя
def get_new_param_track_number(body):
    # 1. Создадим заказ и запишем его тело ответа
    order_response = sender_stand_request.post_new_order(body)
    # 2. Скопируем форму тела ответа из data
    track_number = data.track_number
    # 3. Перезапишем трек-номер в теле track_number
    track_number["t"] = order_response.json()["track"]
    # Выведем сформированное тело (track_number) наружу
    return track_number


# Проверка на наличие заказа в таблице Orders по указанному трек-номеру
def positive_check_of_get_order_by_his_number(params_order):
    # 1. Отправим запрос на получение заказа по его трек-номеру
    body_request = sender_stand_request.get_order_by_his_number(params_order)
    # 2. Если придёт код 200, то заказ в таблице есть
    assert body_request.status_code == 200


# Проведем тест: "Созданный заказ был внесен в таблицу Orders"
def test_check_for_create_order_in_the_order_table():
    # 1. Создадим заказ и сохраним его трек-номер в форме параметра для запроса
    param_of_order = get_new_param_track_number(data.body_order)
    # 2. Проверим наличие заказа в таблице Orders
    positive_check_of_get_order_by_his_number(param_of_order)

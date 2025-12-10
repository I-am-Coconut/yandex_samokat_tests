#Александр Куракин 38 когорта. Финальный проект. Составление SQL-запроса и автоматизация теста.
import order_request

#Проверка что заказ создался по номеру

def test_get_order_by_track():
    response = order_request.get_info_by_track()
    assert response.status_code == 200 
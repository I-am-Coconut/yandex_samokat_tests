#Задание 1 Получение логинов курьеров с заказами в статусе "В доставке"

SELECT
    c.login,
    COUNT(o.id) AS orders_in_delivery
FROM
    "Couriers" AS c 
INNER JOIN
    "Orders" AS o ON c.id = o."courierId"
WHERE
    o."inDelivery" = true
GROUP BY
    c.login

#Задание 2 Получение списка заказов со статусами

SELECT
    track,
    CASE
        WHEN "finished" = true THEN 2
        WHEN "cancelled" = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM
    "Orders";
-- TODO: This query will return a table with the top 10 least revenue categories 
-- in English, the number of orders and their total revenue. The first column 
-- will be Category, that will contain the top 10 least revenue categories; the 
-- second one will be Num_order, with the total amount of orders of each 
-- category; and the last one will be Revenue, with the total revenue of each 
-- catgory.
-- HINT: All orders should have a delivered status and the Category and actual 
-- delivery date should be not null.

WITH olist_orders_with_payments AS (
	SELECT
		oo.order_id,
		oop.payment_value
	FROM
		OLIST_ORDERS AS oo
	JOIN
		OLIST_ORDER_PAYMENTS AS oop
	ON
		oo.order_id = oop.order_id
	WHERE
		oo.order_status = "delivered"
		AND oo.order_purchase_timestamp IS NOT NULL
        AND oo.order_delivered_customer_date IS NOT NULL
),
filtered_olist_order_items AS (
	SELECT 
		ooi.order_id,
		ooi.product_id,
		ooi.price,
		ooi.freight_value,
		oo.payment_value
	FROM
		OLIST_ORDER_ITEMS AS ooi
	JOIN
		olist_orders_with_payments AS oo
	ON
		oo.order_id = ooi.order_id
	ORDER BY ooi.order_id
),
olist_products_with_category AS (
	SELECT
		op.product_id,
		pcnt.product_category_name_english AS category
	FROM
		OLIST_PRODUCTS AS op
	JOIN
		PRODUCT_CATEGORY_NAME_TRANSLATION AS pcnt
	ON
		op.product_category_name = pcnt.product_category_name
	WHERE
		category IS NOT NULL
)
SELECT
	opwc.category AS Category,
	COUNT(DISTINCT fooi.order_id) AS Num_order,
	SUM(fooi.payment_value) AS Revenue
FROM
	filtered_olist_order_items AS fooi
JOIN
	olist_products_with_category AS opwc
ON
	fooi.product_id = opwc.product_id
GROUP BY
	Category
ORDER BY
	Revenue
LIMIT 10

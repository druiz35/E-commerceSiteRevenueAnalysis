-- TODO: This query will return a table with two columns; customer_state, and 
-- Revenue. The first one will have the letters that identify the top 10 states 
-- with most revenue and the second one the total revenue of each.
-- HINT: All orders should have a delivered status and the actual delivery date 
-- should be not null. 
WITH olist_order_with_state AS (
	SELECT 
		oc.customer_id,
		oc.customer_state,
		oo.order_id
	FROM
		OLIST_CUSTOMERS_DATASET AS oc,
		OLIST_ORDERS AS oo
	WHERE
		oc.customer_id = oo.customer_id
		AND oo.order_status = "delivered"
		AND oo.order_delivered_customer_date IS NOT NULL
		AND oo.order_purchase_timestamp IS NOT NULL
	ORDER BY customer_state ASC
),
olist_order_payments_total AS (
	SELECT 
		oop.order_id,
		SUM(payment_value) AS total_payment_value
	FROM
		OLIST_ORDER_PAYMENTS AS oop
	GROUP BY order_id
	ORDER BY order_id
), 
joined_tables AS (
	SELECT 
		oows.customer_id,
		oows.order_id,
		oows.customer_state,
		oopt.total_payment_value
	FROM
		olist_order_payments_total AS oopt,
		olist_order_with_state AS oows
	WHERE
		oopt.order_id = oows.order_id
	GROUP BY oows.customer_id
	ORDER BY oows.customer_id
)
SELECT
	jt.customer_state AS customer_state,
	SUM(jt.total_payment_value) AS Revenue
FROM joined_tables AS jt
GROUP BY customer_state
ORDER BY Revenue DESC
LIMIT 10

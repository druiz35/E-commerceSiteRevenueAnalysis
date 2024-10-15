-- This query will return a table with two columns; State, and 
-- Delivery_Difference. The first one will have the letters that identify the 
-- states, and the second one the average difference between the estimate 
-- delivery date and the date when the items were actually delivered to the 
-- customer.
-- HINTS:
-- 1. You can use the julianday function to convert a date to a number.
-- 2. You can use the CAST function to convert a number to an integer.
-- 3. You can use the STRFTIME function to convert a order_delivered_customer_date to a string removing hours, minutes and seconds.
-- 4. order_status == 'delivered' AND order_delivered_customer_date IS NOT NULL
WITH filtered_olist_orders AS (
    SELECT
        oo.customer_id,
        oo.order_delivered_customer_date,
        oo.order_estimated_delivery_date,
        oc.customer_state AS State
    FROM
        OLIST_ORDERS AS oo,
        OLIST_CUSTOMERS_DATASET AS oc
    WHERE
        oo.order_status = "delivered"
        AND oo.order_delivered_customer_date IS NOT NULL
        AND oo.customer_id = oc.customer_id
),
difference_olist_orders AS (
	SELECT 
	    State, 
	    CAST(ROUND(JULIANDAY(order_estimated_delivery_date) - JULIANDAY(order_delivered_customer_date)+0.5, 0) AS INTEGER) AS Delivery_Difference
	FROM 
	    filtered_olist_orders
)
SELECT 
    State, 
    SUM(Delivery_Difference) / COUNT(State) AS Delivery_Difference
FROM 
    difference_olist_orders
GROUP BY State
ORDER BY Delivery_Difference
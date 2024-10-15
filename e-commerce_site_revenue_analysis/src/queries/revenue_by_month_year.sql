-- TODO: This query will return a table with the revenue by month and year. It
-- will have different columns: month_no, with the month numbers going from 01
-- to 12; month, with the 3 first letters of each month (e.g. Jan, Feb);
-- Year2016, with the revenue per month of 2016 (0.00 if it doesn't exist);
-- Year2017, with the revenue per month of 2017 (0.00 if it doesn't exist) and
-- Year2018, with the revenue per month of 2018 (0.00 if it doesn't exist).

-- Tables: olist_order_payments
-- Columns: 

WITH temp_table AS
(SELECT
    strftime('%m', oo.order_delivered_customer_date) AS month_no,
    oop.payment_value AS payment_value,
    oo.order_delivered_customer_date AS order_delivered_customer_date
FROM 
    OLIST_ORDERS AS oo, 
    OLIST_ORDER_PAYMENTS AS oop
WHERE oo.order_id = oop.order_id
    AND order_status = 'delivered' 
    AND order_delivered_customer_date IS NOT NULL 
    AND order_purchase_timestamp IS NOT NULL
GROUP BY oo.order_id 
)
SELECT
    month_no AS month_no,
    CASE
        WHEN month_no = "01" THEN "Jan"
        WHEN month_no = "02" THEN "Feb"
        WHEN month_no = "03" THEN "Mar"
        WHEN month_no = "04" THEN "Apr"
        WHEN month_no = "05" THEN "May"
        WHEN month_no = "06" THEN "Jun"
        WHEN month_no = "07" THEN "Jul"
        WHEN month_no = "08" THEN "Aug"
        WHEN month_no = "09" THEN "Sep"
        WHEN month_no = "10" THEN "Oct"
        WHEN month_no = "11" THEN "Nov"
        WHEN month_no = "12" THEN "Dec"
    END AS "month",
    SUM(CASE strftime('%Y', order_delivered_customer_date)
        WHEN '2016' THEN (payment_value) ELSE 0.0 
    END) AS 'Year2016',
    SUM(CASE strftime('%Y', order_delivered_customer_date)
        WHEN '2017' THEN (payment_value) ELSE 0.0 
    END) AS 'Year2017',
    SUM(CASE strftime('%Y', order_delivered_customer_date)
        WHEN '2018' THEN (payment_value) ELSE 0.0 
    END) AS 'Year2018'
FROM temp_table
GROUP BY month_no
ORDER BY month_no

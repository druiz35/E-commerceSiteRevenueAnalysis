WITH converted_order_days as (
SELECT strftime('%Y/%m/%d', order_purchase_timestamp) as order_day FROM OLIST_ORDERS WHERE strftime('%Y', order_purchase_timestamp) == '2017'
),
order_counts as (
	SELECT order_day, COUNT(order_day) as order_count FROM converted_order_days GROUP BY order_day ORDER BY order_count DESC
)
SELECT 
	oc.order_day, 
	oc.order_count,
	CASE WHEN strftime('%Y/%m/%d', h.date) IS NULL THEN 'No' ELSE 'Yes' END AS is_holiday
FROM
	order_counts as oc
FULL OUTER JOIN 
	public_holidays as h
ON
	oc.order_day = strftime('%Y/%m/%d', h.date);
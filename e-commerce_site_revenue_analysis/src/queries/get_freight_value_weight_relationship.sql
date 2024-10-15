WITH freight_weight_relationship AS (
SELECT
	ooi.order_id,
	op.product_weight_g + ooi.freight_value AS relationship_sum
FROM OLIST_PRODUCTS AS op
FULL OUTER JOIN OLIST_ORDER_ITEMS AS ooi
ON op.product_id = ooi.product_id
)
SELECT fwr.order_id, fwr.relationship_sum
FROM freight_weight_relationship AS fwr
JOIN OLIST_ORDERS AS oo
ON fwr.order_id = oo.order_id
WHERE oo.order_status == 'delivered';
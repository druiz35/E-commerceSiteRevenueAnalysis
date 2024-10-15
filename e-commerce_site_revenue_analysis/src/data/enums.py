from enum import Enum

class QueryEnum(Enum):
    """This class enumerates all the queries that are available"""
    DELIVERY_DATE_DIFFERENCE = "delivery_date_difference"
    GLOBAL_AMMOUNT_ORDER_STATUS = "global_ammount_order_status"
    REVENUE_BY_MONTH_YEAR = "revenue_by_month_year"
    REVENUE_PER_STATE = "revenue_per_state"
    TOP_10_LEAST_REVENUE_CATEGORIES = "top_10_least_revenue_categories"
    TOP_10_REVENUE_CATEGORIES = "top_10_revenue_categories"
    REAL_VS_ESTIMATED_DELIVERED_TIME = "real_vs_estimated_delivered_time"
    ORDERS_PER_DAY_AND_HOLIDAYS_2017 = "orders_per_day_and_holidays_2017"
    GET_FREIGHT_VALUE_WEIGHT_RELATIONSHIP = "get_freight_value_weight_relationship"

class TableEnum(Enum):
    """"""
    OLIST_CUSTOMERS_DATASET = "olist_customers_dataset.csv"
    OLIST_GEOLOCATION = "olist_geolocation_dataset.csv"
    OLIST_ORDER_ITEMS = "olist_order_items_dataset.csv"
    OLIST_ORDER_PAYMENTS = "olist_order_payments_dataset.csv"
    OLIST_ORDER_REVIEWS = "olist_order_reviews_dataset.csv"
    OLIST_ORDERS = "olist_orders_dataset.csv"
    OLIST_PRODUCTS = "olist_products_dataset.csv"
    OLIST_SELLERS = "olist_sellers_dataset.csv"
    PRODUCT_CATEGORY_NAME_TRANSLATION = "product_category_name_translation.csv"

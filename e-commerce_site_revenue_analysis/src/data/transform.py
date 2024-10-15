from sqlalchemy import text
from src.data.enums import QueryEnum
from pandas import DataFrame, read_sql
import logging


class QueriesTransform:
    def __init__(self, db_engine, queries_root_path):
        self.db_engine = db_engine
        self.queries_root_path = queries_root_path
        log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=log_fmt)
        self.logger = logging.getLogger(__name__)
        
    def get_queries_results(self):
        query_names = [query_mapping.value for query_mapping in list(QueryEnum)]
        results = {}
        for name in query_names:
            self.logger.info(f'Loading query: {name}')
            query = self.read_query(name)
            if name == "get_freight_value_weight_relationship":
                results[name] = self.query_freight_value_weight_relationship(self.db_engine)
            else:
                results[name] = read_sql(query, self.db_engine)
        return results

    def read_query(self, query_name: str) -> str:
        with open(f"{self.queries_root_path}/{query_name}.sql", "r") as f:
            sql_file = f.read()
            sql = text(sql_file)
        return sql
    
    def query_freight_value_weight_relationship(self, database):
        orders = read_sql("SELECT * FROM OLIST_ORDERS", database)
        items = read_sql("SELECT * FROM OLIST_ORDER_ITEMS", database)
        products = read_sql("SELECT * FROM OLIST_PRODUCTS", database)
        data = items.merge(orders, left_on="order_id", right_on="order_id").merge(products, left_on="product_id", right_on="product_id")
        delivered = data[data["order_status"] == "delivered"]
        aggregations = delivered.groupby("order_id", as_index=False).agg({
            "freight_value": "sum",
            "product_weight_g": "sum"
        })
        return aggregations

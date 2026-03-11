"""Explicit StructType schemas for bronze layer. No inferSchema; dates as DateType/TimestampType."""

from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

# order_items: order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value
order_items_schema = StructType(
    [
        StructField("order_id", StringType(), True),
        StructField("order_item_id", StringType(), True),
        StructField("product_id", StringType(), True),
        StructField("seller_id", StringType(), True),
        StructField("shipping_limit_date", TimestampType(), True),
        StructField("price", DoubleType(), True),
        StructField("freight_value", DoubleType(), True),
    ]
)

# customers: customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state
customers_schema = StructType(
    [
        StructField("customer_id", StringType(), True),
        StructField("customer_unique_id", StringType(), True),
        StructField("customer_zip_code_prefix", StringType(), True),
        StructField("customer_city", StringType(), True),
        StructField("customer_state", StringType(), True),
    ]
)

# products: product_id, product_category_name, product_name_lenght, product_description_lenght,
#           product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm
products_schema = StructType(
    [
        StructField("product_id", StringType(), True),
        StructField("product_category_name", StringType(), True),
        StructField("product_name_lenght", IntegerType(), True),
        StructField("product_description_lenght", IntegerType(), True),
        StructField("product_photos_qty", IntegerType(), True),
        StructField("product_weight_g", DoubleType(), True),
        StructField("product_length_cm", DoubleType(), True),
        StructField("product_height_cm", DoubleType(), True),
        StructField("product_width_cm", DoubleType(), True),
    ]
)

# orders: order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at,
#        order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date
orders_schema = StructType(
    [
        StructField("order_id", StringType(), True),
        StructField("customer_id", StringType(), True),
        StructField("order_status", StringType(), True),
        StructField("order_purchase_timestamp", TimestampType(), True),
        StructField("order_approved_at", TimestampType(), True),
        StructField("order_delivered_carrier_date", TimestampType(), True),
        StructField("order_delivered_customer_date", TimestampType(), True),
        StructField("order_estimated_delivery_date", TimestampType(), True),
    ]
)

# payments: order_id, payment_sequential, payment_type, payment_installments, payment_value
payments_schema = StructType(
    [
        StructField("order_id", StringType(), True),
        StructField("payment_sequential", IntegerType(), True),
        StructField("payment_type", StringType(), True),
        StructField("payment_installments", IntegerType(), True),
        StructField("payment_value", DoubleType(), True),
    ]
)

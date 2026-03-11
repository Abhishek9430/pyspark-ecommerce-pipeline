"""Bronze layer: read raw CSV with schema, add ingestion/partition columns, write Parquet."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from models.schemas import (
    customers_schema,
    order_items_schema,
    orders_schema,
    payments_schema,
    products_schema,
)

# table_name -> schema for raw CSV read (no inferSchema)
SCHEMA_MAP = {
    "orders": orders_schema,
    "customers": customers_schema,
    "products": products_schema,
    "order_items": order_items_schema,
    "payments": payments_schema,
}

BRONZE_TABLES = list(SCHEMA_MAP.keys())


def load_to_bronze(
    spark: SparkSession,
    config: dict,
    process_date: str,
    table_name: str,
) -> None:
    """
    Read raw CSV from {raw}/{table_name}, add ingestion_timestamp and process_date,
    write Parquet to {bronze}/{table_name} partitioned by process_date.
    No joins, no transformations, no business logic.
    """
    if table_name not in SCHEMA_MAP:
        raise ValueError(f"Unknown table: {table_name}. Valid: {BRONZE_TABLES}")

    paths = config.get("paths", {})
    raw_base = paths.get("raw", "data/raw")
    bronze_base = paths.get("bronze", "data/bronze")

    raw_path = f"{raw_base}/{table_name}"
    bronze_path = f"{bronze_base}/{table_name}"
    schema = SCHEMA_MAP[table_name]

    df = (
        spark.read.format("csv")
        .option("header", True)
        .schema(schema)
        .load(raw_path)
    )

    df = (
        df.withColumn("ingestion_timestamp", F.current_timestamp())
        .withColumn("process_date", F.lit(process_date))
    )

    (
        df.write.format("parquet")
        .mode("overwrite")
        .option("partitionOverwriteMode", "dynamic")
        .partitionBy("process_date")
        .save(bronze_path)
    )

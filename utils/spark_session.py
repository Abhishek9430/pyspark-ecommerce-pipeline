"""Build and return a configured SparkSession. Single place for Spark creation."""

import logging

from pyspark.sql import SparkSession


def get_spark_session(config: dict) -> SparkSession:
    """Build SparkSession and apply config-based settings."""
    spark_config = config.get("spark", {})
    app_name = spark_config.get("app_name", "ecommerce-batch-job")

    builder = SparkSession.builder.appName(app_name)
    spark = builder.getOrCreate()

    for logger_name in ("pyspark", "py4j"):
        logging.getLogger(logger_name).setLevel(logging.ERROR)

    shuffle_partitions = spark_config.get("shuffle_partitions")
    if shuffle_partitions is not None:
        spark.conf.set("spark.sql.shuffle.partitions", str(shuffle_partitions))

    broadcast_timeout = spark_config.get("broadcast_timeout")
    if broadcast_timeout is not None:
        spark.conf.set("spark.sql.broadcastTimeout", str(broadcast_timeout))

    adaptive_enabled = spark_config.get("adaptive_execution_enabled", True)
    spark.conf.set("spark.sql.adaptive.enabled", str(adaptive_enabled).lower())

    return spark

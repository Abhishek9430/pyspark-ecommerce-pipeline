import logging

from ingestion.bronze_loader import BRONZE_TABLES, load_to_bronze

logger = logging.getLogger(__name__)


def run(spark, config, process_date):
    logger.info("Bronze job started for process_date=%s", process_date)

    spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")

    for table_name in BRONZE_TABLES:
        load_to_bronze(spark, config, process_date, table_name)

    logger.info("Bronze job completed for process_date=%s", process_date)
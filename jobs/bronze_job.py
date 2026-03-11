from ingestion.bronze_loader import BRONZE_TABLES, load_to_bronze


def run(spark, config, process_date):
    for table_name in BRONZE_TABLES:
        load_to_bronze(spark, config, process_date, table_name)
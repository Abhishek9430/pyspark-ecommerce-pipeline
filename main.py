"""Orchestrator entry point. Parses CLI, loads config, initializes Spark, dispatches to job."""

import argparse
from pathlib import Path

import yaml

from jobs import bronze_job, silver_job, gold_job
from utils.spark_session import get_spark_session


def load_config(config_path: str) -> dict:
    """Load YAML config from path."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="E-commerce PySpark pipeline")
    parser.add_argument("--layer", required=True, choices=["bronze", "silver", "gold"])
    parser.add_argument("--date", required=True, help="Process date (e.g. 2026-01-01)")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent
    config_path = project_root / "config" / "config.yaml"
    config = load_config(config_path)

    spark = get_spark_session(config)
    spark.sparkContext.setLogLevel("ERROR")
    if args.layer == "bronze":
        bronze_job.run(spark, config, args.date)
    elif args.layer == "silver":
        silver_job.run(spark, config, args.date)
    elif args.layer == "gold":
        gold_job.run(spark, config, args.date)

    spark.stop()


if __name__ == "__main__":
    main()

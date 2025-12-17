import yaml
import pandas as pd
from ingestion.csv_connector import read_csv
from validation.schema import HRSchema
from preprocessing.missing_values import handle_missing
from preprocessing.scaling import scale
from preprocessing.encoding import encode
from utils.logger import logger


def run_pipeline() -> None:
    config = yaml.safe_load(open("config/config.yaml"))

    df = read_csv(config["data"]["raw_path"])
    logger.info("Data loaded")

    df = df.drop_duplicates()
    df = df.drop(columns=["Hiring_Date"])
    df["Experience"] = df["Experience"].str.replace("years", "", regex=False)
    # df["Experience"] = df["Experience"].astype(int)
    # df['Experience'] = pd(df['Experience'].astype(str).str.strip())
    df['Experience'] = pd.to_numeric(df['Experience'])
    df["Experience"] = df["Experience"].fillna(0).astype("int64")

    # bins = [5,10,15,20,25,30,35,40]
    # labels = ['Experience 1-5 year','Experience 5-10 year','Experience 10-15 year','Experience 15-20 year','Experience 20-25 year','Experience 25-30 year','Experience 30-35 year','Experience 35-40 year']
    # df['Experience'] = pd.cut(df['Experience'], bins=bins, labels=labels, right=True)

    df["Salary"] = df["Salary"].astype(float)
    df = df[df["Age"] > 18]
    df["Location"] = df["Location"].fillna("Unknown")
    df["Department"] = df["Department"].fillna("Unknown")

    HRSchema.validate(df)
    logger.info("Schema validated")

    df = handle_missing(
        df,
        config["columns"]["numerical"],
        config["columns"]["categorical"]
    )
    logger.info("Missing values handled")

    df = scale(df, config["columns"]["numerical"])
    df = encode(df, config["columns"]["categorical"])
    logger.info("Scaling & encoding completed")

    df.to_csv(config["data"]["processed_path"], index=False)
    logger.info("Pipeline completed")

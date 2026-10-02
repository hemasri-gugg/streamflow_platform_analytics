from pathlib import Path
import logging

import pandas as pd
import mysql.connector

from db_connection import get_connection

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FOLDER = BASE_DIR / "02_data"

DIMENSION_TABLES = {
    "dim_campaigns": "dim_campaigns.csv",
    "dim_content": "dim_content.csv",
    "dim_customers": "dim_customers.csv",
    "dim_devices": "dim_devices.csv",
    "dim_subscription_plans": "dim_subscription_plans.csv"
}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)





def load_table(cursor, connection, table_name, csv_file):

    csv_path = DATA_FOLDER / csv_file

    logging.info(f"Loading {table_name}")

    df = pd.read_csv(csv_path)

    columns = ",".join(df.columns)

    placeholders = ",".join(["%s"] * len(df.columns))

    query = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES ({placeholders})
    """

    records = list(df.itertuples(index=False, name=None))

    cursor.executemany(query, records)

    connection.commit()

    logging.info(f"{len(records)} rows inserted into {table_name}")


def main():

    connection = get_connection()

    cursor = connection.cursor()

    try:

        for table, file in DIMENSION_TABLES.items():

            load_table(cursor, connection, table, file)

        logging.info("-------------------------------------")
        logging.info("Dimension Load Completed Successfully")
        logging.info("-------------------------------------")

    except mysql.connector.Error as err:

        connection.rollback()

        logging.error(err)

    finally:

        cursor.close()

        connection.close()


if __name__ == "__main__":
    main()
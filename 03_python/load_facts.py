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

FACT_TABLES = {
    "fact_subscriptions": "fact_subscriptions.csv",
    "fact_payments": "fact_payments.csv",
    "fact_campaign_responses": "fact_campaign_responses.csv",
    "fact_support_tickets": "fact_support_tickets.csv",
    "fact_watch_history": "fact_watch_history.csv"
}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

# -------------------------------------------------------
# Data Cleaning
# -------------------------------------------------------

def clean_dataframe(df):
    """
    Clean dataframe before inserting into MySQL.
    """

    # Remove empty columns
    df = df.dropna(axis=1, how="all")

    # Remove columns like 'Unnamed: 0'
    df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]

    # Strip spaces from headers
    df.columns = df.columns.astype(str).str.strip()

    # Convert NaN to Python None
    df = df.astype(object)
    df = df.where(pd.notnull(df), None)

    return df


# -------------------------------------------------------
# Schema Validation
# -------------------------------------------------------

def get_mysql_columns(cursor, table_name):

    cursor.execute(f"DESCRIBE {table_name}")

    return [row[0] for row in cursor.fetchall()]


def validate_schema(cursor, table_name, df):

    mysql_columns = get_mysql_columns(cursor, table_name)

    csv_columns = list(df.columns)

    if mysql_columns != csv_columns:

        raise Exception(
            f"""
Schema mismatch in {table_name}

MySQL :
{mysql_columns}

CSV :
{csv_columns}
"""
        )


# -------------------------------------------------------
# Load Single Table
# -------------------------------------------------------

def load_table(cursor, table_name, csv_file):

    csv_path = DATA_FOLDER / csv_file

    logging.info(f"Loading {table_name}")

    df = pd.read_csv(csv_path)

    df = clean_dataframe(df)

    validate_schema(cursor, table_name, df)

    columns = ",".join(df.columns)

    placeholders = ",".join(["%s"] * len(df.columns))

    query = f"""
    INSERT INTO {table_name}
    ({columns})
    VALUES ({placeholders})
    """

    records = [tuple(row) for row in df.to_numpy()]

    cursor.executemany(query, records)

    logging.info(f"{len(records):,} rows inserted into {table_name}")


# -------------------------------------------------------
# Main
# -------------------------------------------------------

def main():

    connection = get_connection()

    cursor = connection.cursor()

    try:

        logging.info("=" * 60)
        logging.info("Loading Fact Tables")
        logging.info("=" * 60)

        for table_name, csv_file in FACT_TABLES.items():

            load_table(
                cursor,
                table_name,
                csv_file
            )

        connection.commit()

        logging.info("=" * 60)
        logging.info("Fact Tables Loaded Successfully")
        logging.info("=" * 60)

    except mysql.connector.Error as err:

        connection.rollback()

        logging.error(err)

    except Exception as err:

        connection.rollback()

        logging.error(err)

    finally:

        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()
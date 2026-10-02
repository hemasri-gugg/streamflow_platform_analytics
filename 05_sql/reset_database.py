from db_connection import get_connection
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

FACT_TABLES = [
    "fact_campaign_responses",
    "fact_payments",
    "fact_subscriptions",
    "fact_support_tickets",
    "fact_watch_history"
]

DIMENSION_TABLES = [
    "dim_campaigns",
    "dim_content",
    "dim_customers",
    "dim_devices",
    "dim_subscription_plans"
]


def reset_database():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        logging.info("Disabling Foreign Key Checks...")

        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

        for table in FACT_TABLES:
            logging.info(f"Truncating {table}")
            cursor.execute(f"TRUNCATE TABLE {table}")

        for table in DIMENSION_TABLES:
            logging.info(f"Truncating {table}")
            cursor.execute(f"TRUNCATE TABLE {table}")

        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        conn.commit()

        logging.info("Database reset completed.")

    except Exception as e:

        conn.rollback()

        logging.error(e)

    finally:

        cursor.close()
        conn.close()


if __name__ == "__main__":
    reset_database()
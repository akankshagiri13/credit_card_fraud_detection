import sqlite3


def save_results(df):

    connection = sqlite3.connect(
        "fraud_detection.db"
    )

    df.to_sql(
        "transactions",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()
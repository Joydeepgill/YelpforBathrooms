import sqlite3


def initialize(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    create_table = "CREATE TABLE IF NOT EXISTS reviews (review_id INTEGER PRIMARY KEY, washroom_id, rating INTEGER, comment TEXT, created_at DATETIME);"
    cursor.execute(create_table)

    create_table = "CREATE TABLE IF NOT EXISTS washrooms (washroom_id INTEGER PRIMARY KEY, primary_address TEXT, city TEXT, province TEXT, postal_code TEXT, longitude DECIMAL, latitude DECIMAL, comments TEXT,created_at DATETIME);"
    cursor.execute(create_table)

    connection.commit()
    connection.close

import os
import psycopg2
import time

def get_data():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM test;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

if __name__ == "__main__":
    while True:
        data = get_data()
        print("Data from DB:", data)
        time.sleep(5)

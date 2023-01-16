import os
import psycopg2

from psycopg2 import sql

if __name__ == "__main__":

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DATABASE", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "petulilinka"),
    )

    with conn, conn.cursor() as cur:
        create_car_table_query = sql.SQL(
            """
            DROP TABLE IF EXISTS car;
            CREATE TABLE car(
                car_id SERIAL PRIMARY KEY,
                brand VARCHAR(128) NOT NULL,
                old_year INT NOT NULL,
                price INT NOT NULL,
                fuel VARCHAR(128),
                color VARCHAR(128),
                mileage INT
            );
            """
        )

        print(create_car_table_query.as_string(cur))
        cur.execute(create_car_table_query)

    conn.close()
    print("1 = Closed ---- 0 = Open: ", conn.closed)

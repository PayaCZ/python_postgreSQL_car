import psycopg2
import psycopg2.extras
import connection


def get_cars(curr, conn):
    curr.execute("SELECT brand, old_year, price FROM car")
    result = curr.fetchall()
    return result


def insert_car(curr, conn, brand, old_year, price):
    curr.execute(
        "INSERT INTO car (brand, old_year, price) VALUES (%s, %s, %s)",
        (brand, old_year, price),
    )


if __name__ == "__main__":
    conn = psycopg2.connect(
        host=connection.POSTGRES_HOST,
        database=connection.POSTGRES_DATABASE,
        user=connection.POSTGRES_USER,
        password=connection.POSTGRES_PASSWORD,
    )

    conn.autocommit = True
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cars = get_cars(cursor, conn)
    print(f"Table before:\n{'-'*13}\n{cars}\n")
    insert_car(
        cursor,
        conn,
        brand=input("Insert car brand : "),
        old_year=int(input("How old is the car: ")),
        price=int(input("Enter the price of the car: ")),
    )

    cars = get_cars(cursor, conn)
    print(f"\nTable now:\n{'-'*10}\n{cars}\n")
    cursor.close()
    conn.close()
    print("1 = Closed conn. / 0 = Open conn.: ", "--", conn.closed, "--")

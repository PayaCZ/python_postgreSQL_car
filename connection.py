import os




POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "petulilinka")


POSTGRES_CONNECTION_STRING = os.getenv
("POSTGRES_CONNECTION_STRING", "dbname=car user=postgres password=petulilinka host=localhost port=5432")

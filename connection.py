import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="deposit",
        user='postgres',
        password="A0B1D9E2",
        host='localhost',
        port=5432
    )

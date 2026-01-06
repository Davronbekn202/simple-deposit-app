from connection import get_connection
from main import *

def table():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts(
        id serial PRIMARY KEY,
        email VARCHAR(150) UNIQUE NOT NULL,
        passvord VARCHAR(250) NOT NULL,
        )
    """)
    connect.commit()
    cursor.close()

def table2():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXIST card_info(
    id serial PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    end_date DATE,
    password VARCHAR(200),
    bank VARCHAR(50)
    """)
    connect.commit()
    cursor.close()

# table()
# table2()
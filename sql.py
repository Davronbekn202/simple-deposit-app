from connection import get_connection
from main import *

def table():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts(
        id serial PRIMARY KEY,
        email VARCHAR(150) UNIQUE NOT NULL,
        password VARCHAR(250) NOT NULL
        )
    """)
    connect.commit()
    cursor.close()
    print("account table created successfully")

def table2():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS card_info (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    end_date DATE,
    password VARCHAR(200),
    bank VARCHAR(50),
    account_id INT REFERENCES accounts(id)
)
    """)
    connect.commit()
    cursor.close()
    print("card_info table created successfully")
def chech_info():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
    SELECT
    email,
    password,
    CASE
        WHEN email IS NOT NULL AND password IS NOT NULL
        THEN 'malumot mavjud'
        ELSE 'malumot yo‘q'
    END AS checking
FROM accounts""")
def show_users():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
    SELECT * FROM accounts
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(f"id-{row[0]}, email-{row[1]}, password-{row[2]}")
def add_info(email_v,password_v):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
    INSERT INTO accounts(email,password)
    VALUES (%s,%s)""",(email_v,password_v))
    connect.commit()
    cursor.close()
# table()
# table2()
chech_info()
show_users()

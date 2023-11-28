

import sqlite3


def first_connection(hw_db):
    connection = sqlite3.connect(hw_db)
    return connection 

def create_table(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)

first_connection("Products")
products = """
CREATE TABLE IF NOT EXISTS products(
id  INTEGER PRIMARY KEY, 
product_title VARCHAR (200) NOT NULL,
price  DOUBLE (6,3) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0);"""




connection = first_connection("Products")
create_table(connection,products)


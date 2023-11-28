import sqlite3
def create_connection(names_list):
 connect = sqlite3.connect(names_list)
 return connect
  
def table (connect,sql):
 cursor = connect.cursor()
 cursor.execute(sql)

create_connection=("darika")
darika  =  """
CREATE TABLE IF NOT EXISTS  
(id TEXT PRIMARY KEY,
date of birth DATE NOT NULL
work VARCHAR (50) DEFAULT EMPTY
address TEXT NOT NULL);"""

connect = create_connection(f"darika")
table = (connect,darika)
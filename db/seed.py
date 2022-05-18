import os
import sqlite3

db_path = '../devTodosDB.db'
sql_tables = './sql/db_initial.sql'
sql_seed = './sql/db_seed.sql'

conn = sqlite3.connect(db_path)
cur = conn.cursor()

if os.path.exists(db_path):
    print('Database Already Exists.')
else:
    cur.executescript(sql_tables)
    cur.executescript(sql_seed)
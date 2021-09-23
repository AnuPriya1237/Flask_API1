import sqlite3

connection = sqlite3.connect('dbt.db')
cur = connection.cursor()
cur.execute('drop table if exists tab')
TABLE = """create table tab (
                           id integer primary key autoincrement,
                           start_time DATETIME not null,
                           end_time DATETIME not null
                           );
                           """

cur.execute(TABLE)
connection.close()

import sqlite3
def insert(start_time, end_time):
    connection = sqlite3.connect('dbt.db')
    cur = connection.cursor()
    cur.execute('insert into tab(start_time, end_time) values (?,?)',(start_time, end_time))

    connection.commit()
    connection.close()


def getdata():
    connection = sqlite3.connect('dbt.db')
    cur = connection.cursor()
    cur.execute('select * from tab')
    post = cur.fetchall()
    return post







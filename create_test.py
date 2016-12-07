import sqlite3
import string
import random
from utils import *

TESTVALS = 1000000

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_test_table():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    cleanup(c, "test")
    print("creating test table")
    try:
        sql_temp_table = "CREATE TABLE test(id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT);"
        c.execute(sql_temp_table)

        for x in range(0, TESTVALS):
            sql_line ="INSERT INTO test (val) VALUES ('" + id_generator() + "');"
            c.execute(sql_line)
        conn.commit()
        conn.close()
    except:
        print("Oh Noes")

if __name__ == "__main__":
    create_test_table()

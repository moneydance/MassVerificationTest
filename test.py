import os
import sys
sys.path.append(os.getcwd())
import sqlite3
import string
import random
from utils import *
from create_test import TESTVALS

# Query a 10th of the database
RETRIEVE = TESTVALS/10

def run_test():
    #Boiler Plate
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    try:
        # Create temp table
        sql_temp_table = "CREATE TABLE temp_test(id INTEGER PRIMARY KEY);"
        c.execute(sql_temp_table)

        # Populate temp table with simulated query values some of which are outside of the tables primary key range
        for x in random.sample(xrange(TESTVALS + TESTVALS/1000), RETRIEVE):
            sql_line ="INSERT INTO temp_test (id) VALUES (" + str(x) +");"
            c.execute(sql_line)

        # call join to get valid and invalid values back valid queries won't have null values.
        sql_join = "SELECT tt.id as q_id, t.id, t.val FROM temp_test tt LEFT OUTER JOIN test t ON tt.id = t.id;"
        c.execute(sql_join)

        # fetch results and print them
        results = c.fetchall()
        for result in results:
            pretty_print_dictionary(result)
        print("QUERY SIZE: " + str(RETRIEVE))
        print("TABLE SIZE: " + str(TESTVALS))
    except:
        print("oh noes")
    cleanup(c, "temp_test")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run_test()


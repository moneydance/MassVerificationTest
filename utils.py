def cleanup(c, table_name):
    try:
        c.execute("DROP TABLE " + table_name +";")
    except:
        print("Table" + table_name + " doesnt exist")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def pretty(d, indent=0):
    print_string = ""
    for key, value in d.iteritems():
        print_string += '\t' * indent + str(key)
        if isinstance(value, dict):
            print_string += '\n' + pretty(value, indent+1)
        else:
            print_string += ': ' + str(value) + ', '
    return print_string

def pretty_print_dictionary(d):
    print pretty(d)

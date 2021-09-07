from enum import Enum
import mysql.connector as mysql

class Option(Enum):
    CREATE_TABLE = 0
    INSERT_DATA = 1

action = Option.CREATE_TABLE
tables = {}

config = {
    'user': 'test',
    'password': 'dhkdls123',
    'host': '127.0.0.1',
    'database': 'mytestdb',
    'raise_on_warnings': True
}

cnx = mysql.connect(**config)
cursor = cnx.cursor()

if action == Option.CREATE_TABLE:
    with open('init.sql') as f:
        try:
            query_iter = cursor.execute(f.read(), multi=True)
            # [query for query in query_iter]
            for res in query_iter:
                print("Running query : ", res)
                print(f'Affected {res.rowcount} rows')
            cnx.commit()
        except mysql.Error as e:
            print("Error msg : ", e.msg)
        else:
            print("Successfully done")


    # check table data
    cursor.execute("SELECT * FROM airports")
    for idx, iata, city, country in cursor:
        print(idx, iata, city, country)

cursor.close()
cnx.close()


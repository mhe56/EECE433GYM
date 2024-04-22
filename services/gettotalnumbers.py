import psycopg2
from psycopg2 import Error
from helper_functions import query_sql

def get_total_numbers():
    print('k')
    try:
        data = {}
        query = lambda x: f"SELECT COUNT(*) FROM {x};"
        for x in ('Member', 'Coach', 'Branch', 'Nutritionist'):
            data[x] = query_sql(query(x))[0][0]
            print(data [x]) 
        return data

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)


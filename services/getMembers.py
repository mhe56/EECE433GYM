import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2

def get_members():
    try:
        query = "SELECT * FROM member;"
        data = query_sql(query)
        print(data)
        return data

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)

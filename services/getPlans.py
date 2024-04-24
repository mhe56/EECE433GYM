import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2

def get_plans():
    try:
        query = "SELECT * FROM plan;"
        data = query_sql(query)
        return data
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)

def add_plans(ID, Description, Calories, Coach_ID, Nutritionist_ID):
    query = "INSERT INTO plan (ID, Description, Calories, Coach_ID, Nutritionist_ID) VALUES (%s, %s, %s, %s, %s)"
    data = (ID, Description, Calories, Coach_ID, Nutritionist_ID)
    return query_sql(query, data)
import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2

def addBranch(x, y):
    query = "INSERT INTO Branch (ID, location) VALUES (%s, %s)"
    data = (int(x), y)
    return query_sql(query, data)

def getBranches():
    try:
        query = "SELECT Branch.ID, Branch.location, COUNT(DISTINCT Coach.ID) AS coach_count, COUNT(DISTINCT Nutritionist.ID) AS nutritionist_count FROM Branch LEFT JOIN Coach ON Branch.ID = Coach.branch_id LEFT JOIN Nutritionist ON Branch.ID = Nutritionist.branch_id GROUP BY Branch.ID, Branch.location;"
        data = query_sql(query)
        return data

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)




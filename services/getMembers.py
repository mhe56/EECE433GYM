import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2

def get_members():
    try:
        query = "SELECT * FROM member;"
        data = query_sql(query)
        return data
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)

def add_member(ID, Email, Age, Name, PhoneNumber, Plan_ID):
    query = "INSERT INTO member (ID, Email, Age, Name, PhoneNumber, Plan_ID) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (ID, Email, Age, Name, PhoneNumber, Plan_ID)
    return query_sql(query, data)

def insert_emergency(Coach_ID,Name,Relationship):
    query = f"INSERT INTO Emergency_Contact (Name , Member_ID, Relationship) VALUES ('{Coach_ID}', {Name}, '{Relationship}');"
    x = query_sql(query, insert=True)
    print(x)
    return x  
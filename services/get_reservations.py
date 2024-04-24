import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2

def addReservation(x, y, z):
    query = "INSERT INTO Member_Reservation (Member_ID, StartDate, DateTime) VALUES (%s, %s, %s)"
    data = (int(x), y, z)
    return query_sql(query, data)

def get_reservations(member_id):
    try:
        query = f"SELECT Member_ID, StartDate, DateTime FROM Member_Reservation WHERE Member_ID={member_id};"
        data = query_sql(query)
        return data

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
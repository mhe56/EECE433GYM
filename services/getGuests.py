import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2

def get_guests():
    try:
        query = "SELECT * FROM guest;"
        data = query_sql(query)
        return data
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)

def add_guest(ID, Name):
    query = "INSERT INTO guest (ID, Name) VALUES (%s, %s)"
    data = (ID, Name)
    return query_sql(query, data)

def get_reservations(guest_id):
    try:
        query = f"SELECT datetime FROM guest_reservation WHERE guest_id={guest_id};"
        data = query_sql(query)
        return data

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)


def addGUReservation(x, y):
    query = f"INSERT INTO Guest_Reservation (Datetime, Guest_ID) VALUES ('{x}',{y});"
    print('iiii')
    print(query)
    return query_sql(query, insert = True)
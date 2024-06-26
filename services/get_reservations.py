import psycopg2
from psycopg2 import Error
from helper_functions import query_sql
import psycopg2
from flask import flash

def addReservation(x, y, z):
    if (z[14:] != "00:00"):
        flash("You can only reserve in 1 hour intervals")
        return 
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

def start_time(x):
    query = f"SELECT StartDate FROM Membership WHERE Member_ID = {x}"
    return query_sql(query)
    
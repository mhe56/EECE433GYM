import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
import secrets


def connect():
    conn = psycopg2.connect(
        database="Project", user="postgres", password="12345678", host='127.0.0.1', port='5432'
    )
    return conn

def query_postgresql(sql, params=None):
        if (params):
            conn = connect()
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()
            conn.close()
        else:
            conn = connect()
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            conn.close()
            return rows
        
def select(name):
    sql = f"SELECT * FROM {name}"
    return query_postgresql(sql)
print(select('branch'))

def insert():    
        return render_template("insert.html", cc="Inserting into Database")

def insert_branch():
    ID = request.form['ID']
    location = request.form['location']
    query_postgresql('CALL insert_branch(%s,%s)', (ID, location))
    return redirect(url_for('insert'))

def insert_Nutritionist():
    ID = request.form['ID']
    name = request.form['name']
    Branch_ID = request.form['Branch_ID']
    query_postgresql('CALL insert_nutritionist(%s, %s, %s)', (ID, name, Branch_ID))
    return redirect(url_for('insert'))

def insert_Coach():
    ID = request.form['ID']
    name = request.form['name']
    Branch_ID = request.form['Branch_ID']
    age = request.form['age']
    years = request.form['years']
    query_postgresql('CALL insert_coach(%s, %s, %s, %s, %s)', (ID, name, age, years, Branch_ID))
    return redirect(url_for('insert'))

def insert_Plan():
    ID = request.form['ID']
    Description = request.form['Description']
    Calories = request.form['Calories']
    Coach_ID  = request.form['Coach_ID']
    Nutritionist_ID  = request.form['Nutritionist_ID']  # Correct the field name
    query_postgresql('CALL insert_plan(%s, %s, %s, %s, %s)', (ID, Description, Calories, Coach_ID, Nutritionist_ID))
    return redirect(url_for('insert'))



def insert_membership():
    Duration  = request.form['Duration']
    StartDate  = request.form['StartDate']
    Level   = request.form['Level']
    Member_ID  = request.form['Member_ID']
    query_postgresql('CALL insert_membership(%s, %s, %s, %s)', (Duration, StartDate, Level, Member_ID))
    return redirect(url_for('insert'))

def insert_Guest():
    ID = request.form['ID']
    name = request.form['name']
    query_postgresql('CALL insert_guest(%s, %s)', (ID, name))
    return redirect(url_for('insert'))

def insert_reservation_type():
    ID = request.form['ID']
    Type = request.form['Type']
    Capacity = request.form['Capacity']
    Branch_ID = request.form['Branch_ID']
    query_postgresql('CALL insert_reservation_type(%s, %s, %s, %s)', (ID, Type, Capacity, Branch_ID))
    return redirect(url_for('insert'))

def insert_member_reservation():
    Member_ID = request.form['Member_ID']
    StartDate = request.form['StartDate']
    DateTime = request.form['DateTime']
    query_postgresql('CALL insert_member_reservation(%s, %s, %s)', (Member_ID, StartDate, DateTime))
    return redirect(url_for('insert'))

def insert_guest_reservation():
    Guest_ID = request.form['Guest_ID']
    DateTime = request.form['DateTime']
    query_postgresql('CALL insert_guest_reservation(%s, %s)', (Guest_ID, DateTime))
    return redirect(url_for('insert'))

def insert_emergency_contact():
    Name = request.form['Name']
    Member_ID = request.form['Member_ID']
    Relationship = request.form['Relationship']
    query_postgresql('CALL insert_emergency_contact(%s, %s, %s)', (Name, Member_ID, Relationship))
    return redirect(url_for('insert'))

def insert_dependents():
    Coach_ID = request.form['Coach_ID']
    Name = request.form['Name']
    Relationship = request.form['Relationship']
    query_postgresql('CALL insert_dependents(%s, %s, %s)', (Coach_ID, Name, Relationship))
    return redirect(url_for('insert'))

def insert_reserve_appointment():
    Nutritionist_ID = request.form['Nutritionist_ID']
    Member_ID = request.form['Member_ID']
    DateTime = request.form['DateTime']
    query_postgresql('CALL insert_reserve_appointment(%s, %s, %s)', (Nutritionist_ID, Member_ID, DateTime))
    return redirect(url_for('insert'))

def insert_reserve_pt():
    DateTime = request.form['DateTime']
    Coach_ID = request.form['Coach_ID']
    Member_ID = request.form['Member_ID']
    query_postgresql('CALL insert_reserve_pt(%s, %s, %s)', (DateTime, Coach_ID, Member_ID))
    return redirect(url_for('insert'))







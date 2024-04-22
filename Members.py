import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
import secrets

def connect():
    conn = psycopg2.connect(
        database="LAB5", user="postgres", password="12345678", host='127.0.0.1', port='5432'
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
        
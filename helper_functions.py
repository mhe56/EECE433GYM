import psycopg2
from flask import flash
db_config = {
    'database': 'Project',
    'user': 'postgres',
    'password': '12345678',
    'host': '127.0.0.1',
    'port': '5432'
}
def query_sql(sql, params=None, insert=False):
    try:
        conn = psycopg2.connect(database=db_config['database'], user=db_config['user'], password=db_config['password'], host=db_config['host'], port=db_config['port'])
        if (params or insert):
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()
            conn.close()
        else:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            conn.commit()
            conn.close()
            return rows
    except Exception as error:
         flash("Error executing PostgreSQL query: " + str(error), 'error')

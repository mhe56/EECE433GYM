import psycopg2
db_config = {
    'database': 'Project',
    'user': 'postgres',
    'password': 'admin1234',
    'host': '127.0.0.1',
    'port': '5433'
}
def query_sql(sql, params=None):
    try:
        conn = psycopg2.connect(database=db_config['database'], user=db_config['user'], password=db_config['password'], host=db_config['host'], port=db_config['port'])
        if (params):
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()
            conn.close()
        else:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            conn.close()
            return rows
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)

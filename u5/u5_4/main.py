import psycopg2

def connect():
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="dbs", user="postgres", password="postgres")

        # create a cursor
        cur = conn.cursor()
        # execute a statement
        cur.execute('SELECT * FROM passagier')
        # display the statement
        print(cur.fetchone())
        # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def main():
    connect()

if __name__ == '__main__':
    main()

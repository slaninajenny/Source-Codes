import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_values(conn):
    """
    Query all rows in the sensordata table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM MaschinenStandort")

    rows = cur.fetchall()

    for row in rows:
        print(row)



def main():
    database = r"C:/path/to/file/test.db"

    # create a database connection
    conn = create_connection(database)
    with conn:

        print("ID aller Eintraege, deren values kleiner als 100 sind:")
        select_all_values(conn)


if __name__ == '__main__':
    main()

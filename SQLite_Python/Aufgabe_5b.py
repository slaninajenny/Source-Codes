import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_sensordata(conn, sensordata):
    """
    Create a new project into the sensordata table
    :param conn:
    :param sensordata:
    :return: sensordata id
    """
    sql = ''' INSERT INTO Maschinen(AlterInJahren)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, sensordata)
    return cur.lastrowid



def main():
    database = r"C:/path/to/file/test.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new sensor value
        sensordata = ('3');
        sensordata_id = create_sensordata(conn, sensordata)
        sensordata = ('4');
        sensordata_id = create_sensordata(conn, sensordata)
        sensordata = ('3');
        sensordata_id = create_sensordata(conn, sensordata)
        sensordata = ('2');
        sensordata_id = create_sensordata(conn, sensordata)
        sensordata = ('1');
        sensordata_id = create_sensordata(conn, sensordata)



if __name__ == '__main__':
    main()

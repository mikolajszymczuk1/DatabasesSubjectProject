# ====== Database utils for manage database (SQLite3) ======
from sqlite3 import Connection, connect

def create_connection(db_file: str) -> Connection | None:
    """
    create a database connection to the SQLite database specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = None

    try:
        conn = connect(db_file)
        return conn
    except Exception as e:
        print(f'Can not connect to database: {e}')

    return conn


def get_all_from_table(conn: Connection, table_name: str) -> list:
    """ Get all data from a table """

    query = f'SELECT * FROM {table_name}'
    result = conn.execute(query)
    return result.fetchall()

from . import db
from sqlite3 import Connection

def get_all_from_table(conn: Connection, table_name: str) -> list:
    """ Get all data from table with 'table_name' """

    return db.get_all_from_table(conn, table_name)


def get_athletes_data(conn: Connection) -> list:
    """ Get all athletes data with their experience"""

    return db.get_athletes_data(conn)

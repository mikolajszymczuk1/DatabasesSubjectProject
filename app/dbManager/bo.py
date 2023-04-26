from . import db
from sqlite3 import Connection

def get_all_from_table(conn: Connection, table_name: str) -> list:
    """ Get all data from table with 'table_name' """

    return db.get_all_from_table(conn, table_name)

import pytest
from os import path
from sqlite3 import Connection
from ..dbManager.db import create_connection

# Database config
DATABASE_NAME = 'sportAppDatabaseTest'
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
DB_TEST_PATH = path.join(BASE_DIR, f'data/{DATABASE_NAME}.db')

def create_connection() -> Connection | None:
    """
    Prepare the database:
    - Truncate all tables
    - Insert test data to all tables
    """

    return create_connection(DB_TEST_PATH)


def prepare_test_database(conn):
    print(conn)
    clear_all_tables_script = BASE_DIR
    print(clear_all_tables_script)

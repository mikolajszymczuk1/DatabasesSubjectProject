import pytest
from os import path
from sqlite3 import Connection
from ..db import create_connection

# Database config
DATABASE_NAME ='sportAppDatabaseTest'
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
DB_TEST_PATH = path.join(BASE_DIR, 'app', f'data/{DATABASE_NAME}.db')

@pytest.fixture
def prepare_database_and_get_conn() -> Connection:
    """
    Prepare the database:
    - Truncate all tables
    - Insert test data to all tables
    """

    conn = create_connection(DB_TEST_PATH)

    return conn

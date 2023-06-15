import pytest
from os import path
from sqlite3 import Connection
from ..dbManager.db import create_connection
from typing import Generator, Optional

# Database config
DATABASE_NAME: str = 'sportAppDatabaseTest'
BASE_DIR: str = path.dirname(path.dirname(path.abspath(__file__)))
DB_TEST_PATH: str = path.join(BASE_DIR, f'data/{DATABASE_NAME}.db')

@pytest.fixture(scope='session')
def db_connection() -> Generator[Optional[Connection], None, None]:
    """ Prepare database connection """

    conn: Connection | None = create_connection(DB_TEST_PATH)

    if conn is not None:
        yield conn
        conn.close()
    else:
        yield None


@pytest.fixture(scope='class', autouse=True)
def prepare_test_database(db_connection) -> None:
    """
    Prepare the database:
    - Truncate all tables
    - Insert test data to all tables
    """

    clear_all_tables_script_path: str = path.join(BASE_DIR, 'sql', 'clear_all_tables.sql')
    insert_test_data: str = path.join(BASE_DIR, 'sql', 'insert_test_data.sql')

    with open(clear_all_tables_script_path, 'r') as file:
        script: str = file.read()
        db_connection.executescript(script)
        file.close()

    with open(insert_test_data, 'r') as file:
        script = file.read()
        db_connection.executescript(script)
        file.close()

    db_connection.commit()

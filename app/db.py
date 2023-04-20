# ====== Database utils for manage database (SQLite3) ======
import sqlite3

# Tables
ATHLETE_TABLE = 'athlete'
EXERCISE_TYPE_TABLE = 'exerciseType'
EXERCISE_TABLE = 'exercise'
PLAN_TABLE = 'plan'


def create_connection(db_file: str) -> sqlite3.Connection | None:
    """
    create a database connection to the SQLite database specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(f'Can not connect to database: {e}')

    return conn

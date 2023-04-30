from . import db
from pandas import DataFrame
from sqlite3 import Connection

def get_all_from_table(conn: Connection, table_name: str) -> list:
    """ Get all data from table with 'table_name' """

    return db.get_all_from_table(conn, table_name)


def get_athletes_data(conn: Connection) -> DataFrame:
    """ Get all athletes data with their experience"""

    result = db.get_athletes_data(conn)
    df = DataFrame(result, columns=['ID', 'First Name', 'Last Name', 'Age', 'Weight', 'Gender', 'Skill Level'])
    return df


def get_athlete_exercises(conn: Connection, firstname: str, lastname: str) -> DataFrame:
    """ Get all athlete's exercises """

    result = db.get_athlete_exercises(conn, firstname, lastname)
    df = DataFrame(result, columns=['Exercise Name', 'Plan Name', 'Sets', 'Reps Per Set'])
    return df

from . import db
from pandas import DataFrame
from sqlite3 import Connection

def get_all_from_table(conn: Connection, table_name: str) -> list:
    """ Get all data from table with 'table_name' """

    return db.get_all_from_table(conn, table_name)


def get_max_id_from_table(conn: Connection, table_name: str, id_column_name: str) -> int:
    """ Return maximum id from table """

    return db.get_max_id_from_table(conn, table_name, id_column_name)


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


def get_single_athlete_data(conn: Connection, firstname: str, lastname: str) -> tuple:
    """ Get data for a single athlete """

    result = db.get_single_athlete_data(conn, firstname, lastname)
    return result


def create_exercise_for_athlete(conn: Connection, firstname: str, lastname: str, planID: int, exerciseTypeID: int, setsCount: int, repsPerSetCount: int) -> None:
    """ Create new exercise record """

    new_exercise_id: int = get_max_id_from_table(conn, 'exercise', 'exerciseID') + 1
    athlete_id = get_single_athlete_data(conn, firstname, lastname)[0]
    db.create_exercise_for_athlete(conn, new_exercise_id, athlete_id, planID, exerciseTypeID, setsCount, repsPerSetCount)

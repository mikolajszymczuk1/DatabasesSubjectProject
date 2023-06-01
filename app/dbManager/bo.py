from . import db
from pandas import DataFrame
from sqlite3 import Connection

def get_all_from_table(conn: Connection, table_name: str) -> list:
    """
    Get all data from the table.

    :param conn: The database connection.
    :type conn: Connection
    :param table_name: The name of the table.
    :type table_name: str
    :return: A list containing all the data from the table.
    :rtype: list
    """

    return db.get_all_from_table(conn, table_name)


def get_max_id_from_table(conn: Connection, table_name: str, id_column_name: str) -> int:
    """
    Return the maximum ID from the table.

    :param conn: The database connection.
    :type conn: Connection
    :param table_name: The name of the table.
    :type table_name: str
    :param id_column_name: The name of the ID column.
    :type id_column_name: str
    :return: The maximum ID from the table.
    :rtype: int
    """

    return db.get_max_id_from_table(conn, table_name, id_column_name)


def get_athletes_data(conn: Connection) -> DataFrame:
    """
    Get all athletes data with their experience.

    :param conn: The database connection.
    :type conn: Connection
    :return: A DataFrame containing athletes' data.
    :rtype: DataFrame
    """

    result = db.get_athletes_data(conn)
    df = DataFrame(result, columns=['ID', 'First Name', 'Last Name', 'Age', 'Weight', 'Gender', 'Skill Level'])
    return df


def get_athlete_exercises(conn: Connection, firstname: str, lastname: str) -> DataFrame:
    """
    Get all athlete's exercises.

    :param conn: The database connection.
    :type conn: Connection
    :param firstname: The first name of the athlete.
    :type firstname: str
    :param lastname: The last name of the athlete.
    :type lastname: str
    :return: A DataFrame containing athlete's exercises.
    :rtype: DataFrame
    """

    result = db.get_athlete_exercises(conn, firstname, lastname)
    df = DataFrame(result, columns=['Exercise Name', 'Plan Name', 'Sets', 'Reps Per Set'])
    return df


def get_single_athlete_data(conn: Connection, firstname: str, lastname: str) -> tuple:
    """
    Get data for a single athlete.

    :param conn: The database connection.
    :type conn: Connection
    :param firstname: The first name of the athlete.
    :type firstname: str
    :param lastname: The last name of the athlete.
    :type lastname: str
    :return: A tuple containing data for the athlete.
    :rtype: tuple
    """

    result = db.get_single_athlete_data(conn, firstname, lastname)
    return result


def create_exercise_for_athlete(conn: Connection, firstname: str, lastname: str, plan_id: int, exercise_type_id: int, sets_count: int, reps_per_set_count: int) -> None:
    """
    Create a new exercise record.

    :param conn: The database connection.
    :type conn: Connection
    :param firstname: The first name of the athlete.
    :type firstname: str
    :param lastname: The last name of the athlete.
    :type lastname: str
    :param plan_id: The ID of the exercise plan.
    :type plan_id: int
    :param exercise_type_id: The ID of the exercise type.
    :type exercise_type_id: int
    :param sets_count: The number of sets.
    :type sets_count: int
    :param reps_per_set_count: The number of repetitions per set.
    :type reps_per_set_count: int
    :return: None
    """

    new_exercise_id: int = get_max_id_from_table(conn, 'exercise', 'exerciseID') + 1
    athlete_id = get_single_athlete_data(conn, firstname, lastname)[0]
    db.create_exercise_for_athlete(conn, new_exercise_id, athlete_id, plan_id, exercise_type_id, sets_count, reps_per_set_count)

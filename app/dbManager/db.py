# ====== Database utils for manage database (SQLite3) ======
from sqlite3 import Connection, connect, Error
from typing import Optional

def create_connection(db_file: str) -> Optional[Connection]:
    """
    Create a database connection to the SQLite database specified by the db_file.

    :param db_file: The path to the database file.
    :type db_file: str
    :return: A Connection object or None.
    :rtype: Optional[Connection]
    """

    conn = None

    try:
        conn = connect(db_file)
        return conn
    except Error as e:
        print(f'Can not connect to database: {e}')

    return conn


def get_all_from_table(conn: Connection, table_name: str) -> list:
    """
    Get all data from a table.

    :param conn: The database connection.
    :type conn: Connection
    :param table_name: The name of the table.
    :type table_name: str
    :return: A list containing all the data from the table.
    :rtype: list
    """

    query = f'SELECT * FROM {table_name}'
    result = conn.execute(query)
    return result.fetchall()


def get_max_id_from_table(conn: Connection, table_name: str, id_column_name: str) -> int:
    """
    Return the maximum ID from a table.

    :param conn: The database connection.
    :type conn: Connection
    :param table_name: The name of the table.
    :type table_name: str
    :param id_column_name: The name of the ID column.
    :type id_column_name: str
    :return: The maximum ID value.
    :rtype: int
    """

    query = f'SELECT MAX({id_column_name}) FROM {table_name};'
    result = conn.execute(query)
    return result.fetchone()[0]


def get_athletes_data(conn: Connection) -> list:
    """
    Get all athletes from a table with their experience level.

    :param conn: The database connection.
    :type conn: Connection
    :return: A list of tuples containing athlete data.
    :rtype: list
    """

    query = '''
        SELECT athleteID, firstName, lastName, age, athleteWeight, gender, experienceLevel
        FROM Athlete INNER JOIN Experience on Athlete.athleteID = Experience.experienceID;
    '''

    result = conn.execute(query)
    return result.fetchall()


def get_athlete_exercises(conn: Connection, firstname: str, lastname: str) -> list:
    """
    Get all exercises for a specific athlete.

    :param conn: The database connection.
    :type conn: Connection
    :param firstname: The first name of the athlete.
    :type firstname: str
    :param lastname: The last name of the athlete.
    :type lastname: str
    :return: A list of tuples containing exercise data.
    :rtype: list
    """

    query = f'''
        SELECT exerciseTypeName, planName, setsCount, repsPerSetCount
        FROM Exercise INNER JOIN Athlete ON Athlete.athleteID = Exercise.athleteID
        INNER JOIN Plan ON Plan.planID = Exercise.planID
        INNER JOIN ExerciseType ON ExerciseType.exerciseTypeID = Exercise.exerciseTypeID
        WHERE firstName = '{firstname}' AND lastname = '{lastname}';
    '''

    result = conn.execute(query)
    return result.fetchall()


def get_single_athlete_data(conn: Connection, firstname: str, lastname: str) -> tuple:
    """
    Get data for a single athlete.

    :param conn: The database connection.
    :type conn: Connection
    :param firstname: The first name of the athlete.
    :type firstname: str
    :param lastname: The last name of the athlete.
    :type lastname: str
    :return: A tuple containing the athlete data.
    :rtype: tuple
    """

    query = f'''
        SELECT athleteID, firstName, lastName, age, athleteWeight, gender, experienceLevel
        FROM Athlete INNER JOIN Experience on Athlete.athleteID = Experience.experienceID
        WHERE firstName = '{firstname}' AND lastName = '{lastname}';
    '''

    result = conn.execute(query)
    return result.fetchone()


def create_exercise_for_athlete(conn: Connection, exercise_id: int, athlete_id: int, plan_id: int, exercise_type_id: int, sets_count: int, reps_per_set_count: int) -> None:
    """
    Create a new exercise record.

    :param conn: The database connection.
    :type conn: Connection
    :param exercise_id: The ID of the exercise.
    :type exercise_id: int
    :param athlete_id: The ID of the athlete.
    :type athlete_id: int
    :param plan_id: The ID of the plan.
    :type plan_id: int
    :param exercise_type_id: The ID of the exercise type.
    :type exercise_type_id: int
    :param sets_count: The number of sets.
    :type sets_count: int
    :param reps_per_set_count: The number of repetitions per set.
    :type reps_per_set_count: int
    :return: None
    :rtype: None
    """

    query = f'''
        INSERT INTO Exercise (exerciseID, athleteID, planID, exerciseTypeID, setsCount, repsPerSetCount)
            VALUES ({exercise_id}, {athlete_id}, {plan_id}, {exercise_type_id}, {sets_count}, {reps_per_set_count});
    '''

    conn.execute(query)
    conn.commit()

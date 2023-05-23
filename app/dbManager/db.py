# ====== Database utils for manage database (SQLite3) ======
from sqlite3 import Connection, connect, Error
from typing import Optional

def create_connection(db_file: str) -> Optional[Connection]:
    """
    create a database connection to the SQLite database specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """

    conn = None

    try:
        conn = connect(db_file)
        return conn
    except Error as e:
        print(f'Can not connect to database: {e}')

    return conn


def get_all_from_table(conn: Connection, table_name: str) -> list:
    """ Get all data from a table """

    query = f'SELECT * FROM {table_name}'
    result = conn.execute(query)
    return result.fetchall()


def get_max_id_from_table(conn: Connection, table_name: str, id_column_name: str) -> int:
    """ Return maximum id from table """

    query = f'SELECT MAX({id_column_name}) FROM {table_name};'
    result = conn.execute(query)
    return result.fetchone()[0]


def get_athletes_data(conn: Connection) -> list:
    """ Get all athletes from a table with their experience level """

    query = '''
        SELECT athleteID, firstName, lastName, age, athleteWeight, gender, experienceLevel
        FROM Athlete INNER JOIN Experience on Athlete.athleteID = Experience.experienceID;
    '''

    result = conn.execute(query)
    return result.fetchall()


def get_athlete_exercises(conn: Connection, firstname: str, lastname: str) -> list:
    """ Get all athlete's exercises """

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
    """ Get data for a single athlete """

    query = f'''
        SELECT athleteID, firstName, lastName, age, athleteWeight, gender, experienceLevel
        FROM Athlete INNER JOIN Experience on Athlete.athleteID = Experience.experienceID
        WHERE firstName = '{firstname}' AND lastName = '{lastname}';
    '''

    result = conn.execute(query)
    return result.fetchone()


def create_exercise_for_athlete(conn: Connection, exercise_id: int, athlete_id: int, plan_id: int, exercise_type_id: int, sets_count: int, reps_per_set_count: int) -> None:
    """ Create new exercise record """

    query = f'''
        INSERT INTO Exercise (exerciseID, athleteID, planID, exerciseTypeID, setsCount, repsPerSetCount)
            VALUES ({exercise_id}, {athlete_id}, {plan_id}, {exercise_type_id}, {sets_count}, {reps_per_set_count});
    '''

    conn.execute(query)
    conn.commit()

import pytest
from sqlite3 import Connection
from ..dbManager.db import (
    get_all_from_table, get_athletes_data,
    get_max_id_from_table, get_athlete_exercises,
    get_single_athlete_data, create_exercise_for_athlete,
    create_athlete
)
from .fixtures import db_connection, prepare_test_database
from ..enums.TablesEnum import TablesEnum

@pytest.mark.usefixtures('prepare_test_database')
class TestDB:
    def test_get_all_from_table(self, db_connection: Connection) -> None:
        # GIVEN
        expected = [
            (1, 'Regular pushups'),
            (2, 'Wide pushups'),
            (3, 'Bench press'),
            (4, 'Squats with elevated legs')
        ]

        # WHEN
        result = get_all_from_table(db_connection, TablesEnum.EXERCISE_TYPE_TABLE.value)

        # THEN
        assert len(result) == len(expected)
        assert result == expected

    def test_get_max_id_from_table(self, db_connection: Connection) -> None:
        # GIVEN
        expected = 4

        # WHEN
        result: int = get_max_id_from_table(db_connection, TablesEnum.EXERCISE_TABLE.value, 'exerciseID')

        # THEN
        assert result == expected

    def test_get_athletes_data(self, db_connection: Connection) -> None:
        # GIVEN
        expected = [
            (1, 'John', 'Doe', 25, 66, 'Male', 'Advanced'),
            (2, 'Jane', 'Doe', 28, 86, 'Female', 'Intermediate'),
            (3, 'Michael', 'Johnson', 55, 190, 'Male', 'Elite'),
            (4, 'Sarah', 'Lee', 23, 90, 'Female', 'Beginner')
        ]

        # WHEN
        result = get_athletes_data(db_connection)

        # THEN
        assert len(result) == len(expected)
        assert result == expected

    def test_get_athlete_exercises(self, db_connection: Connection) -> None:
        # GIVEN
        expected = [
            ('Regular pushups', 'Weight Loss Plan', 3, 10),
            ('Wide pushups', 'Weight Loss Plan', 3, 10)
        ]

        test_firstname = 'John'
        test_lastname = 'Doe'

        # WHEN
        result = get_athlete_exercises(db_connection, test_firstname, test_lastname)

        # THEN
        assert len(result) == len(expected)
        assert result == expected

    def test_get_single_athlete_data(self, db_connection: Connection) -> None:
        # GIVEN
        expected = (1, 'John', 'Doe', 25, 66, 'Male', 'Advanced')
        test_firstname = 'John'
        test_lastname = 'Doe'

        # WHEN
        result = get_single_athlete_data(db_connection, test_firstname, test_lastname)

        # THEN
        assert result != []
        assert result == expected

    def test_create_exercise_for_athlete(self, db_connection: Connection) -> None:
        # GIVEN
        exercise_id: int = get_max_id_from_table(db_connection, 'exercise', 'exerciseID') + 1
        athlete_id: int = 1
        plan_id: int = 1
        exercise_type_id: int = 1
        sets_count: int = 5
        reps_count: int = 12

        test_firstname: str = 'John'
        test_lastname: str = 'Doe'

        # WHEN
        create_exercise_for_athlete(db_connection, exercise_id, athlete_id, plan_id, exercise_type_id, sets_count, reps_count)

        # THEN
        expected = [
            ('Regular pushups', 'Weight Loss Plan', 3, 10),
            ('Wide pushups', 'Weight Loss Plan', 3, 10),
            ('Regular pushups', 'Weight Loss Plan', 5, 12)
        ]

        exercises = get_athlete_exercises(db_connection, test_firstname, test_lastname)
        assert len(exercises) == len(expected)
        assert exercises == expected

    def test_create_athlete(self, db_connection: Connection) -> None:
        # GIVEN
        athlete_id: int = get_max_id_from_table(db_connection, 'athlete', 'athleteID') + 1
        firstname: str = 'Michael'
        lastname: str = 'Wan'
        age: int = 24
        weight: int = 66
        gender: str = 'Male'
        experience_id: int = 2

        # WHEN
        create_athlete(db_connection, athlete_id, firstname, lastname, age, weight, gender, experience_id)

        # THEN
        expected = [
            (1, 'John', 'Doe', 25, 66, 'Male', 'Advanced'),
            (2, 'Jane', 'Doe', 28, 86, 'Female', 'Intermediate'),
            (3, 'Michael', 'Johnson', 55, 190, 'Male', 'Elite'),
            (4, 'Sarah', 'Lee', 23, 90, 'Female', 'Beginner'),
            (5, 'Michael', 'Wan', 24, 66, 'Male', 'Intermediate')
        ]

        athletes = get_athletes_data(db_connection)
        assert len(athletes) == len(expected)
        assert athletes == expected

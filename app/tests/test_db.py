import pytest
from sqlite3 import Connection
from ..dbManager.db import (
    get_all_from_table, get_athletes_data,
    get_max_id_from_table, get_athlete_exercises,
    get_single_athlete_data, create_exercise_for_athlete
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
            (1, 'John', 'Doe', 25, 66, 'Male', 'Beginner'),
            (2, 'Jane', 'Doe', 28, 86, 'Female', 'Intermediate'),
            (3, 'Michael', 'Johnson', 55, 190, 'Male', 'Advanced'),
            (4, 'Sarah', 'Lee', 23, 90, 'Female', 'Elite')
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
        expected = (1, 'John', 'Doe', 25, 66, 'Male', 'Beginner')
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
        athlete_id = 1
        plan_id = 1;
        exercise_type_id = 1
        sets_count = 5
        reps_count = 12

        test_firstname = 'John'
        test_lastname = 'Doe'

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

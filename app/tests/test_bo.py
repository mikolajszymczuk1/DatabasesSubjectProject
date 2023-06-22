import pytest
from sqlite3 import Connection
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from ..dbManager.bo import (
    get_all_from_table,
    get_athletes_data,
    get_athlete_exercises,
    get_max_id_from_table,
    get_single_athlete_data,
    create_exercise_for_athlete,
    create_athlete
)
from .fixtures import db_connection, prepare_test_database
from ..enums.TablesEnum import TablesEnum

@pytest.mark.usefixtures('prepare_test_database')
class TestBO:
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
        assert result == expected

    def test_get_max_id_from_table(self, db_connection: Connection) -> None:
        # GIVEN
        table_name: str = TablesEnum.EXERCISE_TYPE_TABLE.value
        id_column_name: str = 'exerciseTypeID'
        expected_id: int = 4

        # WHEN
        result: int = get_max_id_from_table(db_connection, table_name, id_column_name)

        # THEN
        assert result == expected_id

    def test_get_athletes_data(self, db_connection: Connection) -> None:
        # GIVEN
        data = [
            (1, 'John', 'Doe', 25, 66, 'Male', 'Advanced'),
            (2, 'Jane', 'Doe', 28, 86, 'Female', 'Intermediate'),
            (3, 'Michael', 'Johnson', 55, 190, 'Male', 'Elite'),
            (4, 'Sarah', 'Lee', 23, 90, 'Female', 'Beginner')
        ]

        expected: DataFrame = DataFrame(data, columns=['ID', 'First Name', 'Last Name', 'Age', 'Weight', 'Gender', 'Skill Level'])

        # WHEN
        result: DataFrame = get_athletes_data(db_connection)

        # THEN
        assert_frame_equal(result, expected)

    def test_get_athlete_exercises(self, db_connection: Connection) -> None:
        # GIVEN
        test_firstname: str = 'John'
        test_lastname: str = 'Doe'

        data = [
            ('Regular pushups', 'Weight Loss Plan', 3, 10),
            ('Wide pushups', 'Weight Loss Plan', 3, 10)
        ]

        expected = DataFrame(data, columns=['Exercise Name', 'Plan Name', 'Sets', 'Reps Per Set'])

        # WHEN
        result = get_athlete_exercises(db_connection, test_firstname, test_lastname)

        # THEN
        assert_frame_equal(result, expected)

    def test_get_single_athlete_data(self, db_connection: Connection) -> None:
        # GIVEN
        firstname: str = 'John'
        lastname: str = 'Doe'
        expected = (1, 'John', 'Doe', 25, 66, 'Male', 'Advanced')

        # WHEN
        result = get_single_athlete_data(db_connection, firstname, lastname)

        # THEN
        assert result == expected

    def test_create_exercise_for_athlete(self, db_connection: Connection) -> None:
        # GIVEN
        firstname: str = 'John'
        lastname: str = 'Doe'
        plan_id: int = 1
        exercise_type_id: int = 1
        sets_count: int = 2
        reps_per_set_count: int = 10

        data = [
            ('Regular pushups', 'Weight Loss Plan', 3, 10),
            ('Wide pushups', 'Weight Loss Plan', 3, 10),
            ('Regular pushups', 'Weight Loss Plan', 2, 10)
        ]

        expected: DataFrame = DataFrame(data, columns=['Exercise Name', 'Plan Name', 'Sets', 'Reps Per Set'])

        # WHEN
        create_exercise_for_athlete(db_connection, firstname, lastname, plan_id, exercise_type_id, sets_count, reps_per_set_count)

        # THEN
        exercises: DataFrame = get_athlete_exercises(db_connection, firstname, lastname)
        assert_frame_equal(exercises, expected)

    def test_create_athlete(self, db_connection: Connection) -> None:
        # GIVEN
        firstname: str = 'Michael'
        lastname: str = 'Wan'
        age: int = 24
        weight: int = 66
        gender: str = 'Male'
        experience_id: int = 2

        data = [
            (1, 'John', 'Doe', 25, 66, 'Male', 'Advanced'),
            (2, 'Jane', 'Doe', 28, 86, 'Female', 'Intermediate'),
            (3, 'Michael', 'Johnson', 55, 190, 'Male', 'Elite'),
            (4, 'Sarah', 'Lee', 23, 90, 'Female', 'Beginner'),
            (5, 'Michael', 'Wan', 24, 66, 'Male', 'Intermediate')
        ]

        expected: DataFrame = DataFrame(data, columns=['ID', 'First Name', 'Last Name', 'Age', 'Weight', 'Gender', 'Skill Level'])

        # WHEN
        create_athlete(db_connection, firstname, lastname, age, weight, gender, experience_id)

        # THEN
        athletes: DataFrame = get_athletes_data(db_connection)
        assert_frame_equal(athletes, expected)

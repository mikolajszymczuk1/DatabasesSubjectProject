import pytest
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from ..dbManager.bo import get_all_from_table, get_athletes_data, get_athlete_exercises
from .fixtures import db_connection, prepare_test_database
from ..enums.TablesEnum import TablesEnum

@pytest.mark.usefixtures('prepare_test_database')
class TestBO:
    def test_get_all_from_table(self, db_connection):
        expected = [
            (1, 'Regular pushups'),
            (2, 'Wide pushups'),
            (3, 'Bench press'),
            (4, 'Squats with elevated legs')
        ]

        result = get_all_from_table(db_connection, TablesEnum.EXERCISE_TYPE_TABLE.value)
        assert result == expected

    def test_get_athletes_data(self, db_connection):
        data = [
            (1, 'John', 'Doe', 25, 66, 'Male', 'Beginner'),
            (2, 'Jane', 'Doe', 28, 86, 'Female', 'Intermediate'),
            (3, 'Michael', 'Johnson', 55, 190, 'Male', 'Advanced'),
            (4, 'Sarah', 'Lee', 23, 90, 'Female', 'Elite')
        ]

        expected = DataFrame(data, columns=['ID', 'First Name', 'Last Name', 'Age', 'Weight', 'Gender', 'Skill Level'])
        result = get_athletes_data(db_connection)
        assert_frame_equal(result, expected)

    def test_get_athlete_exercises(self, db_connection):
        test_firstname = 'John'
        test_lastname = 'Doe'

        data = [
            ('Regular pushups', 'Weight Loss Plan', 3, 10),
            ('Wide pushups', 'Weight Loss Plan', 3, 10)
        ]

        expected = DataFrame(data, columns=['Exercise Name', 'Plan Name', 'Sets', 'Reps Per Set'])
        result = get_athlete_exercises(db_connection, test_firstname, test_lastname)
        assert_frame_equal(result, expected)

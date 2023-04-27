import pytest
from ..dbManager.db import get_all_from_table, get_athletes_data
from .fixtures import db_connection, prepare_test_database
from ..enums.TablesEnum import TablesEnum

@pytest.mark.usefixtures('prepare_test_database')
class TestDB:
    def test_get_all_from_table(self, db_connection):
        expected = [
            (1, 'Regular pushups'),
            (2, 'Wide pushups'),
            (3, 'Bench press'),
            (4, 'Squats with elevated legs')
        ]

        result = get_all_from_table(db_connection, TablesEnum.EXERCISE_TYPE_TABLE.value)
        assert len(result) == len(expected)
        assert result == expected

    def test_get_athletes_data(self, db_connection):
        expected = [
            (1, 'John', 'Doe', 25, 66, 'Male', 'Beginner'),
            (2, 'Jane', 'Doe', 28, 86, 'Female', 'Intermediate'),
            (3, 'Michael', 'Johnson', 55, 190, 'Male', 'Advanced'),
            (4, 'Sarah', 'Lee', 23, 90, 'Female', 'Elite')
        ]

        result = get_athletes_data(db_connection)
        assert len(result) == len(expected)
        assert result == expected

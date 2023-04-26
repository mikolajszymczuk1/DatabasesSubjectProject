
from ..dbManager.db import get_all_from_table
from .fixtures import create_connection, prepare_test_database
from ..enums.TablesEnum import TablesEnum

class TestDB:
    @staticmethod
    def setup_class(testData):
        prepare_test_database(create_connection)
        testData.conn = create_connection()

    def test_get_all_from_table(self, testData):
        expected = [
            (1, 'Regular pushups'),
            (2, 'Wide pushups'),
            (3, 'Bench press'),
            (4, 'Squats with elevated legs')
        ]

        result = get_all_from_table(testData.conn, TablesEnum.EXERCISE_TYPE_TABLE.value)
        assert result == expected

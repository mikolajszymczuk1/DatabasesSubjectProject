from os import path
from dbManager.db import create_connection
from dbManager.bo import get_all_from_table
from enums.TablesEnum import TablesEnum

# Database config
DATABASE_NAME ='sportAppDatabase'
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
DB_PATH = path.join(BASE_DIR, 'app', f'data/{DATABASE_NAME}.db')

# Create database connection
conn = create_connection(DB_PATH)

all_exercise_types = get_all_from_table(conn, TablesEnum.EXERCISE_TYPE_TABLE.value)
print(all_exercise_types)

conn.close()

# Created by Chat GPT 4   !!! NOT COMMERSIAL !!!

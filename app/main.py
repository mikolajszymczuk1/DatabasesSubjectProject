from os import path
from db import create_connection

# Database config
DATABASE_NAME ='sportAppDatabase'
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
DB_PATH = path.join(BASE_DIR, 'app', f'data/{DATABASE_NAME}.db')

# Create database connection
conn = create_connection(DB_PATH)
print('Connected to database !')

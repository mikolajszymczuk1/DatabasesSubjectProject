from os import path
from dbManager.db import create_connection
from UserDBManager.UserDBManager import UserDBManager

# Database config
DATABASE_NAME = 'sportAppDatabase'
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
DB_PATH = path.join(BASE_DIR, 'app', f'data/{DATABASE_NAME}.db')


def main() -> None:
    # Create database connection
    conn = create_connection(DB_PATH)

    if conn is not None:
        userDBManager = UserDBManager(conn)
        userDBManager.run()
        conn.close()
    else:
        print('Error !')


if __name__ == '__main__':
    main()

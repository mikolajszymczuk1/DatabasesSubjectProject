# Sport app
## Project for Database subject
Simple project with backend and client side where you can menage athletes and gym exercises in different categories.

---

## Project tech stack

- Database: ```SqlLite```
- Testing: ```PyTest```
- Data modifications: ```Pandas```
- Documentation generating: ```Sphinx```

---

## Project structure

```db.py``` and ```bo.py``` are important things in project,
in first one there are all queries to database and in second one there are all handlers for db queries functions with additional functionality.

Example db/bo:

db

```py
def get_all_from_table(conn: Connection, table_name: str) -> list:
    """
    Get all data from a table.

    :param conn: The database connection.
    :type conn: Connection
    :param table_name: The name of the table.
    :type table_name: str
    :return: A list containing all the data from the table.
    :rtype: list
    """

    query = f'SELECT * FROM {table_name}' # <--- Query to execute
    result = conn.execute(query)          # <--- Result from executed query
    return result.fetchall()
```

bo

```py
def get_all_from_table(conn: Connection, table_name: str) -> list:
    """
    Get all data from the table.

    :param conn: The database connection.
    :type conn: Connection
    :param table_name: The name of the table.
    :type table_name: str
    :return: A list containing all the data from the table.
    :rtype: list
    """

    return db.get_all_from_table(conn, table_name)
```

---

## Project setup

### 1) Clone project

---

### 2) Create virtual environment in project directory

```sh
python3 -m venv env
```

and activate virtual environment

```sh
source ./env/bin/activate
```

---

### 3) Install all dependencies

```sh
pip install -r requirements.txt
```

### 4) Run app

```sh
python app/main.py
```

---

## Testing

In project there are two sqlite databases: ```sportAppDatabase``` and ```sportAppDatabaseTest```

You can run test with command:

```sh
pytest
```
or

```sh
pytest -v
```

---

## Documentation

Each important function has full description with examples and parameters types etc. You can generate sphinx documentation with command:

```sh
sphinx-build -b html . build
```

After that you should see documentation as html page in ```build``` directory.

Only what you must to do is open index.html in browser.

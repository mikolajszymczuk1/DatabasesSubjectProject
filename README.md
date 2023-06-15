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

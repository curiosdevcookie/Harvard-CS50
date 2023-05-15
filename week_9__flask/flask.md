# Flask

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program.

Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.

## Files in a project

Speaking of files in a project, Flask needs to find `app.py` or `wsgi.py` in the root directory of the project. If you want to use a different filename, you need to set the `FLASK_APP` environment variable to the filename you want to use. For example, if you want to use `hello.py` as the filename, you need to run `export FLASK_APP=hello.py` in the terminal before running `flask run`.

Also, it needs a `templates` directory in the root directory of the project. Flask will look for HTML files in the `templates` directory.

Also, it needs a `static` directory in the root directory of the project. Flask will look for CSS files, JavaScript files, and image files in the `static` directory.

Also, a project needs a `requirements.txt` file in the root directory of the project. This file contains a list of all the packages that are required to run the project. You can generate this file by running `pip freeze > requirements.txt` in the terminal.

## Load a database

To load a database in your Python code, you need to import the `sqlite3` module. Then, you need to connect to the database. Then, you need to create a cursor. A cursor is a cursor object with the following properties:

- `cursor.execute()` - Executes an SQL statement.
- `cursor.executemany()` - Executes an SQL statement multiple times.
- `cursor.fetchone()` - Fetches the next row of a query result set.
- `cursor.fetchmany()` - Fetches the next set of rows of a query result, returning a list.
- `cursor.fetchall()` - Fetches all remaining rows of a query result, returning a list.

Then, you need to execute a SQL query. Then, you need to commit the changes. Then, you need to close the connection.

```python
import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL)")
conn.commit()
conn.close()
```

## Using Flask

To use Flask in your Python code, you need to import the `flask` module. Then, you need to create an instance of the `Flask` class. Then, you need to define a route. Then, you need to define a function that returns a string. Then, you need to run the app.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"
````

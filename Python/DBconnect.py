import sqlite3

# create table
def createTable():
    createTableSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/createTable.sql'

    with open(createTableSQL, 'r') as fileProcess:
        sql = fileProcess.read()

    sql_statements = [
        sql
    ]

    try:
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()

            for statement in sql_statements:
                cursor.execute(statement)

            conn.commit()

            print(f"Tables created successfully using SQLLite version {sqlite3.sqlite_version}")

    except sqlite3.OperationalError as e:
        print("Oh no! Error:", e)

# populate created table
def populateTable():
    populateTableSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/populateTable.sql'

    with open(populateTableSQL, 'r') as fileProcess:
        sql = fileProcess.read()

    sql_statements = [
        sql
    ]

    try:
        with sqlite3.connect("data.db") as conn:
            cursor = conn.cursor()

            for statement in sql_statements:
                cursor.execute(statement)

            conn.commit()

            print(f"Tables created successfully using SQLLite version {sqlite3.sqlite_version}")

    except sqlite3.OperationalError as e:
        print("Oh no! Error:", e)
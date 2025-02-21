import sqlite3
from string import Template
import os

db_path = os.path.join(os.path.dirname(__file__), "data.db")

# create table
def createTable(tblName, colName, colType):

    createTableSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/createTable.sql'
    
    with open(createTableSQL, 'r') as fileProcess:
        sql = fileProcess.read()
    
    # Substitute the placeholders with the actual values from the GUI
    query = Template(sql).substitute(
        table_name=tblName,
        col1=colName,
        col1Type=colType
    )
    
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print(f"Table created successfully using SQLite version {sqlite3.sqlite_version}")
    except sqlite3.OperationalError as e:
        print("Oh no! Error:", e)

# populate created table
def populateTable(tblName, colName, colValues):

    populateTableSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/populateTable.sql'

    with open(populateTableSQL, 'r') as fileProcess:
        sql = fileProcess.read()

    query = Template(sql).substitute(
        table_name=tblName,
        col1=colName,
        value1=colValues
    )

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print(f"Tables populated successfully!")

    except sqlite3.OperationalError as e:
        print("Oh no! Error:", e)

# select * from the table
def selectSQL(tblName):

    selectSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/selectSQL.sql'

    with open(selectSQL, 'r') as fileProcess:
        sql = fileProcess.read()

    query = Template(sql).substitute(
        table_name=tblName
    )

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print(f"SELECT executed successfully! Query = " + "`" + query + "`")

    except sqlite3.OperationalError as e:
        print("Oh no! Error:", e)

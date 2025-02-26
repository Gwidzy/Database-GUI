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

# rename table
def renameTbl(tblName,tbl1After):
    
    renameTblSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/renameTable.sql'

    with open(renameTblSQL, 'r') as fileProcess:
        sql = fileProcess.read()

    query = Template(sql).substitute(
        table_name = tblName,
        table1After = tbl1After
    )

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print(f"Table " + tblName + " successfully renamed to " + tbl1After)

    except sqlite3.OperationalError as e:
        print("Oh no! Error: ", e)

# rename column
def renameCol(tblName,col1Before,col1After):

    renameColSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/renameColumn.sql'

    with open(renameColSQL, 'r') as fileProcess:
        sql = fileProcess.read()

    query = Template(sql).substitute(
        table_name = tblName,
        column1Before = col1Before,
        column1After = col1After
    )

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print(f"Column " + col1Before + " successfully renamed to " + col1After)

    except sqlite3.OperationalError as e:
        print("Oh no! Error:", e)

# add new column
def addColumn(tblName,colName,colType):

    addColumnSQL = '/Users/guido/Documents/code/DatabaseGUI/SQL/addColumn.sql'
    
    with open(addColumnSQL, 'r') as fileProcess:
        sql = fileProcess.read()

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

            print(f"New column " + colName + " successfully created on table " + tblName)
        
    except sqlite3.OperationalError as e:
        print("Oh no! Error: ", e)

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

import tkinter as tk
from string import Template
# from tkinter import ttk, messagebox
# import json

# TODO
# create GUI


# Function to make the API call
def createSQL():
    tblName = tblName_entry.get()
    colName = colName_entry.get()
    colType = colType_entry.get()

    createTableSQL = '/Users/guido/Documents/code/Database-GUI/SQL/createTable.sql'

    with open(createTableSQL, 'r') as fileProcess:
        sql = fileProcess.read()
    
    query = Template(sql).substitute(
        table_name = tblName,
        col1 = colName,
        col1Type = colType
    )

    print("createTable reached")
    print(tblName)
    print(colName)
    print(colType)

# Set up the Tkinter window
root = tk.Tk()
root.title("DUI - Create Table")

# Table name entry
tk.Label(root, text="Enter table name:").grid(row=0, column=0, padx=10, pady=5)
tblName_entry = tk.Entry(root, width=40)
tblName_entry.grid(row=0, column=1, padx=10, pady=5)

# Column name entry
tk.Label(root, text="Enter column name:").grid(row=1, column=0, padx=10, pady=5)
colName_entry = tk.Entry(root, width=40)
colName_entry.grid(row=1, column=1, padx=10, pady=5)

# Column type entry
tk.Label(root, text="Enter column type:").grid(row=2, column=0, padx=10, pady=5)
colType_entry = tk.Entry(root, width=40)
colType_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=createSQL)
submit_button.grid(row=3, columnspan=2, pady=10)


root.mainloop()

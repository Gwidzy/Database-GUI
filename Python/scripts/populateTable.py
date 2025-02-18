import tkinter as tk
import sys
import os
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from DBconnect import populateTable
# from tkinter import ttk, messagebox
# import json

# TODO
# create GUI


# Function to make the API call
def populateSQL():

    populateTable()
    # tblName = tblName_entry.get()
    # colName = colName_entry.get()
    # colValues = colValues_entry.get()

    # popTableSQL = '/Users/guido/Documents/code/Database-GUI/SQL/populateTable.sql'

    # with open(popTableSQL, 'r') as fileProcess:
    #     sql = fileProcess.read()
    
    # query = Template(sql).substitute(
    #     table_name = tblName,
    #     col1 = colName,
    #     value1 = colValues
    # )

    print("popTable reached")
    # print(tblName)
    # print(colName)
    # print(colValues)

# Set up the Tkinter window
root = tk.Tk()
root.title("DUI - Populate Table")

# Table name entry
tk.Label(root, text="Enter table name:").grid(row=0, column=0, padx=10, pady=5)
tblName_entry = tk.Entry(root, width=40)
tblName_entry.grid(row=0, column=1, padx=10, pady=5)

# Column name entry
tk.Label(root, text="Enter column name:").grid(row=1, column=0, padx=10, pady=5)
colName_entry = tk.Entry(root, width=40)
colName_entry.grid(row=1, column=1, padx=10, pady=5)

# Column value entry
tk.Label(root, text="Enter column values:").grid(row=2, column=0, padx=10, pady=5)
colValues_entry = tk.Entry(root, width=40)
colValues_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=populateSQL)
submit_button.grid(row=3, columnspan=2, pady=10)


root.mainloop()

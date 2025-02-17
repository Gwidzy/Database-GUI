import tkinter as tk
# from tkinter import ttk, messagebox
# import json

# TODO
# create GUI


# Function to make the API call
def createSQL():
    tblName = tblName_entry.get()
    colName = colName_entry.get()

    createTable = "Database-GUI/SQL/createTable.sql"

    createTable.table_name = tblName
    createTable.col1 = colName
    
    print("createTable reached")
    print(tblName)
    print(colName)

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

# Submit Button
submit_button = tk.Button(root, text="Submit", command=createSQL)
submit_button.grid(row=2, columnspan=2, pady=10)


root.mainloop()
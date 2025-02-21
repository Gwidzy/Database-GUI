import tkinter as tk
import DBconnect

# Function to make the API call
def populateSQL():

    tblName = tblName_entry.get()
    colName = colName_entry.get()
    colValues = colValues_entry.get()

    print("popTable reached")
    print("Table Name:", tblName)
    print("Column Name:", colName)
    print("Column value:", colValues)
    print("---------------------")

    outputSQL.config(text="REPLACE INTO " + tblName  + " (" + colName + ") VALUES " + "(" + colValues + ");")

    DBconnect.populateTable(tblName, colName, colValues)

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

# Display output
tk.Label(root, text="Output:").grid(row=5, column=0, padx=10, pady=5)
outputSQL = tk.Label(root, text="")
outputSQL.grid(row=6, column=0,columnspan=3,padx=10, pady=5)

root.mainloop()

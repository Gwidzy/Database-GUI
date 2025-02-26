import tkinter as tk
import DBconnect

# function to gather input and call DBconnect.addColumn
def addColumn():
    tblName = tblName_entry.get()
    colName = colName_entry.get()
    colType = colType_entry.get()
    
    print("addColumn reached")
    print("Table Name:", tblName)
    print("Column Name:", colName)
    print("Column Type:", colType)
    print("---------------------")

    outputSQL.config(text="ALTER TABLE " + tblName + "  ADD" + colName + " " + colType + ";")

    # call the function from DBconnect with params
    DBconnect.addColumn(tblName, colName, colType)

# set up the Tkinter window
root = tk.Tk()
root.title("DUI - Add Column")

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
submit_button = tk.Button(root, text="Submit", command=addColumn)
submit_button.grid(row=3, columnspan=2, pady=10)

# Display output
tk.Label(root, text="Output:").grid(row=5, column=0, padx=10, pady=5)
outputSQL = tk.Label(root, text="")
outputSQL.grid(row=6, column=0,columnspan=3,padx=10, pady=5)

root.mainloop()

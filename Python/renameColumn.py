import tkinter as tk
import DBconnect

# Function to make the API call
def renameCol():

    tblName = tblName_entry.get()
    col1Before = col1Before_entry.get()
    col1After = col1After_entry.get()

    print("renameCal reached")
    print("Table Name:", tblName)
    print("Column before:", col1Before)
    print("Column after:", col1After)
    print("---------------------")

    outputSQL.config(text="ALTER TABLE " + tblName + " RENAME COLUMN " + col1Before + " to " + col1After) 

    DBconnect.renameCol(tblName, col1Before, col1After)

root = tk.Tk()
root.title("DUI - Get Table Values")

# Table name entry
tk.Label(root, text="Enter table name:").grid(row=0, column=0, padx=10, pady=5)
tblName_entry = tk.Entry(root, width=40)
tblName_entry.grid(row=0, column=1, padx=10, pady=5)

# Column before entry
tk.Label(root, text="Enter old column name:").grid(row=1, column=0, padx=10, pady=5)
col1Before_entry = tk.Entry(root, width=40)
col1Before_entry.grid(row=1, column=1, padx=10, pady=5)

# Column after entry
tk.Label(root, text="Enter new column name:").grid(row=2, column=0, padx=10, pady=5)
col1After_entry = tk.Entry(root, width=40)
col1After_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=renameCol)
submit_button.grid(row=3, columnspan=2, pady=10)

# Display output
tk.Label(root, text="Output:").grid(row=5, column=0, padx=10, pady=5)
outputSQL = tk.Label(root, text="")
outputSQL.grid(row=6, column=0,columnspan=3,padx=10, pady=5)

root.mainloop()

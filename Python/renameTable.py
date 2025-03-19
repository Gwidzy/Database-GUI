import tkinter as tk
import DBconnect

# function to gather input and call DBconnect.renameTable
def renameTbl():

    tblName = tblName_entry.get()
    tbl1After = tbl1After_entry.get()

    print("renameTable reached")
    print("Table Name:", tblName)
    print("Table after:", tbl1After)
    print("---------------------")

    outputSQL.config(text="ALTER TABLE " + tblName + " RENAME TO " + tbl1After) 

    # call the function from DBconnect with params
    DBconnect.renameTbl(tblName, tbl1After)

# set up the Tkinter window
root = tk.Tk()
root.title("DUI - Rename Table")

# Table name entry
tk.Label(root, text="Enter table name:").grid(row=0, column=0, padx=10, pady=5)
tblName_entry = tk.Entry(root, width=40)
tblName_entry.grid(row=0, column=1, padx=10, pady=5)

# Table after entry
tk.Label(root, text="Enter new table name:").grid(row=2, column=0, padx=10, pady=5)
tbl1After_entry = tk.Entry(root, width=40)
tbl1After_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=renameTbl)
submit_button.grid(row=3, columnspan=2, pady=10)

# Display output
tk.Label(root, text="Output:").grid(row=5, column=0, padx=10, pady=5)
outputSQL = tk.Label(root, text="")
outputSQL.grid(row=6, column=0,columnspan=3,padx=10, pady=5)

root.mainloop()

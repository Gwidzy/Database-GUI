import tkinter as tk

# Function to make the API call
def selectSQL():

    tblName = tblName_entry.get()
    
    print("selectSQL reached")
    print("Table Name:", tblName)
    print("---------------------")

    outputSQL.config(text="SELECT * FROM " + tblName) 

root = tk.Tk()
root.title("DUI - Get Table Values")

# Table name entry
tk.Label(root, text="Enter table name:").grid(row=0, column=0, padx=10, pady=5)
tblName_entry = tk.Entry(root, width=40)
tblName_entry.grid(row=0, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=selectSQL)
submit_button.grid(row=3, columnspan=2, pady=10)

# Display output
tk.Label(root, text="Output:").grid(row=5, column=0, padx=10, pady=5)
outputSQL = tk.Label(root, text="")
outputSQL.grid(row=6, column=0,columnspan=3,padx=10, pady=5)

root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("DUI - About")

messages = [
    "This was created by Gwidzy as a side project.",
    "The project has been something I've wanted to try for a while.",
    "The database is currently being run on a text file."
]

for msg in messages:
    label = tk.Label(root, text=msg, wraplength=500, justify="left", padx=10, pady=5)
    label.pack(anchor="w")

root.mainloop()

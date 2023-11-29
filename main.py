import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

import ttkbootstrap as ttks
from ttkbootstrap.constants import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime('%Y-%m-%d')

def fill_tree(tree):
    # Add some random data to the treeview
    for i in range(1, 200):
        name = f"Item {i}"
        date = generate_random_date()
        tree.insert(parent='', index=tk.END, values=(i, name, date))

window = tk.Tk()
window.geometry('1600x800')
window_height = window.winfo_screenheight()
tree_height_percentage = 0.75
tree_visible_rows = int((window_height * tree_height_percentage) / 20)  # Assuming each row has a height of 20

# Row configuration for the entire window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=40)
window.grid_columnconfigure(1, weight=60)

window_width = window.winfo_screenwidth()
tree_width_percentage = 0.4
tree_visible_columns = int((window_width * tree_width_percentage) / 100)  # Assuming each column has a width of 100

# Create frame1 (60% width, full height)
frame1 = tk.Frame(window)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.grid_rowconfigure(0, weight=15)
frame1.grid_rowconfigure(1, weight=10)
frame1.grid_rowconfigure(2, weight=75)
frame1.grid_columnconfigure(0, weight=1)

tree = ttk.Treeview(window,columns=('Category', 'Amount', 'Date'), show='headings', height=tree_visible_rows)
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.heading("Date", text="Date")
tree.column("Category", width=int(tree_visible_columns/3))
tree.column("Amount", width=int(tree_visible_columns/3))
tree.column("Date", width=int(tree_visible_columns/3))

tree.grid(row=2, column=0, sticky="nsew")
fill_tree(tree)

# label_1_0 = tk.Label(frame1, text="Frame 1, Row 0", bg="red")
# label_1_0.grid(row=0, column=0, sticky="nsew")
#
# label_1_1 = tk.Label(frame1, text="Frame 1, Row 1", bg="blue")
# label_1_1.grid(row=1, column=0, sticky="nsew")
#
# label_1_2 = tk.Label(frame1, text="Frame 1, Row 2", bg="green")
# label_1_2.grid(row=2, column=0, sticky="nsew")
# Create frame2 (40% width, full height)
frame2 = tk.Frame(window)
frame2.grid(row=0, column=1, sticky="nsew")
frame2.grid_rowconfigure(0, weight=50)
frame2.grid_rowconfigure(1, weight=50)
frame2.grid_columnconfigure(0, weight=1)

# label_2_0 = tk.Label(frame2, text="Frame 2, Row 0", bg="yellow")
# label_2_0.grid(row=0, column=0, sticky="nsew")
#
# label_2_1 = tk.Label(frame2, text="Frame 2, Row 1", bg="purple")
# label_2_1.grid(row=1, column=0, sticky="nsew")
#


window.mainloop()

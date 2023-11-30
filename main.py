import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
import os
from dotenv import load_dotenv


def generate_random_date():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime('%Y-%m-%d')


def fill_tree(tree):
    # Add some random data to the treeview
    rows = execute_query(query3)
    for row in rows:
        Amount = row[1]
        Desc = row[2]
        Date = row[3]
        tree.insert(parent='', index=tk.END, values=(Amount, Desc, Date))


def create_pie_chart(frame):
    fig = Figure(figsize=(frame.winfo_width() / 100, frame.winfo_height() / 100), dpi=100)
    pie_chart = fig.add_subplot(111)
    sizes = [25, 30, 20, 25]
    labels = ['A', 'B', 'C', 'D']
    wedges, texts, autotexts = pie_chart.pie(sizes, labels=labels, autopct='%1.1f%%')

    pie_chart.axis('equal')

    # Adding a legend
    pie_chart.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5), title='Legend')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)


# Function to create the bar series
def create_bar_series(frame):
    fig = Figure(figsize=(frame.winfo_width() / 100, frame.winfo_height() / 100), dpi=100)
    bar_series = fig.add_subplot(111)
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
    values = [20, 35, 30, 15]
    bar_series.bar(categories, values)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)


def execute_query(query):
    cursor = mydb.cursor()
    cursor.execute(query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    cursor.close()
    return rows


load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
pas = os.getenv('DB_PASSWORD')
db = os.getenv('DB_DATABASE')

mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=pas,
    database=db,
)

# Queries
query1 = "SELECT Category, SUM(Amount) FROM Expenses GROUP BY Category;"
query2 = "SELECT DATE_FORMAT(TransactionDate, '%m-%Y') AS TransactionMonth, SUM(Amount) AS TotalAmount FROM Expenses GROUP BY DATE_FORMAT(TransactionDate, '%m-%Y') ORDER BY TransactionMonth;"
query3 = "SELECT * FROM Expenses;"
# Execute queries
execute_query(query1)
execute_query(query2)

window = tk.Tk()
window.geometry('1600x800')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=40)
window.grid_columnconfigure(1, weight=60)

frame1 = tk.Frame(window)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.grid_rowconfigure(0, weight=15)
frame1.grid_rowconfigure(1, weight=10)
frame1.grid_rowconfigure(2, weight=75)
frame1.grid_columnconfigure(0, weight=1)

tree = ttk.Treeview(frame1, columns=('Category', 'Amount', 'Date'), show='headings')
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.heading("Date", text="Date")
tree.column("Category", width=100)
tree.column("Amount", width=100)
tree.column("Date", width=100)

tree.grid(row=2, column=0, sticky="nsew")
fill_tree(tree)

frame2 = tk.Frame(window)
frame2.grid(row=0, column=1, sticky="nsew")

frame2.grid_rowconfigure(0, weight=50)
frame2.grid_rowconfigure(1, weight=50)
frame2.grid_columnconfigure(0, weight=1)

sub_frame_1 = tk.Frame(frame2)
sub_frame_1.grid(row=0, column=0, sticky="nsew")

sub_frame_2 = tk.Frame(frame2)
sub_frame_2.grid(row=1, column=0, sticky="nsew")

create_pie_chart(sub_frame_1)
create_bar_series(sub_frame_2)

window.mainloop()

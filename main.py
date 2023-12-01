import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
import os
from dotenv import load_dotenv


def fill_tree(tree):
    # Add some random data to the treeview
    rows = execute_query(query3)
    for row in rows:
        Amount = row[1]
        Desc = row[2]
        Date = row[3]
        tree.insert(parent='', index=tk.END, values=(Amount, Desc, Date))


def create_pie_chart(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    query1 = "SELECT Category, SUM(Amount) FROM Expenses GROUP BY Category;"
    data = execute_query(query1)
    sumOfAmount = []
    categories = []
    for tup in data:
        value1, value2 = tup  # Unpack the tuple into two values
        categories.append(value1)  # Append the first value to array1
        sumOfAmount.append(value2)  # Append the second value to array2

    fig = Figure(figsize=(frame.winfo_width() / 100, frame.winfo_height() / 100), dpi=100)
    pie_chart = fig.add_subplot(111)

    wedges, texts, autotexts = pie_chart.pie(sumOfAmount, labels=categories, autopct='%1.1f%%')

    pie_chart.axis('equal')

    # Adding a legend
    pie_chart.legend(wedges, categories, loc='center left', bbox_to_anchor=(1, 0.5), title='Legend')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)


# Function to create the bar series
def create_bar_series(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    query2 = "SELECT DATE_FORMAT(TransactionDate, '%m-%Y') AS TransactionMonth, SUM(Amount) AS TotalAmount FROM Expenses GROUP BY DATE_FORMAT(TransactionDate, '%m-%Y') ORDER BY TransactionMonth;"
    data = execute_query(query2)
    amount = []
    categories = []
    for tup in data:
        value1, value2 = tup  # Unpack the tuple into two values
        categories.append(value1)  # Append the first value to array1
        amount.append(value2)  # Append the second value to array2
    fig = Figure(figsize=(frame.winfo_width() / 100, frame.winfo_height() / 100), dpi=100)
    bar_series = fig.add_subplot(111)
    bar_series.bar(categories, amount)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)


def execute_query(query):
    cursor = mydb.cursor()
    cursor.execute(query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    cursor.close()
    return rows


def button_clicked():
    create_pie_chart(sub_frame_1)
    create_bar_series(sub_frame_2)



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

query3 = "SELECT * FROM Expenses;"
# Execute queries

window = tk.Tk()
window.geometry('1600x800')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=30)
window.grid_columnconfigure(1, weight=70)

frame1 = tk.Frame(window)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.grid_rowconfigure(0, weight=15)
frame1.grid_rowconfigure(1, weight=10)
frame1.grid_rowconfigure(2, weight=75)
frame1.grid_columnconfigure(0, weight=1)

label = tk.Label(frame1, text="Expense Tracker App", font=("Helveticca", 28), foreground="blue")
label.grid(row=0, column=0)

button = tk.Button(frame1, text="Add Expense", command=button_clicked, width=10)
button.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

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

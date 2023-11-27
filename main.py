import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.geometry('1600x800')


# Row configuration for the entire window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
# Create frame1 (60% width, full height)
frame1 = tk.Frame(window)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.grid_rowconfigure(0, weight=15)
frame1.grid_rowconfigure(1, weight=10)
frame1.grid_rowconfigure(2, weight=75)
frame1.grid_columnconfigure(0, weight=60)

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
frame2.grid_rowconfigure(0, weight=33)
frame2.grid_rowconfigure(1, weight=33)
frame2.grid_rowconfigure(2, weight=33)
frame2.grid_columnconfigure(0, weight=40)

# label_2_0 = tk.Label(frame2, text="Frame 2, Row 0", bg="yellow")
# label_2_0.grid(row=0, column=0, sticky="nsew")
#
# label_2_1 = tk.Label(frame2, text="Frame 2, Row 1", bg="purple")
# label_2_1.grid(row=1, column=0, sticky="nsew")
#
# label_2_2 = tk.Label(frame2, text="Frame 2, Row 2", bg="orange")
# label_2_2.grid(row=2, column=0, sticky="nsew")


window.mainloop()

import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from PIL import Image, ImageTk  # Need to pip install Pillow

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.resizable(False, False)
root.title("Converter")
root.geometry('300x200')

root.iconbitmap(r'calc.ico')

#font.nametofont("TkDefaultFont").configure(size=10)

style = ttk.Style(root)
#print(style.theme_names())
style.theme_use("clam")

feet_value = tk.StringVar()
metres_value = tk.StringVar()


def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


main = ttk.Frame(root, padding=(15, 15))
main.grid()

root.columnconfigure(0, weight=1)

# -- Widgets --

metres_label = ttk.Label(main, text="Metres: ",font=("Courier", 10))
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Courier", 10))  # None means "don't change the font".
feet_label = ttk.Label(main, text="Feet: ",font=("Courier", 10))
feet_display = ttk.Label(main, textvariable=feet_value, font=("Courier", 10))

calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

# -- Layout --

metres_label.grid(column=0, row=0, sticky="W")
metres_input.grid(column=1, row=0, sticky="EW")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")

# winfo_children stands for "widget info children", and gets all the children of a widget.
for child in main.winfo_children():
    child.grid_configure(padx=10, pady=10)


root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
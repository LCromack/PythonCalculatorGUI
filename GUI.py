from tkinter import *
from tkinter import ttk
from Calculator import *

def calculate(*args):
    try:
        Num1 = float(num1.get())
        Num2 = float(num2.get())
        Operator = str(opp.get())
        # result.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        result.set(calculation(Num1, Num2, Operator))
    except ValueError:
        pass

root = Tk()
root.title("Calculator")
root.geometry("400x300")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

num1 = StringVar()
num1_entry = ttk.Entry(mainframe, width=14, textvariable=num1)
num1_entry.grid(column=2, row=1, sticky=(W, E))

num2 = StringVar()
num2_entry = ttk.Entry(mainframe, width=14, textvariable=num2)
num2_entry.grid(column=2, row=2, sticky=(W, E))

opp = StringVar()
opp_entry = ttk.Entry(mainframe, width=14, textvariable=opp)
opp_entry.grid(column=2, row=3, sticky=(W, E))

result = StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="=", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="Num 1").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Num 2").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Operator").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Result").grid(column=1, row=4, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

num1_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
'''
Frederick Herzog
A GUI for looking up hex color codes
'''
import csv
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

HEIGHT = 300
WIDTH = 400
COLOR = '#5d8aa8'

def getCode(variable):
	output.delete(0.0, tk.END)
	output.insert(tk.END, data[variable])
	l = tk.Label(frame, text="Preview:", bg=COLOR)
	l.place(relx=.3, rely=.7, relwidth=.4, relheight=.1)
	prev = tk.Label(frame, bg=data[variable])
	prev.place(relx=.3, rely=.8, relwidth=.4, relheight=.1)

def makeDict(file):
	data = {}
	with open(file, newline='') as f:
		reader = csv.reader(f)
		next(reader)
		data = dict(reader)
		return data

data = makeDict('colors.csv')
colors = list(data.keys())

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(window, bg=COLOR)
frame.place(relwidth=1, relheight=1)

variable = tk.StringVar(window)
variable.set(colors[0]) # default value

w = tk.OptionMenu(frame, variable, *colors)
w.place(relx=.3, rely=.54, relwidth=.4, relheight=.1)

enter_btn = tk.Button(frame, text='Find Color', bg='orange', command=lambda: getCode(variable.get()))
enter_btn.place(relx=.3, rely=.4, relwidth=.2, relheight=.1)

output = tk.Text(frame, width=14, height=6, font=14, background="white", padx=3)
output.place(relx=.5, rely=.4, relwidth=.2, relheight=.1)

window.mainloop()

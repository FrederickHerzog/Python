'''
Frederick Herzog
A simple tkinter glossary for the 50 states
'''
import csv 
import webbrowser
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def clear():
	output.delete(0.0, tk.END)
	output2.delete(0.0, tk.END)

def wiki(entry):
	webbrowser.open('https://en.wikipedia.org/wiki/'+entry)

def getInfo(entry):
	tab = '\t\t    '
	clear()
	output.insert(tk.END, "Capitol:" +tab+state_cap[entry])
	output.insert(tk.END, "\nPopulation:" +tab+state_pops[entry])
	output.insert(tk.END, "\nCoordinates:"+tab+coor[entry])
	output.insert(tk.END, "\nFounded:"+tab+founded[entry])

	output2.insert(tk.END, "Flower:" +tab+st_flowers[entry])
	output2.insert(tk.END, "\nBird:" +tab+birds[entry])
def makeDict(file):
	data = {}
	with open(file, newline='') as f:
		reader = csv.reader(f)
		next(reader)
		data = dict(reader)
		return data

HEIGHT = 600
WIDTH = 700
state_cap = makeDict('capitals.csv')
states = list(state_cap.keys())
state_pops = makeDict('populations.csv')
st_flowers = makeDict('flowers.csv')
coor = makeDict('coordinates.csv')
birds = makeDict('birds.csv')
founded = makeDict("founded.csv")

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

background_img = tk.PhotoImage(file='states.png')
back_label = tk.Label(window, image = background_img)
back_label.place(relwidth=1, relheight=1)

frame1 = tk.Frame(window, bg='gray')
frame1.place(relwidth=1, relheight=.17)

frame2 = tk.Frame(window)
frame2.place(relx=0, rely=.75, relwidth=.5, relheight=.28)

frame3 = tk.Frame(window, bg='gray')
frame3.place(relx=.5, rely=.75, relwidth=.5, relheight=.25)

variable = tk.StringVar(window)
variable.set(states[0]) # default value
w = tk.OptionMenu(frame1, variable, *states)
w.place(relx=.3, rely=0, relwidth=.4, relheight=.27)

enter_btn = tk.Button(frame1, text='Get Info', bg='orange', bd=3,
							font=16, command=lambda: getInfo(variable.get()))
enter_btn.place(relx=.4, rely=.4, relwidth=.2, relheight=.4)

wiki_btn = tk.Button(frame1, text='See Wiki', bd=3, command= lambda: wiki(variable.get()))
wiki_btn.place(relx=.4, rely=.8, relwidth=.2, relheight=.2)

clear_btn = tk.Button(frame1, text='Clear', bg='#ff3333', bd=3, font=12, command= clear)
clear_btn.place(relx=.9, rely=0, relwidth=.1, relheight=1)

output = tk.Text(frame2, width=14, height=6, font=12, background="#ffe6cc", padx=3)
output.place(relwidth=1, relheight=1)

output2 = tk.Text(frame3, width=14, height=6, font=12, background="#ffe6cc", padx=3)
output2.place(relwidth=1, relheight=1)

window.mainloop()

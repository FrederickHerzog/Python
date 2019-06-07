'''
Frederick Herzog
A basic GUI that finds the day of the week from 
a user defined date.
'''

import tkinter as tk 
import datetime

HEIGHT = 220
WIDTH = 320
COLOR = '#0B4C5F'

def show():
	output.delete(0.0, tk.END)
	try:
		y = int(e1.get())
		m = int(e2.get())
		d = int(e3.get())
		mydate = datetime.date(y,m,d)
		day = mydate.strftime("%A")
		output.insert(tk.END, day)
	except:
		output.insert(tk.END, 'ERROR')

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame1 = tk.Frame(window, bg=COLOR)
frame1.place(relwidth=1, relheight=1)

#Labels
l1 = tk.Label(frame1, text="Year", fg='gray', font='12', bg=COLOR)
l1.place(relx=0, rely=0, relwidth=.13, relheight=.11)
l2 = tk.Label(frame1, text="Month", fg='gray', font='12', bg=COLOR)
l2.place(relx=0, rely=.1, relwidth=.13, relheight=.11)
l3 = tk.Label(frame1, text="Day", fg='gray', font='12', bg=COLOR)
l3.place(relx=0, rely=.2, relwidth=.13, relheight=.11)

l4 = tk.Label(frame1, text='Day of Week', font='12', fg = 'gray', bg=COLOR)
l4.place(relx=.2, rely=.5, relwidth=.35, relheight=.1)

#Input text boxes
e1 = tk.Entry(frame1, font='12')
e1.place(relx=.2, rely=0, relwidth=.35, relheight=.11)
e2 = tk.Entry(frame1, font='12')
e2.place(relx=.2, rely=.1, relwidth=.35, relheight=.11)
e3 = tk.Entry(frame1, font='12')
e3.place(relx=.2, rely=.2, relwidth=.35, relheight=.11)

#Output text box
output = tk.Text(frame1, width=9, height=2, font='13', background="white")
output.place(relx=.2, rely=.6, relwidth=.35, relheight=.11)

#Buttons
b1 = tk.Button(frame1, text='Quit', height=2, bd=3, bg='red', command=window.quit)
b1.place(relx=.75, rely=.5, relwidth=.25, relheight=.15)
b2 = tk.Button(frame1, text='Calculate', fg="yellow", bg='gray',
						bd=3, height=2, width=6, cursor="dot", command=show)
b2.place(relx=.75, rely=.3, relwidth=.25, relheight=.2)


window.mainloop( )

#Frederick Herzog
import datetime 
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

HEIGHT = 300
WIDTH = 400

def datee():
    print(datetime.datetime.now())

def hello():
	print("Hello")

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(window, bg='#81F79F')
frame.place(relwidth=1, relheight=1)


btn1 = tk.Button(frame, text="Say Hi", bg='gray', fg='#FA5882', command=hello)
btn1.place(relx=.375, rely=.35, relwidth=.25, relheight=.15)
btn2 = tk.Button(frame, text="Date And Time", command=datee)
btn2.place(relx=.35, rely=.5, relwidth=.30, relheight=.15)

window.mainloop()

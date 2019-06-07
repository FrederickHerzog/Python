#Frederick Herzog

import tkinter as tk 

HEIGHT = 300
WIDTH = 400

def hello():
    print("Hello")

window = tk.Tk()

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(window, bg='gray')
frame.place(relwidth=1, relheight=1)

btn1 = tk.Button(frame, text="Say Hi", command=hello)
btn1.place(relx=.35, rely=.35, relwidth=.3, relheight=.3)

window.mainloop()

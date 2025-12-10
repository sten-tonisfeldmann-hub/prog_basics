from tkinter import *
raam = Tk()
raam.title("Lipp")
tahvel = Canvas(raam, width=1000, height=1000, background="white")

tahvel.create_oval(0, 0, 1000, 1000, fill="red", outline="red")
tahvel.create_oval(70, 70, 930, 930, fill="white", outline="white")

tahvel.pack()
raam.mainloop()
from tkinter import *
raam = Tk()
raam.title("Lipp")
tahvel = Canvas(raam, width=1000, height=600, background="white")

tahvel.create_rectangle(0, 150, 1000, 300, fill="red", outline="red")
tahvel.create_rectangle(0, 450, 1000, 600, fill="red", outline="red")

tahvel.pack()
raam.mainloop()
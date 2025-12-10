from tkinter import *
raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=1600, height=1000, background="white")

tahvel.create_rectangle(0, 0, 1600, 1000, fill="cyan", outline="cyan")
tahvel.create_rectangle(0, 600, 1600, 1000, fill="green", outline="green")
tahvel.create_rectangle(400, 300, 1200, 700, fill="white", outline="white")
tahvel.create_rectangle(390, 350, 1210, 300, fill="gray", outline="gray")
tahvel.create_rectangle(410, 330, 470, 150, fill="red", outline="red")
tahvel.create_rectangle(460, 500, 560, 700, fill="black", outline="black")
tahvel.create_rectangle(660, 460, 1150, 650, fill="black", outline="black")

tahvel.pack()
raam.mainloop()
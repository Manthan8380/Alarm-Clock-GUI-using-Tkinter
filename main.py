import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time, pygame

# ================================================================================
def mainLabels():
    # Entry Box 1
    global entryB1
    entryB1 = Entry(root, width=25)
    entryB1.place(x=250, y=180)

    # Entry Box 2
    global entryB2
    entryB2 = Entry(root, width=25)
    entryB2.place(x=250, y=250)

# Message Box Logic
def message1():
    global entryB1
    AlrmTimelabel = entryB1.get()
    messagebox.showinfo("Alarm Clock", f"Alarm is set to: {AlrmTimelabel}")

# Submit Button Logic
def submit():
    global entryB1, entryB2
    submit_text.set("Alarm is counting...")
    Alarmtime = entryB1.get()
    message1()
    currentTime = time.strftime("%H:%M")
    AlarmMsg = entryB2.get()

    while Alarmtime != currentTime:
        currentTime = time.strftime("%H:%M")
        time.sleep(1)

    if Alarmtime == currentTime:
        submit_text.set("Playing alarm sound..")
        pygame.mixer.music.load("audio/wakeup-alarm-tone-21497.mp3")
        pygame.mixer.music.play()
        messagebox.showinfo("Alarm Message", f"Message: {AlarmMsg}")
# ================================================================================

root = Tk()

# Window Title & Icon
root.title("Alarm Clock")
root.iconbitmap("icon/Boshton.ico")
wallpaper =  Image.open("image/opticalno.jpg")

# Canvas Size
Aclock_canvas = tk.Canvas(root, width=600, height=350)
Aclock_canvas.pack(fill="both", expand=True)
Aclock_canvas.grid(columnspan=3, rowspan=5)

# To Resize the Image
resized_image = wallpaper.resize((600,350), Image.ANTIALIAS)
new_wall = ImageTk.PhotoImage(resized_image)
Aclock_canvas.create_image(0,0, image=new_wall, anchor="nw")
Aclock_canvas.create_text(300,50, text="...A Rooster...", fill='black', font=('Gabriola', 30, 'bold'))
Aclock_canvas.create_text(140,188, text="Time in HH:MM         :", fill='black', font=('Raleway', 12, 'bold'))
Aclock_canvas.create_text(140,260, text="Enter the Message  :", fill='black', font=('Raleway', 12, 'bold'))

# Submit Button
submit_text = tk.StringVar()
submit_btn = tk.Button(root, textvariable=submit_text, font=('Comic Sans MS', 10, 'bold'), bg='#45B39D', fg='black', width=16, command=submit).place(x=450, y=245)
submit_text.set("Set Alarm")

mainLabels()
pygame.mixer.init()

root.mainloop()
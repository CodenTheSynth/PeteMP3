from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from modules.AnimatedGif import *
import atexit
from pygame import mixer
from tkinter import simpledialog
import os

mixer.init()

spd = 0.04
paused = False

def hehehe():
    laugh = mixer.Sound("Audio\hehe.mp3")
    laugh.play()

def setvol():
    vol = simpledialog.askinteger(prompt="Set Song Volume", title="PeteMP3 Tools")
    mixer.music.pause()
    mixer.music.set_volume(vol*0.01)
    mixer.music.unpause()

def setspeed():
    global spd
    global retep
    spd = simpledialog.askfloat(prompt="Set Dance Speed", title="PeteMP3 Tools")
    retep.destroy()
    retep = AnimatedGif(window,"images/peter.gif",spd)
    retep.place(x=28,y=10)
    retep.config(bg="white")
    retep.start()


def AnimatePete():
    mixer.music.stop()
    audio = filedialog.askopenfilename(defaultextension='.mp3', filetypes=[("MP3 Files", '*.mp3')])
    try:
      mixer.music.load(audio)
      mixer.music.play(-1)
      paus.configure(state=NORMAL)
      paus.update()
      songinfo.config(text="Now Playing: {}".format(os.path.basename(audio)))
    except:
        messagebox.showerror("Error", "Unable to play the audio file.")
        return
    retep.place(x=28,y=10)

def Credits():
    messagebox.showinfo(title="Credits", message="PeteMP3 was created by Coden.\nThanks to olesk75 for the AnimatedGif module.\nPeter Griffin & Family Guy is owned by Seth MacFarlane")
def Info():
    messagebox.showinfo(title="Info", message="PeteMP3 is a very basic mp3 player i made using tkinter and pygame, its pretty much bad on purpose. i basically made it to test out my tkinter'ing skills. \ni plan on improving and adding stuff to this little project, i hope you enjoy this. also, feel free to contribute :D")
def togglepause():
    global paused
    if(paused):
        paused = False
        mixer.music.unpause()
        retep.place(x=28,y=10)
        paus.config(text="   Pause   ")
    else:
        paused = True
        mixer.music.pause()
        retep.place(x=9999,y=9999)
        paus.config(text="Unpause")
    paus.update()


window = Tk()
window.config(bg="white")
window.geometry("250x310")
window.resizable(False,False)
window.title("PeteMP3")
icon = PhotoImage(file="images\icon.png")
window.iconphoto(True, icon)
menubar = Menu(window)
window.config(menu=menubar)

Config_Menu = Menu(menubar)
Info_Menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Config", menu=Config_Menu,font=("Comic Sans MS",8))
Config_Menu.add_command(label="Dance Speed", command=setspeed,font=("Comic Sans MS",8))
Config_Menu.add_command(label="Set Volume", command = setvol,font=("Comic Sans MS",8))
Config_Menu.add_separator()
Config_Menu.add_command(label="heheheheh", command=hehehe,font=("Comic Sans MS",8))

menubar.add_cascade(label="Info", menu=Info_Menu,font=("Comic Sans MS",8))
Info_Menu.add_command(label="Credits", command=Credits,font=("Comic Sans MS",8))
Info_Menu.add_command(label="Info", command=Info,font=("Comic Sans MS",8))

peteIdle = PhotoImage(file="images/peter.gif")


# do not touch the 1st, paremeter, you can edit the other two freely.
peter = Label(window,image=peteIdle, bg = "white")
peter.pack(padx=10, pady=10)

retep = AnimatedGif(window,"images/peter.gif",spd)
retep.place(x=99999,y=99999)
retep.config(bg="white")
retep.start()


frame = Frame(window,bg="black")
frame.pack(fill='both')
songinfo = Label(frame, bg = "black",fg="white", font=("Comic Sans MS",8), text="No Songs Playing Right Now :/")
songinfo.pack(side=BOTTOM)
select = Button(frame, text="Select Mp3", pady=1, padx= 30, command=AnimatePete, font=("Comic Sans MS",8), bg="dark grey")
select.pack(side=LEFT,pady=10)

paus = Button(frame, text="   Pause   ", pady=1, padx= 30, command=togglepause, state=DISABLED,font=("Comic Sans MS",8),bg="dark grey")
paus.pack(side=RIGHT, pady=10)


window.mainloop()
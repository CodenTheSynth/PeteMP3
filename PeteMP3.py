from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from modules.AnimatedGif import *
import atexit
import wave

from pygame import mixer

mixer.init()

paused = False

def AnimatePete():
    mixer.music.stop()
    audio = filedialog.askopenfilename(defaultextension='.mp3', filetypes=[("MP3 Files", '*.mp3')])
    try:
      mixer.music.load(audio)
      mixer.music.play()
      paus.configure(state=NORMAL)
      paus.update()
    except:
        messagebox.showerror("Error", "Unable to play the audio file.")
        return
    retep.place(x=15,y=10)

def togglepause():
    global paused
    if(paused):
        paused = False
        mixer.music.unpause()
        retep.place(x=15,y=10)
        paus.config(text="Pause")
    else:
        paused = True
        mixer.music.pause()
        retep.place(x=9999,y=9999)
        paus.config(text="Unpause")
    paus.update()


window = Tk()
window.geometry("250x300")
window.resizable(False,False)
window.title("PeteMP3")
icon = PhotoImage(file="images\icon.png")
window.iconphoto(True, icon)

peteIdle = PhotoImage(file="images/peter.gif")

# do not touch the 1st, paremeter, you can edit the other two freely.
peter = Label(window,image=peteIdle)
peter.pack(padx=10, pady=10)

retep = AnimatedGif(window,"images/peter.gif", 0.06)
retep.place(x=99999,y=99999)
retep.start()

select = Button(window, text="Select Mp3", pady=1, padx= 25, command=AnimatePete)
select.pack(side=LEFT, pady=10)

paus = Button(window, text="Pause", pady=1, padx= 30, command=togglepause, state=DISABLED)
paus.pack(side=RIGHT, pady=10)

window.mainloop()
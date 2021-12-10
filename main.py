from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog
import os

root = Tk()

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar) #config makes sure that the menu bar sticks to the top and is ready to contain sub menus

# Create the submenu
subMenu = Menu(menubar, tearoff=0)

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

menubar.add_cascade(label="My Music", menu=subMenu)
subMenu.add_command(label="Add song", command=browse_file)
subMenu.add_command(label="Add multiple songs")

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo("Arushi's music player", "This music player is built using Python")

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

mixer.init()

root.geometry('500x400')
root.title("Arushi's Music Player")
root.iconbitmap(r'icon.ico')

def play_music():
    try:
        paused

    except NameError:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = "Playing music" + ' - ' + os.path.basename(filename)
        except:
            tkinter.messagebox.showerror('File not found', 'Music Player could not find any file. Please check again.')

    else:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"

def vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

#Playlist box
song_list = Listbox(root, bg="black", fg="red", width=60)
song_list.pack(pady=20)

#Player control button images
back_img = PhotoImage(file=r'previous.png')
next_img =PhotoImage(file=r'next.png')
play_img =PhotoImage(file=r'play.png')
pause_img = PhotoImage(file=r'pause.png')
stop_img = PhotoImage(file=r'stop.png')

#Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_img, borderwidth=0)
forward_button = Button(controls_frame, image=next_img, borderwidth=0)
play_button = Button(controls_frame, image=play_img, borderwidth=0, command=play_music)
pause_button = Button(controls_frame, image=pause_img, borderwidth=0, command=pause_music)
stop_button = Button(controls_frame, image=stop_img, borderwidth=0, command=stop_music)

back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=vol, )
scale.set(70) #sets the default value to 70
mixer.music.set_volume(70)
scale.pack()

statusbar = Label(root, text="Welcome to Arushi's Music Player", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)



root.mainloop()
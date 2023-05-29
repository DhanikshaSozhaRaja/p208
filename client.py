import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    print("\n\t\t\t\tMusic Sharing")

    #Client GUI starts here
    window=Tk()

    window.title('Music Sharing')
    window.geometry("500x350")
    window.configure(bg="LightSkyBlue")

    label = Label(window, text="Select Song", bg = "LightSkyBlue", font=("Calibri", 8))
    label.place(x=2, y=1)

    listBox = Listbox(window, height=10, width=39, font=("Calibri", 10), activestyle='dotbox', borderwidth=2, bg = "LightSkyBlue")
    listBox.place(x=10, y=18)

    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command=listBox.yview)

    play = Button(window, text="Play", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    play.place(x=30, y=200)

    stopButton = Button(window, text="Stop", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    stopButton.place(x=200, y=200)

    upload = Button(window, text="Upload", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    upload.place(x=30, y=250)

    download = Button(window, text="Download", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    download.place(x=200, y=250)

    infoLabel = Label(window, text = "", bg = "Blue", font=("Calibri", 10))
    infoLabel.place(x=4, y=280)


    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    musicWindow()

setup()

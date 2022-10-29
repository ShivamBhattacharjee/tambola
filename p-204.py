
import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None



#Teacher write code here for askPlayerName()
def askPlayerName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    nameWindow=Tk()
    nameWindow.title("Tambola game")
    nameWindow.attributes('-fullscreen',True)

    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()

    bg=ImageTk.PhotoImage(file="assets/background1.png")

    canvas1=Canvas(nameWindow,width=screen_width,height=500)
    canvas1.pack(fill="both",expand=True)
    
    canvas1.create_image(0,0,image=bg,anchor="nw")
    canvas1.create_text(screen_width/2,screen_height/5,text="Tambola game",font=("Chalkboard SE",100),fill="white")

    nameEntry=Entry(nameWindow,width=10,justify="center",font=("Chalkboard SE",100),bg="white")
    nameEntry.place(x=screen_width/2-370,y=screen_height/4+100)

    button=Button(nameWindow,text="save",font=("Chalkboard SE",40),bg="grey",bd=3,width=5,command=saveName)
    button.place(x=screen_width/2-120,y=screen_height/2+100)

    nameWindow.resizable(True,True)
    nameWindow.mainloop()

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName=nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode("utf-8"))

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()

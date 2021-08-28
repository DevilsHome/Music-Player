from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from pygame import mixer
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class player:
    def __init__(self,root):
        self.root=root
        root.title("Ritesh c Palyer")
        
        root.config(bg="black")

        self.track = StringVar()
    
        self.status = StringVar()


        self.bg=ImageTk.PhotoImage(file="images/bg.gif")
        bg = Label(self.root,image=self.bg).place(x=163,y=2,width=1032,height=613)

        #=============================SIDEBAR===================================


        F1=LabelFrame(self.root,bd=5,bg="black").place(x=0,y=0,width=160,height=700)

        #self.bg=ImageTk.PhotoImage(file="images/spotify.png")
        #bg = Label(F3,image=self.bg).place(x=660,y=300)

        Home=Button(F1,text="Home",bd=0,font=("Times new roman",14),cursor="hand2",bg="black",fg="white",activebackground="grey").place(x=40,y=30)
        search=Button(F1,text="Search",bd=0,font=("Times new roman",14),cursor="hand2",bg="black",fg="white",activebackground="grey").place(x=40,y=62)
        library=Button(F1,text="//Your library",bd=0,font=("Times new roman",14),cursor="hand2",bg="black",fg="white",activebackground="grey").place(x=20,y=90)

        # -------------------- Button Frame------------------------
        F2=LabelFrame(self.root,bd=10,bg="Black")
        F2.place(x=0,y=700,relwidth=1,height=120)
        #songtracker=Scale(F2,width=20,orient=HORIZONTAL).pack()
        
       
        #======================Pause button============

        self.btn_2=ImageTk.PhotoImage(file="images/pause.png")
        btn_2 = Button(F2,image=self.btn_2,command=self.pause,cursor="hand2").place(x=660,y=40,width=20,height=20)

        #======================Play button============
        self.btn_1=ImageTk.PhotoImage(file="images/play.jpg")
        btn_1 = Button(F2,image=self.btn_1,command=self.play,cursor="hand2").place(x=760,y=40,width=20,height=20)

        #======================Stop button============

        self.btn_3=ImageTk.PhotoImage(file="images/stop.png")
        btn_3 = Button(F2,image=self.btn_3,command=self.stop,cursor="hand2").place(x=860,y=40,width=20,height=20)

        Load = Button(F2, text = 'Load',  width = 10, font = ('Times', 10),cursor="hand2",command=self.load).place(x=560,y=40)
        #play = Button(F2, text = 'Play',  width = 10, font = ('Times', 10),cursor="hand2",command=self.play).place(x=660,y=40)
        #pause = Button(F2, text = 'Pause',  width = 10, font = ('Times', 10),cursor="hand2",command=self.pause).place(x=760,y=40)
        #stop = Button(F2, text = 'Stop',  width = 10, font = ('Times', 10),cursor="hand2",command=self.stop).place(x=860,y=40)

        self.c_file=self.playlist=False
        self.playing_state=False
        
        
        songsframe=Label(self.root,text="Songs", font=("times new roman",12),bd=10,relief=SUNKEN,fg="gold")
        songsframe.place(x=1200,y=0,width=350,height=700)
        #Fav = Button(self.root,text="Add to fav",font=("Times new Roman",12),fg="black",bg="white",bd=6,width=10).place(x=800,y=40)
        trackframe=LabelFrame(self.root,text="Song Status",fg="gold" , bd=10 ,bg="white")
        trackframe.place(x=160,y=620,width=1050,height=80)

        songtrack=Label(trackframe,text="Song Status",width=90,height=2,textvariable=self.track,bg="Orange",fg="black",font=("times new roman",12)).place(x=0,y=0)
        trackstatus=Label(trackframe,textvariable=self.status,font=("times new roman",12),bg="blue",fg="gold",width=24,height=2).place(x=800,y=0)
        Scrol_y=Scrollbar(songsframe,orient=VERTICAL)
        self.playlist=Listbox(songsframe,yscrollcommand=Scrol_y.set,font=("times new roman",12),selectbackground="grey",bg="black",fg="white",selectmode=SINGLE)
        Scrol_y.pack(side=RIGHT,fill=Y)
        Scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH,expand=1)
        #Changing Directory for fetching Songs
        os.chdir("D:\music")
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END,track)

    def load(self):
        self.c_file=filedialog.askopenfilename()
        self.status.set("Song loaded")
        pass

    def play(self):
        
        self.track.set(self.playlist.get(ACTIVE))
        
        self.status.set("Playing")
        mixer.init()
        mixer.music.load(self.playlist.get(ACTIVE))
        mixer.music.play()
        pass

    def pause(self):
        if self.playing_state:
            self.playing_state=False
            mixer.pause()
            self.status.set("Pause")
        else:
            self.playing_state=True
            mixer.unpause()
            self.status.set("playing")
            

    def stop(self):
        mixer.stop()
        self.status.set("stop")

         
root=Tk()
obj=player(root)
root.mainloop()

  
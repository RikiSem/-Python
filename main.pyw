import os
import sys
import time
from tkinter import *
from tkinter import font
from tkinter.messagebox import showerror, showwarning, showinfo
from pygame import mixer
from play_music import Music
import multiprocess

if __name__ == "__main__":
    countMusic = 0
    files = 0
    path = ""
    exit = False
    num = -1
    play = False
    statusText = "------"
    MusicTime = 1
    oldMusic = -1

    root = Tk()
    root.geometry("720x360")
    root.title("PyMus")
    root.resizable(False,False)
    root.configure(background="black")
    mixer.init()

    def SetPath():
        MusicList.delete(0, END)
        file = open("path.sgg","w")
        if way.get() == "":
            way.set(path)
        path = way.get()
        file.write(path)
        file.close()
        files = Music(path).showMusicInPath()
        countMusic = len(files)
        Start()

    def ShowSetWindow():
        global Entr, way, path
        setWindow = Toplevel(root)
        insetFont = font.Font(family= "Arial", size=12, weight="normal", slant="roman")
        setWindow.geometry("480x320")
        setWindow.resizable(False,False)
        way = StringVar(setWindow,value = path)
        label1 = Label(setWindow,text="Папка с музыкой: ",font=insetFont).place(x=0,y=1)
        Entr = Entry(setWindow,width=30, font=insetFont,textvariable=way).place(x=20*7,y=1)
        SaveBtn = Button(setWindow,text="Сохранить",command=SetPath, font=insetFont).place(x = 0,y = 30)

    def ExitDef():
        global exit
        exit = True
        root.destroy()
        sys.exit(0)

    def playMusic():
        global path, num, files, play, oldMusic, MusicLen
        NewMusic = int(MusicList.curselection()[0])
        if(play == True and NewMusic == oldMusic):
            play = False
            mixer.music.pause()
            Playbtn.configure(image=playImg)
        elif(play == False and NewMusic == oldMusic):
            play = True
            mixer.music.unpause()
            Playbtn.configure(image=pauseImg)
        elif(play == True and NewMusic != oldMusic):
            play = True
            Playbtn.configure(image=pauseImg)
            mixer.music.load(path + "\\" + files[int(MusicList.curselection()[0])])
            mixer.music.play()
        elif(play == False and NewMusic != oldMusic):
            play = True
            Playbtn.configure(image=pauseImg)
            mixer.music.load(path + "\\" + files[int(MusicList.curselection()[0])])
            mixer.music.play()
        oldMusic = int(MusicList.curselection()[0])   

    def Start():
        global files,countMusic, files, num, path, statusText
        try:
            file = open("path.sgg","r")
            path = file.read()
            file.close()
            files = Music(path).showMusicInPath()
            countMusic = len(files)
            i = 0
            for line in files:
                MusicList.insert(i,line)
                i += 1
            statusText = "Найдено композиций: " + str(countMusic)
            status.set(statusText) 
        except:
            ShowSetWindow()  
 



    ############################################################################# Верхний Frame
    setFont = font.Font(family= "Verdana", size=8, weight="normal", slant="roman")
    setFrame = Frame(root,background="grey",width=720,height=35,borderwidth = 3,relief="ridge")
    settingsBtn = Button(setFrame,text="Настройки",width=9, height=1,bg="white",background="grey",activebackground="lightgrey", fg="white",font=setFont, command=ShowSetWindow)
    setFrame.pack(side="top")
    settingsBtn.place(x = 5,y = 3)
    ############################################################################# Левый нижний Frame
    PlayListFrame = Frame(root,background="grey",width=250,height=350,borderwidth = 3,relief="ridge").pack(side="left")
    ############################################################################# Правый нижний Frame
    PlayMusicFrame = Frame(root,width=470,background="grey",height=340,borderwidth = 3,relief="ridge")

    MusicList = Listbox(PlayMusicFrame, background="grey", width=77,height=12,selectmode=SINGLE,foreground="white")

    playImg = PhotoImage(file="img/music-player.png")
    pauseImg = PhotoImage(file="img/pause-sign.png")
    Playbtn = Button(PlayMusicFrame,width=64,height=64,image=playImg,background="grey",bg="grey",borderwidth=0,activebackground="grey",command=playMusic)

    status = StringVar(PlayMusicFrame,value=statusText)

    StatusLabel = Label(PlayMusicFrame,textvariable=status,background="grey",foreground="white")

    PlayMusicFrame.pack(side="right")
    MusicList.place(x= 232,y=320 - 225, anchor="center")
    Playbtn.place(x= 235,y=320 - 64, anchor="center")
    StatusLabel.place(x= 235,y=320 - 12,anchor="center")
    
    Start()

    root.protocol("WM_DELETE_WINDOW", ExitDef)
    root.mainloop()



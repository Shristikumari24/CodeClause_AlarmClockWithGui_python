from time import strftime 
from tkinter import * 

import time
import datetime
from pygame import mixer
 
root = Tk() 
root.geometry("500x350")
root.configure(bg="#FAEBD7")
root.title('Shristi Alarm-Clock') 

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 

def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 20, 'bold'),
            text="Wake up!Wake up!Wake up",bg="DodgerBlue2",fg="white").grid(row=6,columnspan=3)
            print("wake up!")
            mixer.init()
            mixer.music.load(r'C:\Users\shris\Music\ggg.mp3')
            mixer.music.play()
            break
 

hrs=StringVar()
mins=StringVar()
secs=StringVar()


greet=Label(root, font = ('arial', 20, 'bold'),
text="Take a short nap!")
greet.place(x=120,y=50)


hrbtn=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold')).place(x=90,y=110)


minbtn=Entry(root,textvariable=mins,
width=5,font = ('arial', 20, 'bold')).place(x=200,y=110)



secbtn=Entry(root,textvariable=secs,
width=5,font = ('arial', 20, 'bold')).place(x=300,y=110)


setbtn=Button(root,text="set alarm",command=setalarm,bg="DodgerBlue2",
fg="white",font = ('arial', 20, 'bold')).place(x=160,y=160)

timeleft = Label(root,font=('arial', 20, 'bold')) 
timeleft.grid()
  
mainloop() 
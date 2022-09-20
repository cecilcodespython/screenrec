from tkinter import *
from tkinter import filedialog
import pyscreenrec,os



root = Tk()
root.title("Screenrec")
root.geometry("300x300")
root.configure(bg='#020100')
root.resizable(False,False)

recorder = pyscreenrec.ScreenRecorder()

rec_img = PhotoImage(file='button.png')
stop_img = PhotoImage(file='stop-button.png')
pause_img = PhotoImage(file='video-pause-button.png')

def start_recording():
    recorder.start_recording('recording.mp4',5)

def stop_recording():
    recorder.stop_recording()


def pause_recording():
    pause_reset = False
    if pause_reset == False:
        recorder.pause_recording()
        pause_reset = True
        if pause_reset == True:
            recorder.resume_recording()
            pause_reset=False


    



start_rec = Button(root,image=rec_img,command=start_recording)
start_rec.place(x=120,y=20)

stop_rec = Button(root,image=stop_img,command=stop_recording)
stop_rec.place(x=120,y=100)

pause_rec = Button(root,image=pause_img,command=pause_recording)
pause_rec.place(x=120,y=180)






root.mainloop()

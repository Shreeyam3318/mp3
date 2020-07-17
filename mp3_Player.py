def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100


def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.1)
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100


def stopmusic():
    mixer.music.stop()

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid()
    root.ResumeButton.grid()

def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value']=40
    ProgressbarVolumeLabel['text']='40%'

    mixer.music.play()

    song=MP3(ad)
    totalsonglegth=int(song.info.length)
    ProgressbarMusic['maximum']=totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    




def musicurl():
    dd=filedialog.askopenfilename()
    print(dd)
    audiotrack.set(dd)

def createwidthes():

    global implay, impause, imbrowse, imvolumeup, imvolumedown, imstop, imresume, ProgressbarVolumeLabel, ProgressbarVolume, ProgressbarLabel
    global ProgressbarMusicLabel, ProgressbarMusic, ProgressbarMusicEndTimeLabel, ProgressbarMusicStartTimeLabel, ProgressbarMusiczz
#label
    TrackLabel=Label(root, text='Select Audio Track: ', bg="royalblue", font=('arial', 15, 'italic bold'))
    TrackLabel.grid(row=0, column=0, padx=20, pady=20)

#entrybox

    TrackLabelEntry=Entry(root, font=('arial', 15, 'italic bold'), width=35, textvariable=audiotrack)
    TrackLabelEntry.grid(row=0, column=1, padx=20, pady=20)

#buttons

    BrowseButton=Button(root, text='Search', width=20, bd=5, activebackground='grey', command=musicurl)
    BrowseButton.grid(row=0, column=2, padx=20, pady=20)


    PlayButton = Button(root, text='Play',bg='gold2', width=20, bd=5, activebackground='grey', command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)


    root.PauseButton = Button(root, text='Pause', bg='IndianRed1', width=20, bd=5, activebackground='grey', command=pausemusic)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)


    root.ResumeButton = Button(root, text='Resume', bg='IndianRed1', width=20, bd=5, activebackground='grey', command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    VolumeupButton = Button(root, text='Vol+', bg='orchid4', width=20, bd=5, activebackground='grey', command=volumeup)
    VolumeupButton.grid(row=1, column=2, padx=20, pady=20)


    StopButton = Button(root, text='Stop', bg='firebrick4', width=20, bd=5, activebackground='grey', command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)


    VolumedownButton = Button(root, text='Vol-', bg='green', width=20, bd=5, activebackground='grey', command=volumedown)
    VolumedownButton.grid(row=2, column=2, padx=20, pady=20)

# Progress bar volume


    ProgressbarLabel=Label(root, text='', bg='brown')
    ProgressbarLabel.grid(row=0, column=3, rowspan=3, padx=20, pady=20)
    ProgressbarLabel.grid_remove()
    ProgressbarVolume=Progressbar(ProgressbarLabel, orient=VERTICAL, mode='determinate', value=0, length=190)

    ProgressbarVolume.grid(row=0, column=0, ipadx=5)

    ProgressbarVolumeLabel=Label(ProgressbarLabel, text='0%', bg='lightgray', width=3)
    ProgressbarVolumeLabel.grid(row=0, column=0)

# music left

    ProgressbarMusicLabel = Label(root, text='', bg='brown')
    ProgressbarMusicLabel.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text='0:00:00', bg='brown', width=5)
    ProgressbarMusicStartTimeLabel.grid(row=0, column=0)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text='0:00:00', bg='brown')
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)

    ProgressbarMusic=Progressbar(ProgressbarMusicLabel, orient=HORIZONTAL, mode='determinate', value=0)

    ProgressbarMusic.grid(row=0, column=1, ipadx=370, ipady=3)




from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root= Tk()

root.geometry('1100x500+200+50')
root.title('mp3 Player')
root.iconbitmap('music.ico')
root.resizable(False, False)
root.configure(bg="royalblue")

#audiotrack

audiotrack=StringVar()

currentvol=0

totalsonglength=0





mixer.init()
createwidthes()
root.mainloop()

import tkinter
from time import strftime

relogio = tkinter.Label()
relogio.pack()
relogio['font'] = 'Helvetica 60 bold'
relogio['text'] = strftime('%H:%M:%S')


def tictac():
    agora = strftime('%H:%M:%S')
    relogio['text'] = agora
    relogio.after(40, tictac)


tictac()
relogio.mainloop()

"""O método mainloop é usado para "travar" a execução da janela atual usando um event loop do tkinter. Isso permite
com que o tkinter possa disparar respostas a eventos na instância atual da janela que chamou o mainloop,
como um keypress ou click e não permite a execução de códigos posteriores até que a janela seja fechada. Pode testar
isso ao chamar o método mainloop com um código logo em seguida e verá que ele só será executado depois que fechar a
janela

"""
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
# esse print não será chamado até que feche a janela que chamou o método mainloop
relogio.mainloop()
print('Programa fechado')

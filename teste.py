import tkinter as tk
from random import randint

# Janela

janela = tk.Tk()
janela.geometry('500x500')
janela.configure(bg='black')

#titulo

pergunta = tk.Label(janela, text='Hide and sick')
pergunta.pack(anchor='n', pady=200)

#===========================vareaveis=====================================================
spaw = randint(0,490)

#===========================================FUNÇOES=======================================
def hover(event):
    x = spaw
    y = spaw
    nao.place(x=x,y=y)

def X():
        nao= tk.Button(janela, text=' x ', command= '')
        nao.place(x=300, y=230)
        nao.bind('<Enter>',hover)

nao= tk.Button(janela, text=' x ', command= '')
nao.place(x=300, y=230)
nao.bind('<Enter>',hover)

X()


janela.mainloop()
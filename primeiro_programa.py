import tkinter as tk
from typing import Text

ALTURA = 500
LARGURA = 800

def escreve():
    print('teste')

def escreve2():
    print('ola mundo!')

def escreve_mensagem(msg):
    print(msg)

root = tk.Tk()#janela

canvas = tk.Canvas(root, height=ALTURA, width=LARGURA)
canvas.pack()

frame1 = tk.Frame(root, bg='blue')
frame1.place(relx=0.0,rely=0.0,relwidth=1,relheight=0.5)

frame2 = tk.Frame(root, bg='green')
frame2.place(relx=0.0,rely=0.5,relwidth=1,relheight=0.5)

label = tk.Label(frame1,text="Ola mundo!", bg='green')
#label.pack()
label.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.1)

entrada = tk.Entry(frame1, bg='white')
entrada.place(relx=0.2,rely=0.2,relwidth=0.5,relheight=0.1)

label = tk.Label(frame2,text="Ola mundo!", bg='green')
#label.pack()
label.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.1)

entrada = tk.Entry(frame2, bg='white')
entrada.place(relx=0.2,rely=0.2,relwidth=0.5,relheight=0.1)

def teste():
    texto = entrada.get()
    print(texto)

botao1 = tk.Button(frame2, text="Clique aqui", bg='yellow', fg='blue',command=escreve)
botao1.place(relx=0.2,rely=0.3,relwidth=0.5,relheight=0.1)

botao2 = tk.Button(frame2, text="Clique aqui", bg='white', fg='blue',command=lambda: escreve_mensagem(entrada.get()))
botao2.place(relx=0.2,rely=0.4,relwidth=0.5,relheight=0.1)



root.mainloop()


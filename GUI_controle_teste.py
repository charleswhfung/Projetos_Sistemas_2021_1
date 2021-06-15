import tkinter as tk
import serial
import time

ALTURA = 500
LARGURA = 500

dado_enviado = 'N'

s = serial.Serial('COM4')

def envia_caractere():
    print('A')
    s.write(b'A')

def envia_caractere_direita():
    global dado_enviado 
    dado_enviado = 'A'
    #print('A')
    #s.write(b'A')

def envia_caractere_esquerda():
    global dado_enviado 
    dado_enviado = 'B'
    #print('B')
    #s.write(b'B')

def envia_dado():
    print('Enviando')
    print(dado_enviado)
    s.write(dado_enviado.encode("utf-8"))
    janela.after(10, envia_dado)


def escreve_mensagem(msg):
    print(msg)
    for i in range(len(msg)):#ola mundo
        s.write(msg[i].encode("utf-8"))
        time.sleep(0.1)


janela = tk.Tk()

janela.title('Interface Serial')

canvas = tk.Canvas(janela,height=ALTURA,width=LARGURA)
canvas.pack()

frame = tk.Frame(janela, bg='blue')
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

entrada = tk.Entry(frame,font = "Helvetica 44 bold", bg='white')
entrada.place(relx=0,rely=0,relwidth=1,relheight=0.2)

botaoEsquerda = tk.Button(frame,font = "Helvetica 44 bold", text="Esquerda",bg='gray',command=envia_caractere_esquerda)
botaoEsquerda.place(relx=0,rely=0.3,relwidth=0.5,relheight=0.2)

botaoDireita = tk.Button(frame,font = "Helvetica 44 bold", text="Direita",bg='gray',command=envia_caractere_direita)
botaoDireita.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.2)

botaoCaractere = tk.Button(frame,font = "Helvetica 33 bold", text="Envia um caractere", bg='brown',fg='white',command=envia_caractere)
botaoCaractere.place(relx=0,rely=0.6,relwidth=1,relheight=0.2)


janela.after(10, envia_dado)
janela.mainloop()




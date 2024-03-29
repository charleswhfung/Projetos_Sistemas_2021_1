import tkinter as tk
import serial
import time

ALTURA = 500
LARGURA = 500

dado_enviado = 'P'

s = serial.Serial('COM4')

def envia_dado():
    global dado_enviado
    print(dado_enviado)
    s.write(dado_enviado.encode("utf-8"))
    janela.after(10,envia_dado)


def envia_caractere_esquerda():
    global dado_enviado
    dado_enviado = 'E'
    #print('E')
    #s.write(b'E')

def envia_caractere_direita():
    global dado_enviado
    dado_enviado = 'D'
    #print('D')
    #s.write(b'D')

def envia_caractere_parar():
    global dado_enviado
    dado_enviado = 'P'
    #print('P')
    #s.write(b'P')


def envia_caractere():
    print('A')
    s.write(b'A')


def escreve_mensagem(msg):
    print(msg)
    for i in range(len(msg)):#ola mundo
        s.write(msg[i].encode("utf-8"))
        time.sleep(0.1)


janela = tk.Tk()

janela.title('Controle de motor de passo')

canvas = tk.Canvas(janela,height=ALTURA,width=LARGURA)
canvas.pack()

frame = tk.Frame(janela, bg='blue')
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

botaoEsquerda = tk.Button(frame,font = "Helvetica 33 bold",text="Esquerda",bg='gray', command=envia_caractere_esquerda)
botaoEsquerda.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.2)

botaoDireita = tk.Button(frame,font = "Helvetica 33 bold",text="Direita",bg='gray', command=envia_caractere_direita)
botaoDireita.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.2)

botaoParada = tk.Button(frame,font = "Helvetica 33 bold",text="Parar",bg='red',fg='white', command=envia_caractere_parar)
botaoParada.place(relx=0,rely=0.5,relwidth=1,relheight=0.2)

janela.after(10,envia_dado)
janela.mainloop()




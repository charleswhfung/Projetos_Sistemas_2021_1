import tkinter as tk
import serial
import time

ALTURA = 500
LARGURA = 500

s = serial.Serial('COM4')

def envia_caractere_esquerda():
    print('E')
    s.write(b'E')

def envia_caractere_direita():
    print('D')
    s.write(b'D')

def envia_caractere_parar():
    print('P')
    s.write(b'P')


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

janela.mainloop()




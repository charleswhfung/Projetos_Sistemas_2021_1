import mysql.connector
import datetime
from pylive import live_plotter
import numpy as np
import serial as sr

#https://github.com/makerportal/pylive

s = sr.Serial('COM3',9600)

con = mysql.connector.connect(host='localhost',database='db_teste',user='root',password='123456')

size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.random.randn(len(x_vec))
line1 = []

while True:
    ser_bytes = s.read()
    valor = int.from_bytes(ser_bytes, "little")
    rand_val = valor
    print(valor)
    #rand_val = np.random.randn(1)
    y_vec[-1] = rand_val
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)

    con = mysql.connector.connect(host='localhost',database='db_teste',user='root',password='123456')

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor Mysql ",db_info)
        now = datetime.datetime.now()
        print(now.year, now.month, now.day, now.hour, now.minute, now.second)

        horario = now.strftime("%d-%b-%Y (%H:%M:%S)")
        print('Horario atual : ', horario)

        cursor = con.cursor()

        sql = "INSERT INTO dados (sensor, horario) VALUES (%s, %s)"
        val = (valor, horario)
        cursor.execute(sql,val)

        con.commit()

        con.close()
        print("Conexão encerrada")


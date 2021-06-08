import mysql.connector
import datetime
import matplotlib.pyplot as plt
import numpy as np

con = mysql.connector.connect(host='localhost',database='db_teste',user='root',password='123456')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor Mysql ",db_info)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    horario = now.strftime("%d-%b-%Y (%H:%M:%S)")
    print('Horario atual : ', horario)

    cursor = con.cursor()

    cursor.execute("SELECT sensor FROM dados")

    resultado = cursor.fetchall()

    dados_y = []
    dados_x = []

    for x in resultado:
        print(x[0])
        dados_y.append(x[0])

    for aux in range(len(dados_y)):
        dados_x.append(aux)

    print("tamanhoy "+ str(len(dados_y)))
    print("tamanhox "+ str(len(dados_x)))

    plt.plot(dados_x, dados_y)
    plt.show()
    
    con.close()
    print("Conexão encerrada")


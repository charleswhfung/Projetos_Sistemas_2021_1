import mysql.connector
import datetime

con = mysql.connector.connect(host='localhost',database='leitura',user='root',password='123456')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor Mysql ",db_info)

    con.close()
    print("Conexão encerrada")


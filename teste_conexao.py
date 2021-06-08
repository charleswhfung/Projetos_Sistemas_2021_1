import mysql.connector
import datetime

con = mysql.connector.connect(host='localhost',database='leitura',user='root',password='123456')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor Mysql ",db_info)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    horario = now.strftime("%d-%b-%Y (%H:%M:%S)")
    print('Horario atual : ', horario)

    cursor = con.cursor()

    sql = "INSERT INTO dados (sensor, horario) VALUES (%s, %s)"
    val = (100, horario)
    cursor.execute(sql,val)

    con.commit()

    con.close()
    print("Conexão encerrada")


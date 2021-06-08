import datetime

now = datetime.datetime.now()

horario = now.strftime("%d-%b-%Y (%H:%M:%S)")
print('Horario atual : ', horario)

print(now)


import serial as sr
import matplotlib.pyplot as plt
import numpy as np

s = sr.Serial('COM3',9600)
plt.close('all')
plt.figure()
plt.ion()
plt.show()

data = np.array([])
i=0
while True:
    #a = s.read()
    #a.decode()
    #print(a)
    #ser_bytes = s.readline()
    ser_bytes = s.read()
    valor = int.from_bytes(ser_bytes, "little")
    print(valor)
    #print(ser_bytes)
    #print(ser_bytes[1:-1])
    #decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    
    #aux = int.from_bytes(a, byteorder='little')
    #print(aux)
    
    b = float(valor)
    data = np.append(data,b)
    plt.cla()
    plt.plot(data)
    plt.pause(0.01)
    i=i+1

s.close()
import serial

s = serial.Serial('COM3')

while True:
    res = s.read()
    print(res)
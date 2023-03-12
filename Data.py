from picamera import PiCamera
import Adafruit_BMP.BMP085 as BMP085
import time 
import serial


lora=serial.Serial(port='/dev/ttyAMA0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
sensor = BMP085.BMP085()
x = 1



while True:

	n = ('Presion = ' + str((sensor.read_pressure())/100) + ' Hpa' + 'Temperatura = {0:0.2f} *C '.format(sensor.read_temperature()) + '\n')
	b = bytes(n,'utf-8')
	s= lora.write(b)
	time.sleep(1)
	camera = PiCamera()	
	camera.capture('/home/cansat/Desktop/Registro_Cansat/Foto%s.jpg' % x)
	camera.close()
	n = ('Presion = ' + str((sensor.read_pressure())/100) + ' Hpa' + 'Temperatura = {0:0.2f} *C '.format(sensor.read_temperature()) + '\n')
	b = bytes(n,'utf-8')
	s= lora.write(b)
	x += 1
	time.sleep(1)
    

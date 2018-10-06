import RPi.GPIO as GPIO
import time

LED = 32			#pin no. as per BOARD, GPIO18 as per BCM


#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)	#set GPIO as output
GPIO.output(LED, GPIO.HIGH)
print('pin ' + str(LED) + ' is high')
time.sleep(40)

GPIO.cleanup()

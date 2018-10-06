import RPi.GPIO as GPIO
import time

LED=None
BLINK=None
PWM = None
blink = None
pwm = None

LED = 36			#pin no. as per BOARD, GPIO18 as per BCM
BLINK = 32
PWM = 12

runtime = 10

def setout(pin):
    GPIO.setup(pin, GPIO.OUT)
    print( 'pin ' + str(pin) + ' is OUT' )

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BOARD)
try:
    if LED:
        setout(LED)	#set GPIO as output
    if BLINK:
        setout(BLINK)	#set GPIO as output
    if PWM:
        setout(PWM)	#set GPIO as output

    if LED:
        GPIO.output(LED, GPIO.HIGH)
        print('pin ' + str(LED) + ' is high')

    # on
        # GPIO.output(PWM, GPIO.HIGH)
        # print('pin ' + str(PWM) + ' is high')
        # time.sleep(runtime)
    if BLINK:
        blink = GPIO.PWM(BLINK, 1.6)
        blink.start(50)
        print('pin ' + str(BLINK) + ' is BLINK')
        if not PWM:
            time.sleep(runtime)
    if PWM:
        pwm = GPIO.PWM(PWM, 500)
        print('pin ' + str(PWM) + ' is PWM')
        step = 8
        sleeptime = 0.3
        n = runtime / sleeptime
        i=0
        pwm.start(100)
        # pwm.ChangeDutyCycle(100.0)
        # time.sleep(runtime)
        while i<n:
            for dc in range(-50, 50, step):
                adc = 100-abs(dc)
                pwm.ChangeDutyCycle(adc)
                print( 'i=' + str(i) + " dc="+str(adc))
                time.sleep(sleeptime)
                i=i+1




except KeyboardInterrupt:
    pass
finally:
    GPIO.output(LED, GPIO.LOW)
    if LED:
        GPIO.output(LED, GPIO.LOW)
    if not blink is None:
        blink.stop()
    if pwm:
        pwm.stop()
    GPIO.cleanup()
    print('cleaned')

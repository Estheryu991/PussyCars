
import RPIO

GPIO.setup("P9_12", GPIO.OUT)
RPI.init()
while True:
if(RPIO.pwm(0, 1000):
GPIO.output("P9_12", GPIO.HIGH)
else:
GPIO.output("P9_12", GPIO.LOW)

P8_5 = GPIO.PWM(channel=1, frequency=100000, duty_cycle=10)
P8_5.start(duty) 
P8_5.set_duty(duty)
P8_5.stop()
P8_5.dispose()

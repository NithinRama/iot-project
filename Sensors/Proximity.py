import time
import RPio.GPIO as GPIO
class Proximity:
    def __init__(self,trig,echo):
        self.trig = trig
        self.echo = echo
    def get_distance(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo.GPIO.IN)
        time.sleep(2)
        GPIO.output(self.trig,True)
        time.sleep(0.0001)
        GPIO.output(self.trig,False)
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        dis = pulse_duration*17150
        dis = round(dis,2)
        return dis

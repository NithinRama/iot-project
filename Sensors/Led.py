import RPio.GPIO as GPIO
GPIO.setmode(GPIo.BCM)
class Led:
    def __init__(self,led_pin):
        self.led_pin = led_pin
        GPIO.setup(self.led_pin,GPIO.OUT)
    def led_on(self):
        GPIO.output(self.led_pin,GPIO.HIGH)
    def led_off(self):
        GPIO.output(self.led_pin,GPIO.LOW)
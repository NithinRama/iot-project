import time
import RPi.GPIO as GPIO
class Temperature:
    def __init__(self,device_id):
        self.device_id = device_id
        self.tempStore = open("/sys/bus/w1/devices/"+device_id+"/w1_slave")
    def get_temp(self):
        data = self.tempStore.read()
        self.tempStore.close()
        tempData = data.split("\n")[1].split(" ")[9]
        temperature = float(tempData[2:])
        temperature = temperature/1000
        return temperature
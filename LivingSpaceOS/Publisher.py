import time
import json
import paho.mqtt.client as paho
import config
from NewClient import addressFilePath
import random

def on_connect(client, userdata, flags, rc):
    pass

def on_publish(client, userdata, mid):
    pass

def on_message(client, userdata, msg):
    print("Received " + msg.payload.decode() + " From " + msg.topic)

def ConnectToMqttBroker():
    """
        Connects to a MQTT broker and returns the client object
    """
    client = paho.Client("Pub", protocol = paho.MQTTv31)
    client.on_connect = on_connect
    client.connect(config.mqttBrokerIp, config.mqttPort)
    client.on_publish = on_publish
    client.on_message = on_message
    return client


if __name__ == '__main__':
    client = ConnectToMqttBroker()
    client.loop_start()
    
    topics = json.loads(open(addressFilePath, 'r').read())
    
    for topic in topics:
        client.subscribe(topic + "controlLed", 1)

    while True:
        tempData = random.randint(30, 70)
        proxData = random.randint(10, 30)
        ledStatus = "off"
        topics = json.loads(open(addressFilePath, 'r').read())
        
        for topic in topics:
            client.publish(topic + "led", ledStatus)

            if topics[topic]["temp"]:
                client.publish(topic + "temp", tempData)
            
            if topics[topic]["prox"]:
                client.publish(topic + "prox", proxData)

        time.sleep(60)
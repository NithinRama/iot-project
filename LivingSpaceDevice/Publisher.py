import time
import json
import paho.mqtt.client as paho
from NewClient import addressFilePath


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def ConnectToMqttBroker(ip):
    """
        Connects to a MQTT broker and returns the client object
    """
    client = paho.Client("Pub", protocol = paho.MQTTv31)
    client.on_connect = on_connect
    client.connect(ip, 9000)
    client.on_publish = on_publish
    return client


if __name__ == '__main__':
    client = ConnectToMqttBroker("127.0.0.1")
    client.loop_start()
    while True:
        # Should be replaced by various sensor data
        data = "RANDOM"
        topics = json.loads(open(addressFilePath, 'r').read())
        
        for topic in topics:
            print(topic)
            client.publish(topic[1: len(topic) - 1], data)
        
        time.sleep(5)


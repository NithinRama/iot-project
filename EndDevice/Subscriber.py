import paho.mqtt.client as paho
import time
from iota import *
from array import array
import json

class IotOS:

    def __init__(self, LivingSpaceAddress, seed, iotaUrl, mqttBrokerIp, mqttPort):
        self.seed = seed
        self.LivingSpaceAddress = LivingSpaceAddress
        self.onTempReceived = None
        self.onProximityReceived = None
        self.onLedStatusReceived = None
        self.iotaUrl = iotaUrl
        self.mqttBrokerIp = mqttBrokerIp
        self.mqttPort = mqttPort
        self.client = None

    def PushTransactionToIota(self, message):
        """Method to add transactions of data to the Tangle"""
        api = Iota(
            # URI of a locally running node.
            self.iotaUrl,

            # Seed used for cryptographic functions.
            seed = str(self.seed).encode()
        )
        api.send_transfer(
        depth = 1,

        # One or more :py:class:`ProposedTransaction` objects to add to the
        # bundle.
        transfers = [
            ProposedTransaction(
            # Recipient of the transfer.
            address =
                Address(
                self.LivingSpaceAddress.encode()
                ),

            # Amount of IOTA to transfer.
            # This value may be zero.
            value = 0,

            # Optional tag to attach to the transfer.
            tag = Tag(b'TAG'),

            # Optional message to include with the transfer.
            message = TryteString.from_string(message),
            ),
        ],
        )
    
    def start(self, tempReceiver, ledReceiver, proximityReceiver):

        def on_connect(client, userdata, flags, rc):
            print("Connected Successfully......")

        def on_subscribe(client, userdata, mid, granted_qos):
            print("Subscribed: " + str(mid) + " " + str(granted_qos))

        def on_message(client, userdata, msg):
            """
            This function is called whenever a message is recieved on a topic
            """
            topic = msg.topic
            payload = msg.payload.decode()
            if topic == self.LivingSpaceAddress + "temp":
                self.onTempReceived(payload)

            elif topic == self.LivingSpaceAddress + "prox":
                self.onProximityReceived(payload)
            
            elif topic == self.LivingSpaceAddress + "led":
                self.onLedStatusReceived(payload)

            self.PushTransactionToIota(topic)
        
        self.onLedStatusReceived = ledReceiver
        self.onProximityReceived = proximityReceiver
        self.onTempReceived = tempReceiver

        self.client = paho.Client("sub", protocol = paho.MQTTv31)
        self.client.on_connect = on_connect
        self.client.connect(self.mqttBrokerIp, self.mqttPort)
        self.client.on_message = on_message
        self.client.on_subscribe = on_subscribe
        self.client.subscribe(self.LivingSpaceAddress + "temp", 1)
        self.client.subscribe(self.LivingSpaceAddress + "prox", 1)
        self.client.subscribe(self.LivingSpaceAddress + "led", 1)
        self.client.loop_forever()

    def controlLed(self, command):
        print("Controlling LED : " + str(command))
        self.client.publish(self.LivingSpaceAddress + "controlLed", command)


if __name__ == '__main__':
    
    device = IotOS('TISMJUFNRBRHXVH9AITQQRPRFJAPJWWOMPYXMNVPPMYJCRFJGBHFAFKVMNWFZKCPSN9DPVNBBXNBAKKNW', 'BETHESEED', 'http://localhost:5000/', '127.0.0.1', 9000)

    def tempRec(msg):
        print("Temperature is : " + msg)
        data = int(msg)
        device.controlLed("ON")

    def ledRec(msg):
        print('Led is : ' + msg)

    def proxRecd(msg):
        print('Prox is : ' + msg)

    device.start(tempRec, ledRec, proxRecd)

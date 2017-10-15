import paho.mqtt.client as paho
import time
from iota import *
from array import array

LivinSpaceAddress = "JSRJDCGVCQJWNSXLHUMPESZBMMFENFWTGNHQDAXXHZKDGLMVTAYX9KUNFNPVSBDYDWUJHWOKUQZCDVVCX"

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    """
    This function is called whenever a message is recieved on a topic
    """
    print(msg.topic + " " + str(msg.qos) + " "+ str(msg.payload))
    PushTransactionToIota(str(msg.payload))

def PushTransactionToIota(message):
    api =\
    Iota(
        # URI of a locally running node.
        'http://localhost:5000/',

        # Seed used for cryptographic functions.
        seed = b'SEED9GOES9'
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
              LivinSpaceAddress.encode()
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

if __name__ == '__main__':
    client = paho.Client("sub", protocol = paho.MQTTv31)
    client.on_connect = on_connect
    client.connect("127.0.0.1", 9000)
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.subscribe(LivinSpaceAddress, 1)
    client.loop_forever()

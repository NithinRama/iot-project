.. IotOS documentation master file, created by
   sphinx-quickstart on Sun Nov 12 17:28:20 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to `IotOS <https://github.com/abhivijay96/iot-project>`_
=================================================================
IotOs is an attemp to provide IOT as a service. All the payments and transactions of the service is managed by `IOTA <https://iota.readme.io/>`_. Every living space can have multiple sensors and actuators which can be used by the clients through this design. Each living space becomes a Node in the IOTA netowork.

Design Approach
--------------------

Architecture
^^^^^^^^^^^^^
1. Every living space is a Node in the IOTA network. (We will be referring to living spaces as Nodes for the rest of the documentation)
2. MQTT is used by these nodes to publish Data to the clients.
3. Every client gets an address based on the services to which the client has agreed to pay.
4. Each Node provides data regarding temperature, proximity, and a control to a Light. (Adding more features in the coming releases!)
5. The service provider tracks the payment of the client for every transaction(data read through mqtt netowrk) using IOTA and can decide to continue or discontinue the service to that client address.

Use-Cases
^^^^^^^^^^
1. **Be a client** - Use the service we provide. In this approach the clients get a unique adderss and IOTA network URL and mqtt broker IP and port. using which they create an instance of a device. This device then is responsible for providing the incoming data of the node to the client and adding transactions to the tangle.::

    device = IotOS('youraddress', 'YOURSEED', 'iotaURL', 'mqttBrokerIp', mqttBrokerPort)

    ## YOURSEED should conatin only A-Z0-9
    def tempRec(msg):
        print("Temperature is : " + msg)
        data = int(msg)
        device.controlLed("ON")

    def ledRec(msg):
        print('Led is : ' + msg)

    def proxRecd(msg):
        print('Prox is : ' + msg)

    device.start(tempRec, ledRec, proxRecd)

2. **Be a Service provider** - Here you can add on to the services we have built and change the subscriber sdk which the clients will be using to access your service. You can choose the IOTA network and MQTT broker or create your own.

    Example of adding new service
    **Edit NewClient.py**::

        addresses[address] = {"temp": temp, "prox": proxy, "newSensor": newSensor}
        # where newSensor is a boolean indicating if the client has requested service for the newSensor

    **Edit Publisher.py**::

        if topics[topic]["newSensor"]:
                client.publish(topic + "newSensor", newSensorData)

    **Edit Subscriber.py**::

        elif topic == self.LivingSpaceAddress + "newSensor":
                self.onNewSensorReceived(payload)
        # Implement support for handing every new type of sensor


.. toctree::
   :maxdepth: 2
   :caption: Contents:

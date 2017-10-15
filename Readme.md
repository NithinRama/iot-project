# IoT as a platform with IOTA as a ledger for Transactions
## Components
- IOTA Node
- Mqtt Broker
- Mqtt Pub/Sub

## IOTA Node
`cd Node`
`java -jar iri-1.4.0.jar -p 5000`

## Mqtt Broker
`sudo apt-get install mosquitto mosqutto-client`
`mosquitto -p 9000`

## Mqtt Publisher
`cd LivingSpaceDevice`

`python3.6 NewClient.py`
This outputs a new address for a new client

`python3.6 Publisher.py`
This starts publishing events to all the addresses as topics

`python3.6 GetTransactions.py`
This gets all the transactions associated with the seed and it's account, this can be used to monitor M2M payments (in the actual IOTA network) and stop services to compromised nodes.

## Mqtt Subscriber

`cd EndDevice`

Replace the value of `LivinSpaceAddress` to the address which was given by `NewClient.py` previously.

`python3.6 Subscribe.py`

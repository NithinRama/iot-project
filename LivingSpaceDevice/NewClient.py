from iota import Iota, __version__
from iota import commands
from iota.crypto.types import Seed
import json
import os, time

seed = 'SECRETKEY'
addressFilePath = 'addresses.json'

def NewAddress():
    """
        Returns an address using which a client can make a transaction with this publisher, Returns None on error
    """
    api = Iota('http://localhost:5000/', seed)
    
    l = 0
    if not os.path.isfile(addressFilePath):
        l = 1

    else:
        l = len(json.loads(open(addressFilePath, 'r').read()))

    api_response = api.get_new_addresses(l + 2, 1)

    try:
        return str(api_response['addresses'][-1])
    
    except e as Exception:
        return None
    
def StoreAddress(address):
    """
    Stores the passed address in a pickle file to be used while publishing
    """
    
    if not os.path.isfile(addressFilePath):
        a = []
        temp = json.dumps(a)
        with open(addressFilePath, 'w') as addressFile:
            addressFile.write(temp)
    
    addresses = json.loads(open(addressFilePath, 'r').read())
    addresses.append(json.dumps(address))

    with open(addressFilePath, 'w') as addressFile:
            addressFile.write(json.dumps(addresses))

def CreateNewClient():
    """
    Creates a new Address and stores it for publishing events and 
    """
    address = NewAddress()

    if address is None:
        return None

    StoreAddress(address)
    return address

if __name__ == '__main__':
    print(CreateNewClient())


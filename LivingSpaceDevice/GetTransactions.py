from iota import Iota, __version__, codecs
from iota import commands
from iota.crypto.types import Seed
from NewClient import seed

api = Iota('http://localhost:5000/', seed)
data = api.get_account_data()
bundles = data['bundles']

for bundle in bundles:
    transactions = bundle.transactions
    messages = bundle.get_messages()
    for i in range(len(transactions)):
        print("Message: ", messages[i], ", Timestamp: ", transactions[i].timestamp, ", Address: ", transactions[i].address)
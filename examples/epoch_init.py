from sgb_ftso_contracts import *
from web3 import Web3

rpcurl = "https://songbird.towolabs.com/rpc"

# Init web3
web3 = Web3(Web3.HTTPProvider(rpcurl))

# Init an ftso factory
ftsoFactory = Ftso("ADA")
ftsoADA = ftsoFactory.contract(web3)

# Some block that has already occured
endblock = 20481300

# Discern when price epochs occur in the context of chain blocks.
# Blocks are not produced at a constant rate, so this mapping cannot be determined by formula.
epochInitFilter = ftsoADA.events.PriceEpochInitializedOnFtso.createFilter(fromBlock=endblock - 256, toBlock=endblock)
events = epochInitFilter.get_all_entries()
for event in events:
  print(f"Over block range: {endblock - 256} to {endblock}")
  print(f"At block: {event['blockNumber']}")
  print(f"The price epoch was: {event['args']['epochId']}")
  print(f"And the price epoch ends at Unix epoch timestamp: {event['args']['endTime']}")

from sgb_ftso_contracts import Ftso, PriceSubmitter
from web3 import Web3

# Define the blockchain endpoint to use
rpcurl = "https://songbird-api.flare.network/ext/bc/C/rpc"

# Init web3
web3 = Web3(Web3.HTTPProvider(rpcurl))

# Init the ftsoManager factory
ftsoFactory = Ftso("ADA")
ftsoADA = ftsoFactory.contract(web3)

# Get the PriceSubmitter contract
priceSubmitterFactory = PriceSubmitter()
priceSubmitter = priceSubmitterFactory.contract(web3)

# This search happens over a block range, so it is necessary to define that range.
endblock = 20481300

# Create an event filter
revealfilter = priceSubmitter.events.PricesRevealed.createFilter(fromBlock=endblock - 15, toBlock=endblock + 15)
events = revealfilter.get_all_entries()
# Iterate over the events found
for event in events:
  pos = 0
  print(event["args"]["epochId"])
  print(event["args"]["voter"])
  for ftso in event["args"]["ftsos"]:
    if ftso.lower() == ftsoADA.address.lower():
      print(event["args"]["prices"][pos])
    else:
      pos += 1

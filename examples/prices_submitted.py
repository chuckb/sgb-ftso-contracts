from sgb_ftso_contracts import PriceSubmitter
from web3 import Web3

# Define the blockchain endpoint to use
rpcurl = "https://songbird-api.flare.network/ext/bc/C/rpc"

# Init web3
web3 = Web3(Web3.HTTPProvider(rpcurl))

# Get the PriceSubmitter contract
priceSubmitterFactory = PriceSubmitter()
priceSubmitter = priceSubmitterFactory.contract(web3)

# This search happens over a block range, so it is necessary to define that range.
endblock = 20481300
submitfilter = priceSubmitter.events.PriceHashesSubmitted.createFilter(fromBlock=endblock - 30, toBlock=endblock)
events = submitfilter.get_all_entries()
for event in events:
  print(event["args"]["submitter"])
  print(event["args"]["epochId"])
  print(event["args"]["ftsos"])
  print(event["args"]["timestamp"])

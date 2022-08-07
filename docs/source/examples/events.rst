======
Events
======

The Songbird smart contract collection fires many events that can give you insight on Ftso operations as they happened.
Any event can be fetched, so long as you know what block range to look for. It is unwise to start a block 0, scanning
all blocks in the chain. Most API providers will not allow this operation. So one should build and keep a mapping of block to 
something like price epoch or reward epoch off-chain, filtering over small block ranges shortly after they happen. This can
be done with RPC or streaming over web sockets. Web sockets are more performant but less reliable (IMHO). The examples below
use RPC.

PriceHashesSubmitted
--------------------
Retrieve logs from blocks containing the PriceHashesSubmitted event from the PriceSubmitter contract.

.. code-block:: python

  from sgb_ftso_contracts import PriceSubmitter
  from web3 import Web3

  # Define the blockchain endpoint to use
  rpcurl = "https://songbird.towolabs.com/rpc"

  # Init web3
  web3 = Web3(Web3.HTTPProvider(rpcurl))

  # Get the PriceSubmitter contract
  priceSubmitterFactory = PriceSubmitter()
  priceSubmitter = priceSubmitterFactory.contract(web3)

  # This search happens over a block range, so it is necessary to define that range.
  endblock = 20481300
  submitfilter = priceSubmitter.events.PriceHashesSubmitted.createFilter(fromBlock=endblock - 256, toBlock=endblock)
  events = submitfilter.get_all_entries()
  for event in events:
    print(event["args"]["submitter"])
    print(event["args"]["epochId"])
    print(event["args"]["ftsos"])
    print(event["args"]["timestamp"])

PricesRevealed
--------------

Retrieve logs from blocks containing the PricesRevealed event from the PriceSubmitter contract.
This example will print the revealed prices for ADA for a given epoch.

.. code-block:: python

  from sgb_ftso_contracts import Ftso, PriceSubmitter
  from web3 import Web3

  # Define the blockchain endpoint to use
  rpcurl = "https://songbird.towolabs.com/rpc"

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
  revealfilter = priceSubmitter.events.PricesRevealed.createFilter(fromBlock=endblock - 156, toBlock=endblock + 100)
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

PriceEpochInitializedOnFtso
---------------------------
Retrieve logs from blocks containing the PriceEpochInitializedOnFtso event from the ADA Ftso contract. Any Ftso would work.
Iterating over ranges of blocks, one can map blocks to price epochs, which then enable fetching other events
within the same price epoch. Knowing what blocks to go after is the key.

.. code-block:: python

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


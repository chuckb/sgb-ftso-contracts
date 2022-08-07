# Songbird FTSO Contract Factory
A small library to quickly instantiate Flare Time Series Oracle (FTSO) contracts on the Songbird network.

## Installation
pip install sgb-ftso-contracts

## Get Started
How to get prices of crypto assets tracked by the Songbird network:

```python
from sgb_ftso_contracts import Ftso
from web3 import Web3

# Songbird network RPC endpoint
# This is a free, rate-limited API node.
# Please do not abuse...
rpcurl = "https://songbird.towolabs.com/rpc"

# Init web3 with REST HTTP provider.
web3 = Web3(Web3.HTTPProvider(rpcurl))

# Create an FTSO contract instance with factory library.
btcFtso = Ftso("BTC").contract(web3)

# Fetch the latest price for Bitcoin from the FTSO.
btcDecimals = btcFtso.functions.ASSET_PRICE_USD_DECIMALS().call()
btcPriceData = btcFtso.functions.getCurrentPrice().call()

# Prices are recorded as integers. Convert to decimal format.
print(btcPriceData[0] / pow(10, btcDecimals))
```

## More

### Documentation
Documentation can be found [here](http://sgb-ftso-contracts.readthedocs.io/).

### Source code
The source code for the FTSO smart contract system, for the Songbird network can be found [here](https://gitlab.com/flarenetwork/flare-smart-contracts/-/tree/songbird-network).

### White paper
More information about the Flare Network, concepts, etc. can be found [here](https://flare.xyz/the-flare-network/).
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
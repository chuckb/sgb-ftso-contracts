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

### Contracts
The key contracts of the FTSO system are listed below:
- [Ftso](https://songbird-explorer.flare.network/address/0x20Fecb7b1Ff69C62BBA5Bb6aCD5a9743D11E246F/contracts)<br>
This is the Ftso for BTC. FTSOs are all the same contract; one instance per asset.
- [FtsoManager](https://songbird-explorer.flare.network/address/0xbfA12e4E1411B62EdA8B035d71735667422A6A9e/contracts)<br>
This contract manages FTSO voting operations and coordinates price and reward epoch execution.
- [FtsoRegistry](https://songbird-explorer.flare.network/address/0x6D222fb4544ba230d4b90BA1BfC0A01A94E6cB23/contracts)<br>
Centralized access to all FTSOs from one contract. This contract is handy to get FTSO current price info from as one does not need to go after the FTSO directly.
- [FtsoRewardManager](https://songbird-explorer.flare.network/address/0xc5738334b972745067fFa666040fdeADc66Cb925/contracts)<br>
Vote power delegators can use this contract to claim rewards and check reward status.
- [PriceSubmitter](https://songbird-explorer.flare.network/address/0x1000000000000000000000000000000000000003/contracts)<br>
Price providers use this contract to centrally submit and reveal prices to one or more of the FTSOs simultaneously.
- [VoterWhitelister](https://songbird-explorer.flare.network/address/0xa76906EfBA6dFAe155FfC4c0eb36cDF0A28ae24D/contracts)<br>
Price providers must be whitelisted in order to submit prices to the FTSOs. This contract is how they do it.
- [WNAT](https://songbird-explorer.flare.network/address/0x02f0826ef6aD107Cfc861152B32B52fD11BaB9ED/contracts)<br>
Holders of the native chain token (for the Songbird network, SGB) use this contract to wrap their Songbird and delegate vote power to FTSOs. WNAT = wrapped native

### Source code
The source code for the FTSO smart contract system, for the Songbird network, can be found [here](https://gitlab.com/flarenetwork/flare-smart-contracts/-/tree/songbird-network).

### White paper
More information about the Flare Network, concepts, etc. can be found [here](https://flare.xyz/the-flare-network/).
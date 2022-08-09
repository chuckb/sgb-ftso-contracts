from sgb_ftso_contracts import *
from web3 import Web3
from eth_account import Account
import getpass

rpcurl = "https://songbird-api.flare.network/ext/bc/C/rpc"

# Init web3
web3 = Web3(Web3.HTTPProvider(rpcurl))

# Init the WNAT contract
wNatFactory = WNAT()
wNat = wNatFactory.contract(web3)

# Setup default web3 transaction parameters. Note chain id 19 is the Songbird chain.
tx_parms = {
  'chainId': 19,
  'gas': 500000,
  'gasPrice': web3.toWei('50', 'gwei'),
  'nonce': 0
}

# Get the password to unencrypt key
password = getpass.getpass()

with open("an encrypted private key file reference goes here", 'r') as f:
  # Set up account to work with by decrypting the private key.
  encrypted = json.loads(f.read())
  privatekey = Account.decrypt(encrypted, password)
  account = Account.from_key(privatekey)
  web3.eth.default_account = account.address

  # Build the undelegate transaction
  tx_parms["nonce"] = web3.eth.getTransactionCount(account.address)
  # Percentage in basis points = % * 100
  tx = wNat.functions.delegate(web3.toChecksumAddress("delegator address goes here"), 10000).buildTransaction(tx_parms)
  signed_tx = account.sign_transaction(tx)

  # Execute the transaction
  tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
  tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
  print(f'Undelegated with tx_hash {tx_receipt["transactionHash"].hex()}')


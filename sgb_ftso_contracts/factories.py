from web3 import Web3
import requests
import json

class FactoryBase:
  def __init__(self, apiurl="https://songbird-explorer.flare.network/api"):
    self.apiurl = apiurl

  def getABI(self, address):
    url = f"{self.apiurl}?module=contract&action=getabi&address={address}"
    response = requests.get(url)
    response_json = response.json()
    abi = json.loads(response_json['result'])
    return abi

  def contract(self, web3: Web3):
    return web3.eth.contract(address=self.address, abi=self.abi)

class FtsoManager(FactoryBase):
  def __init__(self):
    FactoryBase.__init__(self)
    self.address = "0xbfA12e4E1411B62EdA8B035d71735667422A6A9e"
    self.abi = self.getABI(self.address)

class FtsoRegistry(FactoryBase):
  def __init__(self):
    FactoryBase.__init__(self)
    self.address = "0x6D222fb4544ba230d4b90BA1BfC0A01A94E6cB23"
    self.abi = self.getABI(self.address)

class Ftso(FactoryBase):
  def __init__(self, symbol):
    FactoryBase.__init__(self)
    self.symbol = symbol

  def contract(self, web3: Web3):
    # Instantiate the ftso registry
    ftsoRegistryFactory = FtsoRegistry()
    ftsoRegistry = ftsoRegistryFactory.contract(web3)
    ftsoAddress = ftsoRegistry.functions.getFtsoBySymbol(self.symbol).call()
    self.abi = self.getABI(ftsoAddress)
    ftsoContract = web3.eth.contract(address=ftsoAddress, abi=self.abi)
    return ftsoContract

class FtsoRewardManager(FactoryBase):
  def __init__(self):
    FactoryBase.__init__(self)
    self.address = '0xc5738334b972745067fFa666040fdeADc66Cb925'
    self.abi = self.getABI(self.address)

class WNAT(FactoryBase):
  def __init__(self):
    FactoryBase.__init__(self)
    self.address = '0x02f0826ef6aD107Cfc861152B32B52fD11BaB9ED'
    self.abi = self.getABI(self.address)

class PriceSubmitter(FactoryBase):
  def __init__(self):
    FactoryBase.__init__(self)
    self.address = '0x1000000000000000000000000000000000000003'
    self.abi = self.getABI(self.address)

class VoterWhitelister(FactoryBase):
  def __init__(self):
    FactoryBase.__init__(self)
    self.address = '0xa76906EfBA6dFAe155FfC4c0eb36cDF0A28ae24D'
    self.abi = self.getABI(self.address)

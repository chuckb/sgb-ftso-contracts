from web3 import Web3
import requests
import json

class FactoryBase:
  """
  This is a class common to all contract factory operations.
    
  Attributes:
      self.apiurl (string): Location of Blockscout api endpoint for Songbird. 
  """  

  def __init__(self, apiurl="https://songbird-explorer.flare.network/api"):
    """
    The constructor for FactoryBase class.

    Parameters:
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """    
    self.apiurl = apiurl
    self.address = None

  def getABI(self, address):
    """
    A method to fetch the application binary interface (ABI) for
    the contract at the specified address.

    Parameters:
        address (string): Contract address prefixed with 0x.
      
    Returns:
        string: The ABI of the contract.
    """    
    url = f"{self.apiurl}?module=contract&action=getabi&address={address}"
    response = requests.get(url)
    response_json = response.json()
    abi = json.loads(response_json['result'])
    return abi

  def contract(self, web3: Web3):
    """
    A method to instantiate a Web3 Contract set at self.address.

    Parameters:
        web3 (Web3): An instance of the Web3 class, wired up to a valid provider.
      
    Returns:
        Contract: An instantied contract at self.address.
    """
    if self.address is None:
      raise "self.address was not set"
    else:
      return web3.eth.contract(address=self.address, abi=self.abi)

class FtsoManager(FactoryBase):
  """
  A factory to instantiate the `FtsoManager <https://songbird-explorer.flare.network/address/0xbfA12e4E1411B62EdA8B035d71735667422A6A9e/contracts>`_ contract.
  This contract manages FTSO voting operations and coordinates price and reward epoch execution.

  Attributes:
      self.address (string): The address of the contract starting with 0x. 
  """  
  def __init__(self, address="0xbfA12e4E1411B62EdA8B035d71735667422A6A9e", apiurl=None):
    """
    The constructor for FtsoManager class.

    Parameters:
        address (string): Address of the contract starting with 0x.
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """
    FactoryBase.__init__(self) if apiurl is None else FactoryBase.__init__(self, apiurl)
    self.address = address
    self.abi = self.getABI(self.address)

class FtsoRegistry(FactoryBase):
  """
  A factory to instantiate the `FtsoRegistry <https://songbird-explorer.flare.network/address/0x6D222fb4544ba230d4b90BA1BfC0A01A94E6cB23/contracts>`_ contract.
  This provides Centralized access to all FTSOs from one contract. 
  This contract is handy to get FTSO current price info from, as one does not need to go after the FTSO directly.

  Attributes:
      self.address (string): The address of the contract starting with 0x. 
  """  
  def __init__(self, address="0x6D222fb4544ba230d4b90BA1BfC0A01A94E6cB23", apiurl=None):
    """
    The constructor for FtsoRegistry class.

    Parameters:
        address (string): Address of the contract starting with 0x.
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """
    FactoryBase.__init__(self) if apiurl is None else FactoryBase.__init__(self, apiurl)
    self.address = address
    self.abi = self.getABI(self.address)

class Ftso(FactoryBase):
  """
  A factory to instantiate the `Ftso <https://songbird-explorer.flare.network/address/0x20Fecb7b1Ff69C62BBA5Bb6aCD5a9743D11E246F/contracts>`_ contract.
  Note that this link is the FTSO for BTC. FTSOs are all the same contract; one instance per asset.

  Attributes:
      self.symbol (string): The asset symbol of the FTSO.
  """  
  def __init__(self, symbol, apiurl=None):
    """
    The constructor for Ftso class.

    Parameters:
        symbol (string): The asset symbol of the FTSO.
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """
    FactoryBase.__init__(self) if apiurl is None else FactoryBase.__init__(self, apiurl)
    self.symbol = symbol

  def contract(self, web3: Web3):
    """
    A method to instantiate a Web3 Contract set at self.address.

    Parameters:
        web3 (Web3): An instance of the Web3 class, wired up to a valid provider.
      
    Returns:
        Contract: An instantied contract at self.address for the FTSO identified by self.symbol.
    """
    # Instantiate the ftso registry
    ftsoRegistryFactory = FtsoRegistry()
    ftsoRegistry = ftsoRegistryFactory.contract(web3)
    # Get the address by symbol from the registry
    ftsoAddress = ftsoRegistry.functions.getFtsoBySymbol(self.symbol).call()
    # Set the ABI
    self.abi = self.getABI(ftsoAddress)
    # Instantiate the FTSO contract
    ftsoContract = web3.eth.contract(address=ftsoAddress, abi=self.abi)
    return ftsoContract

class FtsoRewardManager(FactoryBase):
  """
  A factory to instantiate the `FtsoRewardManager <https://songbird-explorer.flare.network/address/0xc5738334b972745067fFa666040fdeADc66Cb925/contracts>`_ contract.
  Vote power delegators can use this contract to claim rewards and check reward status.

  Attributes:
      self.address (string): The address of the contract starting with 0x. 
  """  
  def __init__(self, address="0xc5738334b972745067fFa666040fdeADc66Cb925", apiurl=None):
    """
    The constructor for FtsoRewardManager class.

    Parameters:
        address (string): Address of the contract starting with 0x.
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """
    FactoryBase.__init__(self) if apiurl is None else FactoryBase.__init__(self, apiurl)
    self.address = address
    self.abi = self.getABI(self.address)

class WNAT(FactoryBase):
  """
  A factory to instantiate the `WNAT <https://songbird-explorer.flare.network/address/0x02f0826ef6aD107Cfc861152B32B52fD11BaB9ED/contracts>`_ contract.
  Holders of the native chain token (for the Songbird network, SGB) use this contract 
  to wrap their Songbird in order to delegate vote power to FTSOs. WNAT = wrapped native

  Attributes:
      self.address (string): The address of the contract starting with 0x. 
  """  
  def __init__(self, address="0x02f0826ef6aD107Cfc861152B32B52fD11BaB9ED", apiurl=None):
    """
    The constructor for WNAT class.

    Parameters:
        address (string): Address of the contract starting with 0x.
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """
    FactoryBase.__init__(self) if apiurl is None else FactoryBase.__init__(self, apiurl)
    self.address = address
    self.abi = self.getABI(self.address)

class PriceSubmitter(FactoryBase):
  """
  A factory to instantiate the `PriceSubmitter <https://songbird-explorer.flare.network/address/0x1000000000000000000000000000000000000003/contracts>`_ contract.
  Price providers use this contract to centrally submit and reveal prices to one or more of the FTSOs simultaneously.

  Attributes:
      self.address (string): The address of the contract starting with 0x. 
  """  
  def __init__(self, address="0x1000000000000000000000000000000000000003", apiurl=None):
    """
    The constructor for PriceSubmitter class.

    Parameters:
        address (string): Address of the contract starting with 0x.
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """
    FactoryBase.__init__(self) if apiurl is None else FactoryBase.__init__(self, apiurl)
    self.address = address
    self.abi = self.getABI(self.address)

class VoterWhitelister(FactoryBase):
  """
  A factory to instantiate the `VoterWhitelister <https://songbird-explorer.flare.network/address/0xa76906EfBA6dFAe155FfC4c0eb36cDF0A28ae24D/contracts>`_ contract.
  Price providers must be whitelisted in order to submit prices to the FTSOs. This contract is how they do it.

  Attributes:
      self.address (string): The address of the contract starting with 0x. 
  """  
  def __init__(self, address="0xa76906EfBA6dFAe155FfC4c0eb36cDF0A28ae24D", apiurl=None):
    """
    The constructor for VoterWhitelister class.

    Parameters:
        address (string): Address of the contract starting with 0x.
        apiurl (string): Location of Blockscout api endpoint for Songbird. Used for fetching ABI automatically.
    """
    FactoryBase.__init__(self) if apiurl is None else FactoryBase.__init__(self, apiurl)
    self.address = address
    self.abi = self.getABI(self.address)

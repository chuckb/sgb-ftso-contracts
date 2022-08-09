import unittest
from sgb_ftso_contracts import *
from web3 import Web3

rpcurl = "https://songbird-api.flare.network/ext/bc/C/rpc"

class FactoryTestCase(unittest.TestCase):
  """Sanity tests for Songbird FTSO contract factories"""

  def setUp(self):
    self.web3 = Web3(Web3.HTTPProvider(rpcurl))

  def test_ftsoManager_getRewardEpochDurationSeconds(self):
    """Test ftsoManager.rewardEpochDurationSeconds() returns 604800"""
    # Assemble
    ftsoManager = FtsoManager().contract(self.web3)
    # Act
    secs = ftsoManager.functions.rewardEpochDurationSeconds().call()
    # Assert
    self.assertEqual(secs, 604800)

  def test_wNAT_getDecimals(self):
    """Test wNAT.decimals() returns 18"""
    # Assemble
    wNAT = WNAT().contract(self.web3)
    # Act
    decimals = wNAT.functions.decimals().call()
    # Assert
    self.assertEqual(decimals, 18)

  def test_ftsoRegistry_getSupportedSymbols(self):
    """Test ftsoRegistry.getSupportedSymbols() returns SGB"""
    # Assemble
    ftsoRegistry = FtsoRegistry().contract(self.web3)
    # Act
    symbols = ftsoRegistry.functions.getSupportedSymbols().call()
    # Assert
    self.assertTrue("SGB" in symbols)

  def test_ftso_getSymbol(self):
    """Test ftso lookup and contract factory instantiation"""
    # Assemble
    xrpFtso = Ftso("XRP").contract(self.web3)
    # Act
    symbol = xrpFtso.functions.symbol().call()
    # Assert
    self.assertEqual(symbol, "XRP")

  def test_priceSubmitter_getFtsoManager(self):
    """Test priceSubmitter.getFtsoManager() returns the FtsoManager contract address"""
    # Assemble
    priceSubmitter = PriceSubmitter().contract(self.web3)
    ftsoManager = FtsoManager().contract(self.web3)
    # Act
    ftsoManagerAddress = priceSubmitter.functions.getFtsoManager().call()
    # Assert
    self.assertEqual(ftsoManagerAddress, ftsoManager.address)

  def test_voterWhitelister_getDefaultMaxVotersForFtso(self):
    """Test voterWhitelister.DefaultMaxVotersForFtso() returns 100"""
    # Assemble
    voterWhitelister = VoterWhitelister().contract(self.web3)
    # Act
    maxVoters = voterWhitelister.functions.defaultMaxVotersForFtso().call()
    # Assert
    self.assertEqual(maxVoters, 100)

if __name__ == '__main__':
    unittest.main()
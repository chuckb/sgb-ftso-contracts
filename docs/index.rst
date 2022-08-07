.. SGB FTSO Contracts documentation master file, created by
   sphinx-quickstart on Sat Aug  6 13:11:35 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sgb-ftso-contracts
==================

.. image:: https://img.shields.io/pypi/v/sgb-ftso-contracts
   :target: https://pypi.org/project/sgb-ftso-contracts
   :alt: PyPI
.. image:: https://app.travis-ci.com/chuckb/sgb-ftso-contracts.svg?branch=master&status=passed
   :target: https://app.travis-ci.com/github/chuckb/sgb-ftso-contracts
.. image:: https://img.shields.io/github/v/tag/chuckb/sgb-ftso-contracts
   :target: https://www.github.com/chuckb/sgb-ftso-contracts

A small Python library to quickly instantiate `Flare Time Series Oracle (FTSO) contracts <https://gitlab.com/flarenetwork/flare-smart-contracts/-/tree/Songbird-deploy-with-contract-addresses>`_ on the Songbird network.

Installation
------------

.. code-block:: bash

  pip install sgb-ftso-contracts

Get Started
-----------
How to get prices of crypto assets tracked by the Songbird network:

.. code-block:: python

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


.. toctree::
   :maxdepth: 2
   :caption: Usage

   api

.. toctree::
   :maxdepth: 2
   :caption: Examples

   source/examples/delegation
   source/examples/encryption
   source/examples/events

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

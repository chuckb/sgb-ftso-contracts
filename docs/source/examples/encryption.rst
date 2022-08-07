==========
Encryption
==========

Encrypt Private Key
-------------------
To use the included examples that execute transactions on the Songbird blockchain, you will need access to your private key 
(or a wallet and an API). Hardware or software wallets are out of scope for these examples.
Private keys should never be stored in the clear, so this utility provides a means to encrypt your key with a password.

.. code-block:: python

  from eth_account import Account
  from getopt import getopt, GetoptError
  from pprint import pprint
  import json
  import sys
  import getpass

  def main(argv):
    '''Encrypt a wallet private key using a passphrase and store in a
    local directory.

    The encrypted key file is defined with the -o switch on the command line.
    '''
    outputfile = ''

    # Get command line args  
    try:
      opts, args = getopt(argv, "ho:", ["outputfile="])
    except GetoptError:
      printinvoke()
      exit(2)

    # Private key and password could be passed on command line for automation
    # purposes, but is not secure since command history can be stored.
    for opt, arg in opts:
      if opt == "-h":
        printinvoke()
        exit()
      elif opt in ("-o", "--outputfile"):
        outputfile = arg

    # Get private key and password...do not echo to terminal.
    key = getpass.getpass("Private key: ")
    password = getpass.getpass()

    # Encrypt...
    encrypted = Account.encrypt(key, password)
    pprint(encrypted)

    # Write encrypted key to output file defined on command line.
    with open(outputfile, 'w') as f: 
      f.write(json.dumps(encrypted))  

  def printinvoke():
    print("usage:")
    print("  encryptkey.py -o <outputfile>")

  if __name__ == "__main__":
    main(sys.argv[1:])
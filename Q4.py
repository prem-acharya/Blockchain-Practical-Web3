# 4)Write a python script to generate 2 wallet (address & private key).

from web3 import Web3
from eth_account import Account

eth = "https://mainnet.infura.io/v3/cdebf3b29acc4544a64b7be348b0b84a" 
web3 = Web3(Web3.HTTPProvider(eth))

accountA = Account.create()
accountB = Account.create()
account_A_wallet = accountA.address
account_A_key = web3.to_hex(accountA.key)

account_B_wallet = accountB.address
account_B_key = web3.to_hex(accountB.key)
print("Prem Acahrya D30\n")
print("wallet 1")
print("Account A Address: ",account_A_wallet)
print("Account A Private Key: ",account_A_key)
print("\nwallet 2")
print("Account B Address: ",account_B_wallet)
print("Account B Private Key: ",account_B_key)
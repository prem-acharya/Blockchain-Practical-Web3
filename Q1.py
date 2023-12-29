# 1) Write a python script to check balance of specified wallet using web3.py module. Take any wallet from etherscan.io

from web3 import Web3

eth ="https://mainnet.infura.io/v3/cdebf3b29acc4544a64b7be348b0b84a"

web3 = Web3(Web3.HTTPProvider(eth))
print("Prem Acharya D30")
print(web3.is_connected())

balance = web3.eth.get_balance('0x2bdBf6057610FBd173cA364EAD647941c4285Cf8')
balance1 = web3.eth.get_balance('0xd6b4149993542C2f80164100300e7948b9A24EE8')
print("balance 1:",balance / 10**18)
print("balance 2:",balance1 / 10**18)



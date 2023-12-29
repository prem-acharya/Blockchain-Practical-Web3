from web3 import Web3

eth = "https://mainnet.infura.io/v3/cdebf3b29acc4544a64b7be348b0b84a"

web3 = Web3(Web3.HTTPProvider(eth))

print(web3.is_connected())

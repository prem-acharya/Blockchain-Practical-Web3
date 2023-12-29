# Write a python script to get latest block which is being generated right now for ethereum blockchain.

from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/cdebf3b29acc4544a64b7be348b0b84a'

web3 = Web3(Web3.HTTPProvider(infura_url))
print ('Prem Acharya D30')

def get_latest_block():
    try:
        latest_block_number = web3.eth.block_number

        latest_block = web3.eth.get_block(latest_block_number)

        return latest_block
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def main():
    latest_block = get_latest_block()
    if latest_block:
        print("Latest Block Details:")
        print(f"Block Number: {latest_block['number']}")
        print(f"Timestamp: {latest_block['timestamp']}")
        print(f"Hash: {latest_block['hash']}")
        print(f"Parent Hash: {latest_block['parentHash']}")
if __name__=="__main__":
    main()
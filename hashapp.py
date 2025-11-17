# app.py
from web3 import Web3
import sys
import time
import json

def get_l1_header_hash(rpc, block_number):
    w3 = Web3(Web3.HTTPProvider(rpc))
    if not w3.is_connected():
        print("RPC connection failed")
        sys.exit(1)

    block = w3.eth.get_block(block_number)
    header_data = {
        "parentHash": block.parentHash.hex(),
        "stateRoot": block.stateRoot.hex(),
        "transactionsRoot": block.transactionsRoot.hex(),
        "receiptsRoot": block.receiptsRoot.hex()
    }

    encoded = json.dumps(header_data, sort_keys=True).encode()
    header_hash = Web3.keccak(encoded).hex()
    return block.number, header_hash

if __name__ == "__main__":
    RPC = "https://mainnet.infura.io/v3/your_api_key"

    print("Fetching L1 header hash for ZK soundness systems (Aztec/Zama/etc.)...")
    time.sleep(0.2)

    block_number = "latest"
    if len(sys.argv) > 1:
        block_number = int(sys.argv[1])

    num, h = get_l1_header_hash(RPC, block_number)

    print("Block:", num)
    print("Header hash:", h)
    print("Done.")

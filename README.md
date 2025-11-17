# README.md
# L1 Header Hash Generator

## Overview
This repository provides a script that generates a deterministic hash of essential Ethereum L1 block header fields. This hash can be used in ZK systems, soundness verification pipelines, L2 rollups, and frameworks such as Aztec, Zama, and other cryptographic infrastructures.

## Installation
Install Python 3.10 or newer.
Install dependencies:
pip install web3
Insert your own RPC endpoint into the script.

## Usage
Run the script:
python3 app.py
Or specify a block number:
python3 app.py 18000000

## Expected Output
The script prints the block number and a deterministic hash of key header fields including parentHash, stateRoot, transactionsRoot, and receiptsRoot. This hash is suitable for use as a public input to ZK circuits or for soundness verification of L1 data.

## Notes
Works with any EVM-compatible RPC endpoint.  
For ZK systems requiring deterministic proofs, use a stable RPC provider.  
Designed to support integrations with Aztec, Zama, soundness validators, and other cryptographic verification environments.
# L1-Header-Hash-Generator

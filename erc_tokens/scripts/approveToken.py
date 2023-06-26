from brownie import accounts, Token1, Token2, WETH
import json
import os



def approve():
    # t1 = brownie.Contract.from_abi(
    t1_path = "build/contracts/Token1.json"
    with open(t1_path,'r') as f:
        abi = json.load(f)['abi']
    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)
    print(parent_dir)



def main():
    approve()
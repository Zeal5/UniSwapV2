from brownie import accounts, config, Token1, Token2, WETH
import json

def deploye_factory():
    account = accounts[0]
    t1 = Token1.deploy({"from": account} )
    t2 = Token2.deploy({"from": account} )
    weth = WETH.deploy({"from": account} )


    #save data to a file
    data = {
        't1_address' : t1.address,
        't2_address' : t2.address,
        'weth_address': weth.address,
        'from': account.address,
    }

    with open('../token_data.json', 'w') as td:
        json.dump(data,fp=td,indent=4)

    

def main():
    deploye_factory()


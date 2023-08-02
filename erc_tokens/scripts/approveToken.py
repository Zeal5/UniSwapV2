from brownie import accounts, Token1, Token2, WETH
import json


def approve():

    with open('../token_data.json', 'r') as f:
        a = json.load(f)
        t1_address = a['t1_address']
        t2_address = a['t2_address']
        weth_address= a['weth_address']

    token1 = Token1.at(t1_address)
    token2 = Token2.at(t2_address)
    weth   = WETH.at(weth_address)

    # Get weth for eth in account
    weth.deposit({"value": 5 * (10**18),'from':accounts[0]})



        
    # approve factory
    with open('../router_data.json','r') as fd:
        factory_data = json.load(fd)
        router_address = factory_data['router_address']


    token1.approve( router_address,100000000,{'from':accounts[0]})
    token2.approve(router_address ,100000000,{'from':accounts[0]})
    weth.approve(router_address ,5,{'from':accounts[0]})




def main():
    approve()
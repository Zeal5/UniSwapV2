from brownie import accounts, Token1, Token2, WETH
import json
import os



def approve():
    #approve router as spender here  //TODO get router address to approve
    # t1.approve()

    # t1 = brownie.Contract.from_abi(
    # t1_path = "build/contracts/Token1.json"
    # with open(t1_path,'r') as f:
    #     abi = json.load(f)['abi']
    # print(abi)
    # cwd = os.getcwd()
    # parent_dir = os.path.dirname(cwd)
    # print(parent_dir)

    with open('../token_data.json', 'r') as f:
        a = json.load(f)
        t1_address = a['t1_address']
        t2_address = a['t2_address']
        weth_address= a['weth_address']

    token1 = Token1.at(t1_address)
    token2 = Token2.at(t2_address)
    weth   = WETH.at(weth_address)
    # approve factory
    with open('../factory_data.json','r') as fd:
        factory_data = json.load(fd)
        factory_address = factory_data['factory_address']


    token1.approve(factory_address,100000000,{'from':accounts[0]})
    token2.approve(factory_address,100000000,{'from':accounts[0]})
    weth.approve(factory_address,5,{'from':accounts[0]})




def main():
    approve()
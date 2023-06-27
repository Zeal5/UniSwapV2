from brownie import accounts, UniswapV2Router02
import json


def deploye_factory():
    with open('../factory_data.json','r') as fd:
        factory_data_dict = json.load(fd)
    
    with open('../token_data.json','r') as td:
        token_data = json.load(td)
        weth_address = token_data['weth_address']
        

    _factory_address = factory_data_dict['factory_address']
    _WETH_address = weth_address
    account = accounts[0]


    #router = UniswapV2Router02.deploy(_factory_address, _WETH_address, {"from": account} )

    data = {
        # 'router_address' : router.address,
        'weth_address':_WETH_address,
        'message.sender':account,
        'factory_address':_factory_address
    }

    with open('router_data.json','w') as rd:
        json.dump(data,fp=rd,indent=4)
def main():
    deploye_factory()

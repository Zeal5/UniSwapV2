from brownie import accounts, UniswapV2Router02
import json


def deploye_factory():
    with open('../factory_data.json','r') as fd:
        factory_data_dict = json.load(fd)
        

    _factory_address = factory_data_dict['factory_address']

    _WETH_address = "0x06F27e7506D50018a1f35D732D94cdF7D5959205"
    account = accounts[0]


    # router = UniswapV2Router02.deploy(_factory_address, _WETH_address, {"from": account} )

    # data = {
    #     'router_address' : router.address,
    # }

    
def main():
    deploye_factory()

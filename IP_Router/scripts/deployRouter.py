from brownie import accounts, UniswapV2Router02
import json
import os 

def deploye_factory():
  
    with open('../factory_data.json','r') as fd:
        factory_data_dict = json.load(fd)

    with open('../token_data.json','r') as td:
        token_data = json.load(td)
        weth_address = token_data['weth_address']
 

    _factory_address = factory_data_dict['factory_address']
    _WETH_address = weth_address
    account = accounts[0]
    _init_code_hash = factory_data_dict['init_code_hash']
    # remove 0x form init code hash
    _init_code_hash = _init_code_hash[2:]

    # change init code hash 
    new_lib = []
    with open('../IP_Router/contracts/libraries/UniswapV2Library.sol','r') as lib:
        lines = lib.readlines()
        
        for line in lines:
            if line.strip().startswith('hex') and len(line.strip()) > 10 :
                code_hash_line = f"\t\thex'{_init_code_hash}'  // init code hash\n"
                new_lib.append(code_hash_line)
            else:
                new_lib.append(line)

        #remove old libraryV2
        os.remove('../IP_Router/contracts/libraries/UniswapV2Library.sol')

        # rewrite the libraryV2.sol with new hash
        with open('../IP_Router/contracts/libraries/UniswapV2Library.sol','w') as lib:
            for line in new_lib:
                lib.write(line)

    router = UniswapV2Router02.deploy(_factory_address, _WETH_address, {"from": account} )

    data = {
        'router_address' : router.address,
        'weth_address':_WETH_address,
        'message.sender':str(account),
        'factory_address':_factory_address
    }

    with open('../router_data.json','w') as rd:
        json.dump(data,fp=rd,indent=4)

def main():
    deploye_factory()

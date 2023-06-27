from brownie import accounts, config, UniswapV2Factory
import json

def deploye_factory():
    private_key = config["wallets"]["from_key"]
    # owner_account = accounts.add(private_key)
    owner_account = accounts[0]
    account = accounts[0]
    factory = UniswapV2Factory.deploy(owner_account, {"from": account} )
    init_hash = factory.INIT_CODE_HASH()

    data = {
        'init_code_hash' : str(init_hash),
        'factory_address': factory.address,
        'from': account.address,
        'owner_account': owner_account.address,
    }
   
    with open('../factory_data.json', 'w') as f:
        json.dump(data,fp=f,indent=4)



def main():
    deploye_factory()

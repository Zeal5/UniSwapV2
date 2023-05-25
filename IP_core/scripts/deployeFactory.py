from brownie import accounts, config, UniswapV2Factory


def deploye_factory():
    private_key = config["wallets"]["from_key"]
    owner_account = accounts.add(private_key)
    account = accounts[0]
    factory = UniswapV2Factory.deploy(owner_account, {"from": account} )
    init_hash = factory.INIT_CODE_HASH()
    print(f"init_hash {init_hash}")
    with open('../factory_data.txt', 'a') as f:
        f.write(f"_factory_address {factory}\n")
        f.write(f"init_hash {init_hash}\n")
        f.write(f"owner_account {owner_account}\n")

    

    


    # Deploye a contract
    # Import a user wallet
    # private_key = config["wallets"]["from_key"]
    # account = accounts.add(private_key)


def main():
    deploye_factory()

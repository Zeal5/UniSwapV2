from brownie import accounts, config, UniswapV2Factory


def deploye_factory():
    private_key = config["wallets"]["from_key"]
    owner_account = accounts.add(private_key)
    account = accounts[0]
    factory = UniswapV2Factory.deploy(owner_account, {"from": account} )
    init_hash = factory.

    # Deploye a contract
    # Import a user wallet
    # private_key = config["wallets"]["from_key"]
    # account = accounts.add(private_key)


def main():
    deploye_factory()

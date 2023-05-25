from brownie import accounts, config, UniswapV2Factory


def test_deploy():
    private_key = config["wallets"]["from_key"]
    owner_account = accounts.add(private_key)
    account = accounts[0]
    factory = UniswapV2Factory.deploy(owner_account, {"from": account})
    setter = factory.feeToSetter()
    assert setter == owner_account


def test_init_pair():
    private_key = config["wallets"]["from_key"]
    owner_account = accounts.add(private_key)
    account = accounts[0]
    factory = UniswapV2Factory.deploy(owner_account, {"from": account})
    pairs_legth = factory.allPairsLength()
    assert pairs_legth == 0

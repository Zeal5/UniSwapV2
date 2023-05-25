from brownie import accounts, UniswapV2Router02


def deploye_factory():
    _factory_address = "0x78cbCBFaA65A65eA9E0a8933066642aDa21D8Efa"
    _WETH_address = "0x24E9cdDe6bfFa667d204a41E1B5f1813f0a2E700"
    account = accounts[0]
    factory = UniswapV2Router02.deploy(_factory_address, _WETH_address, {"from": account} )


def main():
    deploye_factory()

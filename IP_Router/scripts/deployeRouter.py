from brownie import accounts, UniswapV2Router02


def deploye_factory():
    _factory_address = "0x38EB1321ce58640d9Ac0f3F42326B255d1C859b9"
    _WETH_address = "0x06F27e7506D50018a1f35D732D94cdF7D5959205"
    account = accounts[0]
    router = UniswapV2Router02.deploy(_factory_address, _WETH_address, {"from": account} )
    


def main():
    deploye_factory()

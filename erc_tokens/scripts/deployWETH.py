from brownie import accounts, config, WETH


def deploye_factory():
    account = accounts[0]
    factory = WETH.deploy({"from": account} )


def main():
    deploye_factory()


from brownie import accounts, config, Token1, Token2


def deploye_factory():
    account = accounts[0]
    factory = Token1.deploy({"from": account} )
    factory = Token2.deploy({"from": account} )

    

def main():
    deploye_factory()


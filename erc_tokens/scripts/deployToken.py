from brownie import accounts, config, Token1, Token2, WETH


def deploye_factory():
    account = accounts[0]
    t1 = Token1.deploy({"from": account} )
    t2 = Token2.deploy({"from": account} )
    weth = WETH.deploy({"from": account} )

    with open('../token_data.txt', 'a') as f:
        f.write(f"t1 {t1} \nt2 {t2}\n")
        f.write(f"weth {weth}\n")

    

def main():
    deploye_factory()


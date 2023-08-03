# curl command to interact with ganache-cli
curlCommand() {
    curl -s -X POST --data '{"jsonrpc":"2.0","method":"net_version","params":[],"id":1}' http://localhost:8545 -w "%{http_code}\n" | tail -1
}

# Start Ganache in seperate GNOME Terminal
gnome-terminal -- bash -c "ganache-cli; bash -i" & 

while true; do
    response=$(curlCommand)
    if [[ "$response" != "000" ]]; then
        break
    fi
    sleep 2
done

echo "ganache started"

# Deploy Factory
echo "Deploying factory" 
cd ./IP_core
brownie run scripts/deployFactory.py


# Deploy ERC20 Tokens
echo "Deploying WETH and other tokens"
cd ../erc_tokens 
brownie run scripts/deployToken.py


# Deploying Router contracts
echo "Deploying Router contracts"
cd ../IP_Router
brownie run scripts/deployRouter.py


echo "approving tokens"
cd ../erc_tokens
brownie run scripts/approveToken.py
echo "done"

echo "creating Uniswap pairs"
cd ../IP_Router
# load all variables before opening brownie console
factory_address=$(jq -r '.factory_address' ../factory_data.json)
router_address=$(jq -r '.router_address' ../router_data.json)
t1_address=$(jq -r '.t1_address' ../token_data.json)
t2_address=$(jq -r '.t2_address' ../token_data.json)
echo "router address: $router_address"
echo "t1 address: $t1_address"
echo "t2 address: $t2_address"


router_commands="brownie_commands.exp $router_address $t1_address $t2_address"
factory_commands="../IP_core/brownie_commands.exp $factory_address $t1_address $t2_address"

gnome-terminal --working-directory="/home/zeal/UniswapFork/IP_Router" -- bash -c "expect $router_commands; exec bash" &
gnome-terminal --working-directory="/home/zeal/UniswapFork/IP_core" -- bash -c "expect $factory_commands; exec bash"


# expect brownie_commands.exp $router_address $t1_address $t2_address






# brownie console
# echo "
# router = Contract.from_abi('router', '$router_address', UniswapV2Router02.abi, owner=accounts[0])
# t1 = Contract.from_abi('t1', '$t1_address', ERC20.abi, owner=accounts[0])
# " | brownie console



# router = Contract.from_abi("router",router_address,UniswapV2Router02.abi,owner=accounts[0])
# t1 = Contract.from_abi("t1",t1_address,ERC20.abi,owner=accounts[0])
# t2 = Contract.from_abi("t2",t2_address,ERC20.abi,owner=accounts[0])
# echo "checking allowance for t1 / router"
# t1.allowance(accounts[0],router.address)
# echo "checking allowance for t2 / router"
# t2.allowance(accounts[0],router.address)

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
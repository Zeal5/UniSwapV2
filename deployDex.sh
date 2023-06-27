# Start Ganache in seperate GNOME Terminal
gnome-terminal -- bash -c "ganache-cli; bash -i" & 
sleep 7


# Deploy Factory
echo "Deploying factory" 
cd ./IP_core
brownie run scripts/deployFactory.py


# Deploy ERC20 Tokens
cd ../erc_tokens 
brownie run scripts/deployToken.py
brownie run scripts/approveToken.py

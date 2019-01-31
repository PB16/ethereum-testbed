#finds the account address of the miner given as input argument with the accounts.sh script.
sudo docker exec -it composer_$1_1 /bin/bash -c "accounts.sh $1"

#sets the account address in the truffle.js file.
sudo docker exec -it composer_$1_1 /bin/bash -c "python3 setAccount.py"

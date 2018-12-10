#starts the docker containers in the docker compose file.
sudo docker-compose up -d
sleep 10

#finds the account address of miner1 with the accounts.sh script.
sudo docker exec -it composer_miner1_1 /bin/bash -c "accounts.sh"

#sets the account address in the truffle.js file.
sudo docker exec -it composer_miner1_1 /bin/bash -c "python3 setAccount.py"

#unlocks the account of miner1 and starts mining.
sudo docker exec -it -d composer_miner1_1 /bin/bash -c "geth --datadir workspace/miner1 --networkid 1234 --verbosity 6 --unlock 0 --password password.txt --mine --minerthreads 1 --rpc --rpcapi \"admin, eth, personal, miner, txpool, net, web3\" 2>> workspace/miner1.txt"

#check all conditions for migration of smart contracts is met.
sudo python3 ../../truffle/automatic-migration.py

#Deploying smart contracts and pipe the output to a txt file.
sudo docker exec -it composer_miner1_1 /bin/bash -c "cd truffle/ && truffle migrate > migrations.txt"

#Copying file with contract addresses from docker container to host.
sudo docker cp composer_miner1_1:/truffle/migrations.txt /home/peter/ethereum-testbed/testbed/truffle/

#replacing the ABI in the test scripts.
sudo python3 ../../truffle/setContractAddress.py

#Load javascript files with tests.
sudo python3 ../../truffle/load-test-scripts.py

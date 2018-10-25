sudo docker-compose up -d
sleep 1.5
sudo docker exec -it composer_miner1_1 /bin/bash -c "accounts.sh"
sudo docker exec -it composer_miner1_1 /bin/bash -c "python3 setAccount.py"
sudo docker exec -it composer_miner1_1 /bin/bash -c "geth --datadir miner1 --networkid 1234 --verbosity 6 --unlock \"0xecd8660056afe7a3f0a6b59f90777171b72f4c14\" --password password.txt --mine --minerthreads 1 --rpc --rpcapi \"admin, eth, personal, miner, txpool, net, web3\" 2>> miner1.txt"

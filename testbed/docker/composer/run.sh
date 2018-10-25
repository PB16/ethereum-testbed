sudo docker-compose up -d
sleep 10
sudo docker exec -it composer_miner1_1 /bin/bash -c "accounts.sh"
sudo docker exec -it composer_miner1_1 /bin/bash -c "python3 setAccount.py"
sudo docker exec -it -d composer_miner1_1 /bin/bash -c "geth --datadir workspace/miner1 --networkid 1234 --verbosity 6 --unlock 0 --password password.txt --mine --minerthreads 1 --rpc --rpcapi \"admin, eth, personal, miner, txpool, net, web3\" 2>> workspace/miner1.txt"

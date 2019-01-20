sudo docker exec -it composer_$1_1 /bin/bash -c "accounts.sh $1"

sleep 2

sudo docker exec -it composer_$1_1 /bin/bash -c "python3 setAccount.py"

sleep 2

#sudo docker exec -it -d composer_$1_1 /bin/bash -c "geth --datadir workspace/$1 --networkid 1234 --verbosity 6 --unlock 0 --password password.txt --mine --minerthreads 1 --rpc --rpcapi \"admin, eth, personal, miner, txpool, net, web3\" 2>> workspace/$1.txt"

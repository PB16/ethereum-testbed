#!/bin/bash
cd ../workspace
tc qdisc add dev eth0 root netem delay ${NET_DELAY} 20ms distribution normal
geth --datadir miner1 --networkid 1234 init genesisTesting.json 2>> miner1.txt
geth --datadir miner1 --networkid 1234 --exec 'personal.newAccount("\"1234"\")' console 2>> miner1.txt 
geth --datadir miner1 --networkid 1234 --verbosity 6 --exec 'personal.unlockAccount(eth.accounts[0], "\"1234"\", 10000)' --bootnodes "enode://8a080f000641843af0e117381feb090677ef7d674448e6d3b94f7d3fda46f3c52a727ab9113a9c5c7bf6cb09addc3e3ffbe4f8d4b55ee174d3bd683746e0d638@[172.19.0.200]:30301" --mine --minerthreads 1 --rpc --rpcapi \"admin, eth, personal, miner, txpool, net, web3\" 2>> miner1.txt
./accounts.sh
bin/bash
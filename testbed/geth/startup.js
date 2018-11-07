personal.newAccount("1234");
miner.setEtherbase(eth.accounts[0]);
personal.unlockAccount(eth.accounts[0], "1234", 10000);
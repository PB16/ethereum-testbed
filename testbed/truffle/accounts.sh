#extracts account addresses from the keystore of miner1 and places it in a file.
geth account list --keystore workspace/$1/keystore/ > accountKeys.txt
import pexpect
from time import sleep
import os

#Spawn geth instance of miner1.
geth = pexpect.spawn("geth attach ipc:filecontainer/miner1/geth.ipc")
i = 0

while True:
    geth.expect(">")

    #Request the balance of miner1.
    geth.send("eth.getBalance(eth.coinbase)\r")
    
    #Actually get the balance of miner1.
    geth.expect("m(.*)\\x1b")

    sleep(1)
    
    #Extract the balance and convert it to a string.
    result = str(geth.after.decode())
    result = result.replace("m","")
    result = result.replace("\x1b","")

    print(result + " [" + str(i) + "]")
    i = i + 1
    
    #check if the account has enough ressources to deploy the smart contracts.
    if result.isdigit() and int(result) >= 100000000000000:
        print("migrating smart contracts!")
        sleep(2)
        quit()

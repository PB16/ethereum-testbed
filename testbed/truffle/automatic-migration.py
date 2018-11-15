import pexpect
from time import sleep
import os

print(os.getcwd())
geth = pexpect.spawn("geth attach ipc:filecontainer/miner1/geth.ipc")

while True:
    geth.expect(">")

    geth.send("eth.getBalance(eth.coinbase)\r")
    
    geth.expect("m(.*)\\x1b")

    sleep(1)

    result = str(geth.after.decode())
    result = result.replace("m","")
    result = result.replace("\x1b","")

    print(result)

    if result.isdigit() and int(result) >= 10000000000000000:
        print("migrating smart contracts!")
        sleep(2)
        quit()

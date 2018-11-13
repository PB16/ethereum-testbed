import pexpect
from time import sleep

geth = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/miner1/geth.ipc")

while True:
    geth.expect(">")

    geth.send("eth.getBalance(eth.coinbase)\r")
    
    geth.expect("m(.*)\\x1b")

    sleep(1)

    result = str(geth.after.decode())
    result = result.replace("m","")
    result = result.replace("\x1b","")

    print(result)

    if result.isdigit() and int(result) >= 1000000000000000000:
        print("migrating smart contracts!")
        sleep(2)
        quit()

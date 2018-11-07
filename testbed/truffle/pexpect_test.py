import pexpect

geth = pexpect.spawn("geth attach ipc:/home/peter/geth_test/miner/geth.ipc")

while True:
    geth.expect(">")
    
    geth.send("eth.getBalance(eth.coinbase)\r")
    
    geth.expect("[0-9]+[0-9]+[0-9]+")
    
    result = geth.after.decode("utf-8")
    print(result)
    if int(result) >= 100000000000000000000:
        quit()
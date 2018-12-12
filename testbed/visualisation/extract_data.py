import pexpect
import re

geth = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/miner1/geth.ipc")

geth.expect(">")

geth.send("eth.getBlock(eth.blockNumber)\r")

geth.expect("{(.*)}")

data = geth.after.decode()
print(data)

result = re.search('number: (.*),', data)

print(result.group(1))
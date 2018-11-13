import pexpect
from time import sleep

geth = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/miner1/geth.ipc")

geth.expect(">")

geth.send("loadScript(\"/home/peter/ethereum-testbed/testbed/geth/scripts/createTransactions.js\")")

geth.expect(">")

geth.send("test()")

geth.expect("(.*)")
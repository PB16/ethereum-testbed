import sys
import pexpect
from time import sleep

miner = sys.argv[1]

#Spawn geth instance to run the tests in.
geth = pexpect.spawn("geth attach ipc:filecontainer/" + miner + "/geth.ipc")

geth.expect(">")

#Load a test file to use.
#geth.send("loadScript(\"../../geth/scripts/createTransactions.js\")\r")

geth.send("loadScript(\"../../geth/scripts/tester.js\")\r")

geth.expect("true")

#Call the testcases.
#geth.send("createTransactions(1000)\r")
geth.send("tester()\r")

#Extract the test results.
geth.expect("start(.*)end")
result = geth.after.decode()
result = result.replace("start","")
result = result.replace("end","")
geth.expect("undefined")

#Saving the test results in a file. 
with open(miner + "_results.txt","w") as tfile:
	tfile.writelines(result)

#print(result)
print("done")
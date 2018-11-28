import pexpect
from time import sleep

#Spawn geth instance to run the tests in.
geth = pexpect.spawn("geth attach ipc:filecontainer/miner1/geth.ipc")

geth.expect(">")

#Load a test file to use.
geth.send("loadScript(\"../../geth/scripts/createTransactions.js\")\r")

geth.expect("true")

#Call the testcases.
geth.send("createTransactions(1000)\r")

geth.expect("undefined")
#Extract the test results.
#geth.expect("start(.*)end")
#result = geth.after.decode()
#result = result.replace("start","")
#result = result.replace("end","")

#Saving the test results in a file. 
#with open("results.txt","w") as tfile:
#	tfile.writelines(result)

#print(result)
print("done")
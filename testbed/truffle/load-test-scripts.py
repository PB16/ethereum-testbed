import pexpect
from time import sleep

#Spawn geth instance to run the tests in.
geth = pexpect.spawn("geth attach ipc:../docker/composer/filecontainer/miner1/geth.ipc")

geth.expect(">")

#Load a test file to use.
geth.send("loadScript(\"../geth/scripts/tester.js\")\r")

geth.expect("true")

#Call the testcases.
geth.send("tester()\r")

#Extract the test results.
geth.expect("start(.*)end")
result = geth.after.decode()
result = result.replace("start","")
result = result.replace("end","")

#Saving the test results in a file. 
with open("results.txt","w") as tfile:
	tfile.writelines(result)

#print(result)

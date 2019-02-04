import subprocess
import os
from time import sleep

miners = []
minerspath = os.getcwd() + "/filecontainer/"

#Command for starting the docker containers.
dockerStartCmd = "sudo docker-compose up -d"

#Start the docker containers.
subprocess.call(dockerStartCmd.split())

sleep(5)

#Find the name of miners and add it to a list containing all miners.
for x in next(os.walk(minerspath))[1]:
    if "miner" in x:
        miners.append(x)

sleep(5)

#Find the account for all miners and save the address for later use.
for x in miners:
    subprocess.call(['sudo','./accounts.sh',x])

sleep(5)

#Check that all miners have enough resources to deploy the contracts.
for x in miners:
    subprocess.call(['sudo','python3','../../truffle/automatic-migration.py',x])

sleep(5)

#Deploy the contracts on all miner accounts.
for x in miners:
    subprocess.call(['sudo','./migration.sh',x])

sleep(5)

#Change the contract address in the test scripts to the correct contract address.
for x in miners:
    subprocess.call(['sudo','python3','../../truffle/setContractAddress.py',x])

sleep(5)

#Execute tests on all miners.
for x in miners:
    subprocess.call(['sudo','python3','../../truffle/load-test-scripts.py',x])

sleep(5)

print("testbed has succesfully started!")

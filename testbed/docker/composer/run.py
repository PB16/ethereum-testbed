import subprocess
import os
from time import sleep

miners = []
minerspath = os.getcwd() + "/filecontainer/"

dockerStartCmd = "sudo docker-compose up -d"

subprocess.call(dockerStartCmd.split())

sleep(5)

for x in next(os.walk(minerspath))[1]:
    if "miner" in x:
        miners.append(x)

sleep(5)

for x in miners:
    subprocess.call(['sudo','./accounts.sh',x])

sleep(5)

for x in miners:
    subprocess.call(['sudo','python3','../../truffle/automatic-migration.py',x])

sleep(5)

for x in miners:
    subprocess.call(['sudo','./migration.sh',x])

sleep(5)

for x in miners:
    subprocess.call(['sudo','python3','../../truffle/setContractAddress.py',x])

sleep(5)

for x in miners:
    subprocess.call(['sudo','python3','../../truffle/load-test-scripts.py',x])

sleep(5)

print("testbed has succesfully started!")
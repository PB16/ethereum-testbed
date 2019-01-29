import subprocess
import os
from time import sleep

miners = []
minerspath = os.getcwd() + "/filecontainer/"

dockerStartCmd = "sudo docker-compose up -d"

subprocess.call(dockerStartCmd.split())

for x in next(os.walk(minerspath))[1]:
    if "miner" in x:
        miners.append(x)

print(miners)
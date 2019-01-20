import os
import subprocess
from time import sleep

miners = []

dockerComposeUp = "sudo docker-compose up -d"

subprocess.call(dockerComposeUp.split())

sleep(5)

for x in os.scandir((os.getcwd()+"/filecontainer/")):
    if x.is_dir() and "miner" in x.path:
        args = x.path.split("/")
        miners.append(args[(len(args)-1)])

for x in miners:
    subprocess.run(["sudo", "./accounts.sh", x])

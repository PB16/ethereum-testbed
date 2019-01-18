import os
import subprocess

miners = []

dockerComposeUp = "sudo docker-compose up -d"

subprocess.call(dockerComposeUp.split())

for x in os.scandir((os.getcwd()+"/filecontainer/")):
    if x.is_dir() and "miner" in x.path:
        args = x.path.split("/")
        miners.append(args[(len(args)-1)])

for x in miners:
    subprocess.call(("sudo docker exec -it composer_" + x + "_1 bash -c accounts.sh " + x).split())

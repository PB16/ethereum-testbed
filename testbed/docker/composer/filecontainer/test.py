import os

for x in os.scandir(os.getcwd()):
    if x.is_dir() and "miner" in x.path:
        print(x.path)
import os
import re
from subprocess import call

#gets the current working directory.
start = os.getcwd()
os.chdir("testbed/docker/composer")
cwd = os.getcwd()

cwd = cwd + "/filecontainer:/workspace"

#sets the working directory, so that docker compose works.
with open(".env", "r") as sfile:
  lines = sfile.readlines()
  result = re.search('VOLUME_PATH=(.*)\n', lines[1])
  lines[1] = lines[1].replace(result.group(1), cwd)

with open(".env", "w") as sfile:
  sfile.writelines(lines)

#runs the setup.sh script which install all neccessary software for the testbed to run.
os.chdir(start)
with open('setup.sh', 'rb') as file:
    script = file.read()
rc = call(script, shell=True)

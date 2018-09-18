import os
import re
from subprocess import call

cwd = os.getcwd()

cwd = cwd + "/filecontainer:/workspace"

with open(".env", "r") as sfile:
#for x in f:
  #if "VOLUME_PATH" in x:
  lines = sfile.readlines()
  result = re.search('VOLUME_PATH=(.*)\n', lines[1])
  lines[1] = lines[1].replace(result.group(1), cwd)

with open(".env", "w") as sfile:
  sfile.writelines(lines)

with open('setup.sh', 'rb') as file:
    script = file.read()
os.chdir("..")
rc = call(script, shell=True)
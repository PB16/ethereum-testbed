import os
import re
from subprocess import call

accountAddress = ""

with open("accountKeys.txt", "r") as sfile:
  lines = sfile.readlines()
  result = re.search('{(.*)}', lines[0])
  accountAddress = "0x" + result.group(1)

with open("truffle/truffle.js", "r") as tfile:
  lines = tfile.readlines()
  result = re.search('\"(.*)\"', lines[10])
  lines[10] = lines[10].replace(result.group(1), accountAddress)

with open("truffle/truffle.js", "w") as tfile:
  tfile.writelines(lines)

#with open("unlockaccount.sh", "r") as ufile:
#	lines = ufile.readlines()
#	lines[0] = lines[0].replace("account", accountAddress)
#	lines[0] = lines[0].replace("\"", "")
#
#with open("unlockaccount.sh", "w") as wfile:
#	wfile.writelines(lines)
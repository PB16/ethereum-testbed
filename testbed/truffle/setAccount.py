import os
import re
from subprocess import call

accountAddress = ""

#gets the accounts address of miner1.
with open("accountKeys.txt", "r") as sfile:
  lines = sfile.readlines()
  result = re.search('{(.*)}', lines[0])
  accountAddress = "0x" + result.group(1)

#sets the address in the "from:" attribute to the address of the miner1 account.
with open("truffle/truffle.js", "r") as tfile:
  lines = tfile.readlines()
  result = re.search('\"(.*)\"', lines[10])
  lines[10] = lines[10].replace(result.group(1), accountAddress)

#saves the changes to the truffle.js file.
with open("truffle/truffle.js", "w") as tfile:
  tfile.writelines(lines)
  
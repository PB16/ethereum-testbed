import re

with open("migrations.txt", "r") as sfile:
	for line in sfile:
		line = line.replace(" ","")

with open("/home/peter/ethereum-testbed/testbed/geth/scripts/createTransactions.js") as tfile:
	lines = tfile.readlines()

	for line in lines:
		if not line.lstrip().startswith("//") and "var contractAddress = \"" in line:
			result = re.search('var contractAddress = \"(.*)\";', line.lstrip())

#extracting the old ABI, so it can be replaced with the new ABI.
lines = ''.join(lines)
abi = re.search('eth.contract\((.*)\);', lines, re.DOTALL)

#extracting the new ABI, so the old one can be replaced.
with open("/home/peter/ethereum-testbed/testbed/truffle/build/contracts/Offer.json") as sfile:
	lines1 = sfile.read()

result = re.search('\"abi\":(.*),\n  \"bytecode\":', lines1, re.DOTALL)

#replacing old ABI with new ABI, so that it is possible to interact with contract in use.
with open("/home/peter/ethereum-testbed/testbed/geth/scripts/createTransactions.js") as tfile:
	lines = tfile.readlines()
	lines = ''.join(lines)
	lines = lines.replace(abi.group(1), result.group(1))

#saving the changes.
with open("/home/peter/ethereum-testbed/testbed/geth/scripts/createTransactions.js","w") as tfile:
	tfile.writelines(lines)
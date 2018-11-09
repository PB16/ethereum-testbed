import re

with open("migrations.txt", "r") as sfile:
	for line in sfile:
		line = line.replace(" ","")

		if "Offer:" in line:
			print(line.split(':')[1])

with open("/home/peter/ethereum-testbed/testbed/geth/scripts/createTransactions.js") as tfile:
	lines = tfile.readlines()

	for line in lines:
		if not line.lstrip().startswith("//") and "var contractAddress = \"" in line:
			result = re.search('var contractAddress = \"(.*)\";', line.lstrip())
			print(result.group(1))

lines = ''.join(lines)
abi = re.search('eth.contract\((.*)\);', lines, re.DOTALL)
print(abi.group(1))

with open("/home/peter/geth_test/truffle/build/contracts/Offer.json") as sfile:
	lines1 = sfile.read()

result = re.search('\"abi\":(.*),\n  \"bytecode\":', lines1, re.DOTALL)
print(result.group(1))
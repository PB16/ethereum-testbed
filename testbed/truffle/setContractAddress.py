import re

newContractAddress = ""

#extracting contract addresses from output of truffle.
with open("migrations.txt", "r") as sfile:
	for line in sfile:
		line = line.replace(" ","")

		if "Offer:" in line:
			newContractAddress = line.split(':')[1]

#extracting the old contract address and replaces with the contract address.
with open("../geth/scripts/createTransactions.js") as tfile:
	lines = tfile.readlines()

	for line in lines:
		if not line.lstrip().startswith("//") and "var contractAddress = \"" in line:
			result = re.search('var contractAddress = \"(.*)\";', line.lstrip())
			oldContractAdress = result.group(1)
			lines = ''.join(lines)
			lines = lines.replace(oldContractAdress, newContractAddress.strip("\n"))
			break

#saving the changes.
with open("../geth/scripts/createTransactions.js","w") as tfile:
	tfile.writelines(lines)

#extracting the old ABI, so it can be replaced with the new ABI.
lines = ''.join(lines)
abi = re.search('eth.contract\((.*)\);', lines, re.DOTALL)

#extracting the new ABI, so the old one can be replaced.
with open("build/contracts/Offer.json") as sfile:
	lines1 = sfile.read()

result = re.search('\"abi\":(.*),\n  \"bytecode\":', lines1, re.DOTALL)

#replacing old ABI with new ABI, so that it is possible to interact with contract in use.
with open("../geth/scripts/createTransactions.js") as tfile:
	lines = tfile.readlines()
	lines = ''.join(lines)
	lines = lines.replace(abi.group(1), result.group(1))

#saving the changes.
with open("../geth/scripts/createTransactions.js","w") as tfile:
	tfile.writelines(lines)

print("done")
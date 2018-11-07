import re

with open("migrations.txt", "r") as sfile:
	for line in sfile:
		line = line.replace(" ","")

		if "Offer:" in line:
			print(line.split(':')[1])

with open("/home/peter/ethereum-testbed/testbed/geth/scripts/createTransactions.js") as tfile:
	for line in tfile:
		if not line.lstrip().startswith("//") and "var contractAddress =" in line and "\"" in line:
			result = re.search('var contractAddress = \"(.*)\";', line.lstrip())
			print(result.group(1))
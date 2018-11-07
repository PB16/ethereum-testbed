import os

dirName = "/home/henrik/Documents/testbed/docker/composer/filecontainer/truffle"
fileList = os.listdir(dirName)
for file in fileList:
  if 'UTC' in file:
    account = file[-42:-1]
    print(account)


with open("truffle1.js", "wt") as fileOut:
		fileOut.write(
"""module.exports = {
  networks: {
      development: {
        host: "localhost",
        port: 8545,
        network_id: "1234", // Match any network id
        gas: 6500000,
        gasPrice: 2,
        from: """ + '"' + account + '"' + """
      }
    }
};"""
)

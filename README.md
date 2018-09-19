# ethereum-testbed

The current version of the testbed is located on the master branch.
Information about how to use it can be found in the file called "userguide-findings".

To use the testbed the following has to be installed:
  * Geth
  * Node.js
  * Truffle
  * npm
  * Docker
  * Docker-compose
  
I recommend to use Linux as this will make it much simpler to setup.

The docker-compose file contains some variables which is contained in the ".env" file, which is located in the same folder as the docker-compose file.

To make it easier there is a python script in the root folder called "setup.py", which will install the necessary software on Linux.

It will also build a default docker image and set some values in the ".env" file.

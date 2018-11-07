sudo apt-get update && sudo apt-get -y upgrade

sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum

sudo apt-get install -y build-essential
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

sudo npm install -g truffle

sudo apt-get install docker-ce

sudo apt-get install docker-compose

cd .. && sudo docker image build -t testbed -f docker/Dockerfile .

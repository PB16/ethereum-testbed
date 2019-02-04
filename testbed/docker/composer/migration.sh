#$1 is the miner executing the operations.
#Deploying smart contracts and pipe the output to a txt file.
sudo docker exec -it composer_$1_1 /bin/bash -c "cd truffle/ && truffle migrate > migrations.txt"

#Copying file with contract addresses from docker container to host.
sudo docker cp composer_$1_1:/truffle/migrations.txt /home/peter/ethereum-testbed/testbed/truffle/$1_migrations.txt

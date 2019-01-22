sudo docker exec -it composer_$1_1 /bin/bash -c "cd truffle/ && truffle migrate > migrations.txt"

sleep 2

sudo docker cp composer_$1_1:/truffle/migrations.txt /home/peter/Documents/ethereum-testbed/testbed/truffle/$1_migrations.txt

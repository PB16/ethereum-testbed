sudo docker exec -it composer_$1_1 /bin/bash -c "accounts.sh $1"

sleep 2

sudo docker exec -it composer_$1_1 /bin/bash -c "python3 setAccount.py"

sleep 2

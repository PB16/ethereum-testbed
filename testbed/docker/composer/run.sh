sudo docker-compose up -d
sleep 1.5
sudo docker exec -it composer_miner1_1 /bin/bash -c "accounts.sh"
sudo docker exec -it composer_miner1_1 /bin/bash -c "python3 setAccount.py"
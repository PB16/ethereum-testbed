# # # # # # # # # # # # # # # # # # # # # # # # 
#  Ubuntu Dockerfile with pre-installed geth  #
# # # # # # # # # # # # # # # # # # # # # # # #

# Pull base image.
FROM ubuntu

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y openssh-server && \
  apt-get install -y openssh-client && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get install software-properties-common && \
  add-apt-repository -y ppa:ethereum/ethereum && \
  apt-get update && \
  apt-get install -y ethereum && \
  apt-get install nano && \
  mkdir workspace && \
  mkdir truffle && \
  curl -sL https://deb.nodesource.com/setup_6.x && \
  apt-get install -y nodejs && \
  apt-get install -y npm && \
  npm install -g npm && \
  npm install -g n && \
  n stable && \
  npm install -g express && \
  npm install -g truffle && \
  #ln -s -f /usr/bin/nodejs /usr/bin/node && \
  apt-get update && \
  apt-get install -y iproute2 && \
  apt-get install -y iputils-ping && \
  apt-get update && \
  apt-get install python3.6 && \
  rm -rf /var/lib/apt/lists/*

# Add files.
# ADD root/.bashrc /root/.bashrc
# ADD root/.gitconfig /root/.gitconfig
# ADD root/.scripts /root/.scripts

#COPY bootnode ../../../../usr/bin/bootnode
#COPY geth ../../../../usr/bin/geth
COPY truffle ../truffle
COPY accounts.sh ../accounts.sh
COPY setAccount.py ../setAccount.py

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
CMD ["chmod +x accounts.sh"]
CMD ["./accounts.sh"]
CMD ["python3 setAccount.py"]
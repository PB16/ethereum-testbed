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
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  apt-get install software-properties-common && \
  #add-apt-repository -y ppa:ethereum/ethereum && \
  apt-get update && \
  #apt-get install -y ethereum && \
  apt-get update && \
  apt-get install -y iproute2 && \
  apt-get install -y iputils-ping && \
  mkdir workspace && \
  rm -rf /var/lib/apt/lists/*

# Add files.
# ADD root/.bashrc /root/.bashrc
# ADD root/.gitconfig /root/.gitconfig
# ADD root/.scripts /root/.scripts

COPY bootnode ../../../../usr/bin/bootnode
COPY geth ../../../../usr/bin/geth

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]

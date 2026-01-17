FROM nvidia/cuda:12.4.0-base-ubuntu22.04
RUN apt-get update && apt-get install -y git git-lfs python3 python3-pip
RUN  curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash  && git lfs install && rm cuda-keyring_1.0-1_all.deb && ln -s /usr/bin/python3 /usr/bin/python && rm -rf /var/lib/apt/lists/*

RUN pip3 pip install moondream-station

CMD [ "moondream-station"]


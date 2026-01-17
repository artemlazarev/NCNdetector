FROM nvidia/cuda:12.4.0-base-ubuntu22.04
RUN apt-get update && apt-get install -y git git-lfs python3 python3-pip

RUN pip3 pip install moondream-station

CMD [ "moondream-station"]


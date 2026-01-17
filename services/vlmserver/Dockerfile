FROM nvidia/cuda:12.4.0-base-ubuntu22.04
RUN apt-get update && apt-get install -y git git-lfs python3 python3-pip

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
RUN python -c "import torch; print(torch.cuda.is_available())"

RUN pip install moondream-station

CMD [ "moondream-station"]


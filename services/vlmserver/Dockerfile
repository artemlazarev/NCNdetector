FROM nvidia/cuda:12.4.0-base-ubuntu22.04
RUN apt-get update && apt-get install -y git git-lfs python3 python3-pip \
                          && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
                          && git lfs install \
                          && rm cuda-keyring_1.0-1_all.deb \
                          && ln -s /usr/bin/python3 /usr/bin/python \
                          && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

RUN git clone --depth 1 https://huggingface.co/spaces/vikhyatk/moondream2 \
    && cd moondream2 && pip3 install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir spaces flash-attn

WORKDIR /moondream2
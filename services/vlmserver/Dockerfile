FROM nvidia/cuda:12.4.0-base-ubuntu22.04
RUN apt-get update && apt-get install -y python3 python3-pip git

RUN pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

RUN git clone --depth 1 https://huggingface.co/spaces/vikhyatk/moondream2 \
    && cd moondream2 && pip3 install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir spaces flash-attn

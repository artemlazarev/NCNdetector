#FROM nvidia/cuda:12.4.0-base-ubuntu22.04
FROM nvcr.io/nvidia/pytorch:25.12-py3
RUN apt-get update && apt-get install -y git git-lfs python3 python3-pip

RUN python3 -c "import torch; print(torch.cuda.is_available())"

#RUN pip install moondream-station
RUN git clone --depth 1 https://huggingface.co/spaces/vikhyatk/moondream2 \
    && cd moondream2 && pip3 install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir spaces flash-attn

#CMD [ "moondream-station"]
MD [ "bash", "-c", "python app.py" ]



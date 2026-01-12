import torch
import clip
from PIL import Image
from pathlib import Path
from tqdm import tqdm

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

texts = [
    "FEMALE_GENITALIA_COVERED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "ANUS_EXPOSED",
    #"FEET_EXPOSED",
    #"ARMPITS_EXPOSED",
    #"BELLY_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    "ANUS_COVERED",
    #"FEMALE_BREAST_COVERED",
    "BUTTOCKS_COVERED"
]
text_tokens = clip.tokenize(texts).to(device)

IMAGE_ROOT = Path("dataset")

def classify_image(image_path: str):
    img = Image.open(image_path).convert("RGB")
    image = preprocess(img).unsqueeze(0).to(device)

    with torch.no_grad():
        logits, _ = model(image, text_tokens)
        probs = logits.softmax(dim=-1)[0]

    # собираем результат
    results = sorted( zip(texts, probs))

    return results

for img in (list(IMAGE_ROOT.rglob("*.jpg"))):
    try:
        ret = classify_image(img)
        print(f"{img}")
        print(f"ret: {ret} \n")
    except Exception as e:
        print("ERR", img, e)
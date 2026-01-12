import os
from pathlib import Path
from tqdm import tqdm
from nudenet import NudeDetector
import json
from typing import Tuple
import nc_py_api


IMAGE_DIR ="/data/images"
dry_run = os.getenv('DRY_RUN', 'False').lower() in ('true', '1', 't')

SAFE_T = 0.1
NSFW_T = 0.8

nc = None
detector = None

def main():
    global nc
    global detector
    nc = nc_py_api.Nextcloud(nextcloud_url=os.environ['NEXTCLOUD_URL'] , nc_auth_user=os.environ['NEXTCLOUD_USERNAME'], nc_auth_pass= os.environ['NEXTCLOUD_PASSWORD'])
    detector = NudeDetector()
    add_tag_to_nc()
    process_dir("/")

interests = [
    "FEMALE_GENITALIA_COVERED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "ANUS_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    "ANUS_COVERED",
    "BUTTOCKS_COVERED"
]
def add_tag_to_nc():
    for item in interests:
        tag = None
        try:
            tag = nc.files.tag_by_name(item)
        except nc_py_api.NextcloudExceptionNotFound as e :
            None
        if tag is None :
            nc.files.create_tag(item)
            print(f"tag : {item} created")
        else:
            print(f"tag : {item} exist")        

def fast_score(path) -> Tuple [float, list]:
    maxscore=0
    ret = []
    try:
        result = detector.detect(path)
    except Exception as e:
        print(" ERR: ", path, " : ", e)
        return maxscore , ret
    for item in result:
        if (item["class"] in interests) and  (item["score"] > SAFE_T):
            if item["score"] > maxscore:
                maxscore= item["score"]
            ret.append(item)
    return maxscore , ret 

def process_dir(directory):
    for node in tqdm(nc.files.listdir(directory)):
        if node.is_dir:
            process_dir(node)
        else:
            img = os.path.join(IMAGE_DIR, node.user_path)
            score, detections = fast_score(str(img))
            nsfw = score > SAFE_T
            if nsfw:
                tags = detections
                add_tag_to_image(node.user_path, )
                print(f"nsfw score = ${score} in : {node.user_path}")
                print(f"detections = ${detections}")

def add_tag_to_image(node: nc_py_api.FsNode):
    if dry_run:
        return
    tag = nc.files.tag_by_name("nsfw")
    nc.files.assign_tag(node,tag)


if __name__ == "__main__":
    main()
    exit

import argparse
import pandas as pd
import os
from tqdm import tqdm as tqdm
import requests 
import time

parser = argparse.ArgumentParser(description='Sample of Fakeddit image downloader', add_help=True)

#parsing in dataframe from given directory 
parser.add_argument("-t", '--type', type=str, help='train, validate, or test')

args = parser.parse_args()
df = pd.read_csv(args.type)

pbar = tqdm(total=len(df))

#creating image folder with corresponding subfolder with label for each image if not existing. 
for i in range(len(df["6_way_label"].unique())):
    if not os.path.exists(os.path.join("images", str(i))):
        os.makedirs(os.path.join("images", str(i)))

#Iterating over every row, saving each image from url in the correct label-folder as jpg-file.
for index, row in df.iterrows():
    time.sleep(0.01)   
    img = requests.get(row["image_url"])
    with open("images/" +str(row["6_way_label"]) + "/" + row["id"] + ".jpg", "wb") as f:
        f.write(img.content) 
    pbar.update(1)

print("done")

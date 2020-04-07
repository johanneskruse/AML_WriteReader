# ============================================================================================================
# import packages
from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import os
import argparse
from tqdm import tqdm
from config import *
import numpy as np

import os
from pathlib import Path


# ============================================================================================================
#Define the argument parser to read in the URL
parser = argparse.ArgumentParser()
parser.add_argument('-fname', default="data/proposals2.npz", help='File with image links')
parser.add_argument('-url_name', type=str, default="url", help='Name of the title for the URL')
args = vars(parser.parse_args())
f_name = args['fname']
url_name = args['url_name']

# f_name = "data/proposals2.npz"
# url_name = "url"
# ============================================================================================================
# Function to take an image url and save the image in the given directory
def download_image(url, save_path):
    name = str(url.split('/')[-1])
    urllib.request.urlretrieve(url,os.path.join(save_path, name))

# ============================================================================================================
# Generate all folders needed: 
local_files = Config.local_path

# Create the directory name where the images will be saved
dir_img = local_files / "data" / "images"
# Create the directory if already not there
if not os.path.exists(dir_img):
    os.mkdir(dir_img)

# Load data: 
dir_data = local_files / f_name
data = np.load(dir_data, encoding="latin1")

# ============================================================================================================
links = data[url_name]
error_img = []

for i, img in enumerate(links): 
    try:
        download_image(img, dir_img)
    except:
        error_img.append([i, img])
        print(f"Error for image: {i}")

    # Print the number of images
    if i % 100 == 0: 
        print(f"[INFO] Downloaded {i} of {len(links)} images.")


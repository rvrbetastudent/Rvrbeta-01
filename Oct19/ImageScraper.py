"""
===========================================================
Program Name: ImageScraper.py
Author: Ryan Vrbeta
Date: 2025-10-13
Description:
    This program performs an image scrape of a funny meme.
    It is designed to output filepaths of images and ads.
    
Usage:
    Run the script using Python 3.x. Ensure all dependencies
    are installed before execution.

===========================================================
"""
import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.text
htmldata = getdata("https://memecreator.org/meme/big-chungus/")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
    print(item['src'])
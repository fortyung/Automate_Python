"""
downloadXkcd.py :
    Loads the XKCD home page
    Saves the comic image on that page
    Follows the Previous Comic link
    Repeats until it reaches the first comic.
"""
#! python 3
import os
import requests
from bs4 import BeautifulSoup

url = "https://xkcd.com"
os.makedirs("xkcd", exist_ok=True)  # will not give an error if the dir already exist

while not url.endswith("#"):

    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status

    soup = BeautifulSoup(res.text, "lxml")
    comicElem = soup.select("#comic img")

    if comicElem == []:
        print("Cannot find page.")
    else:
        comicUrl = "http:" + comicElem[0].get("src")

        print(f"Downloading image {comicUrl}...")
        res = requests.get(comicUrl)
        res.raise_for_status

    with open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb") as imageFile:
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)

    # previous button url
    prevlink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevlink["href"]

print("-----------------\n")
print("Done.")

import requests
import os
from bs4 import BeautifulSoup

file_list = os.listdir("books_html")
file_list_html = [file for file in file_list if file.endswith(".html")]


def extract_image_src(result):
    img = result.find("img")
    src = img.get("src")
    if (
        src
        == "https://d2nchlq0f2u6vy.cloudfront.net/cache/2a/d4/2ad4a2027833645e2a809afa63453c47.jpg "
    ):
        src = None
    return src


def extract_slader(folder_name):
    images = []
    for html_name in file_list_html:
        path = "books_html/" + html_name
        html = open(path, "r", encoding="UTF8")
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all("article", {"class": "textbook-work-index-widget"})
        for result in results:
            image_src = extract_image_src(result)
            if image_src is not None:
                images.append(image_src)

    return images


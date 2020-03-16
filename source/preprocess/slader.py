import requests
import os
from bs4 import BeautifulSoup


no_image = "https://d2nchlq0f2u6vy.cloudfront.net/cache/2a/d4/2ad4a2027833645e2a809afa63453c47.jpg "


def extract_image_src(result):
    img = result.find("img")
    src = img.get("src")
    return src


def extract_slader(folder_name):
    file_list = os.listdir("books_html/" + folder_name)
    file_list_html = [file for file in file_list if file.endswith(".html")]
    print(file_list_html)

    images = []
    for html_name in file_list_html:
        path = "books_html/" + folder_name + "/" + html_name
        html = open(path, "r", encoding="UTF8")
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all("article", {"class": "textbook-work-index-widget"})
        for result in results:
            image_src = extract_image_src(result)
            if image_src is not no_image:
                images.append(image_src)

    return images


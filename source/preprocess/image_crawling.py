import requests
import urllib.request
from slader import extract_slader
import os

opener = urllib.request.build_opener()
opener.addheaders = [
    (
        "User-Agent",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
    )
]
urllib.request.install_opener(opener)

folder_names = os.listdir("books_html")
# print(folder_names)
for folder_name in folder_names:
    number = 1
    sources = extract_slader(folder_name)
    length = len(sources)
    print("complete " + folder_name + " : 0%", end="")
    for img_url in sources:
        urllib.request.urlretrieve(
            img_url, "sample_images/" + folder_name + "/" + str(number) + ".jpg",
        )
        print(
            f"\rcomplete {folder_name} : {round((float(number / length) * 100))}%",
            end="",
        )
        number = number + 1
    print()
    print(f"Number of images : {number - 1}")

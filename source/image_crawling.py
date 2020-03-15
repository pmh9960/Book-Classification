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

number = 1
folder_names = os.listdir("books_html")
print(folder_names)
for folder_name in folder_names:
    sources = extract_slader(folder_name)
    length = len(sources)
    for img_url in sources:
        urllib.request.urlretrieve(
            img_url,
            "sample_images/" + folder_name + "engineering_" + str(number) + ".jpg",
        )
        number = number + 1
        if number % 10 == 0:
            print(float(number / length) * 100, "%")
    print(f"Number of images : {number - 1}")

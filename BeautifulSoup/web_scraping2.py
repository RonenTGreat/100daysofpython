from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser")

tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you"

with open("changed.html", "w") as file1:
    file1.write(str(doc))

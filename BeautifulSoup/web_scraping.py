from bs4 import BeautifulSoup
import requests

# with open("index.html", "r") as file:
#     doc = BeautifulSoup(file, "html.parser")
#
# tags = doc.find_all("p")[0]
# print(tags.find_all("b"))

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_" \
      "re=3080-_-14-932-436-_-Product"
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)


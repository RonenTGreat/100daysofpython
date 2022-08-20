from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.findAll(name='a', class_='titlelink')
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)

index_of_highest_upvote = article_upvotes.index(max(article_upvotes))
print(article_texts[index_of_highest_upvote])
print(article_links[index_of_highest_upvote])






















# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
#
# all_anchor_tags = soup.findAll(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.string)
#     # print(tag.getText())
#     # print(tag.get('href'))
#     pass
#
# heading = soup.find(name='h1', id='name')
# # print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText())
#
# company_url = soup.select_one(selector='p a')
# print(company_url)

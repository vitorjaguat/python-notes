import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text # the source code 

soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)

article_tag = soup.select_one('.title .titleline a')
article_title = soup.select_one('.title .titleline a').getText()
article_link = article_tag['href']
article_score = soup.find(name='span', class_='score').text
# print(article_title)
# print(article_link)
# print(article_score)

all_article_tags = soup.find_all(name='a', attrs={'rel': 'noreferrer'})
all_articles_texts = [tag.text for tag in all_article_tags]
all_articles_links = [tag['href'] for tag in all_article_tags]
all_articles_upvotes = [int(span.text.split()[0]) for span in soup.find_all(name='span', class_='score')]
# print(all_articles_texts, all_articles_links, all_articles_upvotes)

largest_score = max(all_articles_upvotes)
largest_score_article_title = all_articles_texts[all_articles_upvotes.index(largest_score)]
largest_score_article_link = all_articles_links[all_articles_upvotes.index(largest_score)]
print(largest_score_article_title)


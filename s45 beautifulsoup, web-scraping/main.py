from bs4 import BeautifulSoup
# import lxml 

with open('./website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())
all_anchor_tags = soup.find_all(name='a') # returns a list of all a tags
print(all_anchor_tags)

for tag in all_anchor_tags:
    tag_text = tag.getText() # get the text content of a tag
    tag_href = tag.get('href') # get the href attribute value of a tag
    print(tag_href)

heading = soup.find(name='h1', id='name') # find the h1 with id="name"
print(heading)

section_heading = soup.find(name='h3', class_='heading') # find the first h3 with the class='heading'
print(section_heading.text)

company_url = soup.select_one(selector='p a') # find the element with the css selectors 'p a'
print(company_url)

all_section_headings = soup.select(selector='.heading') # returns a list with all elements with the .heading css selector
print(all_section_headings) 
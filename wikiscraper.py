from bs4 import BeautifulSoup

import os
from urllib.request import urlopen
url = urlopen("https://en.wikipedia.org/wiki/Process_corners")
content = url.read()
soup = BeautifulSoup(content, "html.parser")
links = soup.findAll("a")

#stackoverflow: bumpkin - https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text

#eliminate script/style
for script in soup(["script", "style", "head", "title", "table"]):
	script.extract()
text = soup.get_text()

#by id
#soup.find('div', id="toc").decompose()
#by class
#for div in soup.findAll("div", {'class':'reflist'}):
#        div.decompose()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = os.linesep.join(chunk for chunk in chunks if chunk)
print(text)

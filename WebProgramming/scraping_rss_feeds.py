from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')

xml = BeautifulSoup(req,'xml')

for item in xml.findAll('item')[1:]: # this cycles through the return, scipping item[0] and going from 1 on.
	print(item.text) # this will give you the item between the tags. so http.... instead of <links>http...</link>

	## If you wanted to simply open those pages we could do the following
	url = item.text
	news = urllib.request.urlopen(url).read()
	print(news)

inp = input("")
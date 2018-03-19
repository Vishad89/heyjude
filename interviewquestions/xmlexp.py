
"""Parse XML file""" 

import requests
from xml.etree import ElementTree


def loadfile():

	url='http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
	resp=requests.get(url)

	with open('newsfeed.xml', 'wb') as f:
		f.write(resp.content)

loadfile()

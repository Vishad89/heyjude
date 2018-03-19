
"""Parse XML file""" 

import requests
from xml.etree import ElementTree


def loadfile():

	url='http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
	resp=requests.get(url)

	with open('rssfeed.xml', 'r') as f:
		f.read(resp.content)

loadfile()

"""XML file - Python play""" 

import requests
from xml.etree import ElementTree
import csv


def loadXML():

	# Get web URL for the newsfeed
	url='http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
	resp=requests.get(url)

	with open('newsfeed.xml', 'wb') as f:
		f.write(resp.content)


def parseXML(xmlfile):

	# Create element Tree object for the XML file
	tree = ElementTree.parse(xmlfile)

	# Find the root element for the tree
	root = tree.getroot()

	news = []
	
	for item in root.findall('./channel/item'):

    	newsitems = {}
 
        # iterate child elements of item
        for child in item:
 
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                newsitems['media'] = child.attrib['url']
            else:
                newsitems[child.tag] = child.text.encode('utf8')
 
        # append news dictionary to news items list
        news.append(newsitems)
	
	return news

def xml2csv(news, filename):

	fields = ['Title','Description','Link','GUID','PubData','Media']

	with open('newsfeed.csv', 'w') as csvfile:

		writer = csv.DictWriter(csvfile, fieldnames = fields)

		writer.writeheader()

		writer.writerows(news)




def main():
 

	# Load an XML file from a web URL
	loadXML()

	# Parse the XML file 
	news = parseXML('newsfeed.xml')

	# convert to csv
	xml2csv(news, 'newsfeed.csv')

if __name__ == "__main__" :
	
	main()



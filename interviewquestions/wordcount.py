""" Find 10 most frequently used words from a file """
""" The search should avoid basic or common words (ie. is, at , am , are, you, I , etc...)"""

from collections import defaultdict
import re

def wordscount():

	f = open("abc.txt", 'r')
	
	"""The defaultdict here will initiate the dictionary"""
	
	wordcount = defaultdict(int)

	""" remove special chars in the line"""
	
	for line in f:
		line = line.replace(',','').replace(')','').replace('.','').replace('\'','').lower().split()
	
		for word in line:
			if 3 < len(word) < 10:
				wordcount[word] += 1
	
	
	"""This is to Sort dictionary by Value"""
	""" """
	"""The "reverse = True" at the end, sort the dictionary key values in descending order"""
	
	wordcount_sorted = sorted(wordcount.items(), key = lambda (k, v) : v , reverse= True)
	
	"""print only top 10 Frequetly used word in the file""" 
	i = 0
	for k,v in wordcount_sorted:
		print "%s : %s" % (k, v)
		i += 1
		if i==10:
			break

wordscount()

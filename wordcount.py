from collections import Counter
from collections import defaultdict
import re

def wordscount():

	f = open("abc.txt", 'r')
	wordcount = defaultdict(int)
	#word = re.sub(r '[^a-z0-9]',' ', word.lower().split())
	for line in f:
		line = re.sub(r'\w+', '', line.lower().split())
		wordcount[word] += 1
	return wordcount 

print wordscount()



#words = re.findall(r'\w+', open('abc.txt').read().lower())
#print Counter(words).most_common(10)
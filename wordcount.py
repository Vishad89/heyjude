from collections import Counter
from collections import defaultdict
import re

def wordscount():

	f = open("abc.txt", 'r')
	wordcount = defaultdict(int)
	#word = re.sub(r '[^a-z0-9]',' ', word.lower().split())
	for line in f:
		#line = re.sub(r'\w+', ' ', line.lower().split())
		line = line.replace(',','').replace(')','').replace('.','').lower().split()
		for word in line:
			wordcount[word] += 1
	print wordcount
	wordcount_sorted = sorted(wordcount.items(), key = lambda (k, v) : v , reverse= True)
	#for word in wordcount:
	print wordcount_sorted
	print wordcount_sorted[:10]
	# for keys in wordcount_sorted:
	#  	return keys, wordcount_sorted[keys]
	#  	i += 1
	#  	if i == 10:
	#  		break


wordscount()



#words = re.findall(r'\w+', open('abc.txt').read().lower())
#print Counter(words).most_common(10)
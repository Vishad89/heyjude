# check if the input string is a palindrom 


def checkifpalindrom(str):
	
#remove spaces from string
	str = str.replace(' ', '')

#convert it into a list
	str_old = str
	str_list = list(str)
	#print str_list

#reverse the list
	#str_list = str_list.reverse()
	l = len(str_list)
	i = 0 
	while (i <= (l-i)):
		str_list[i], str_list[l - i - 1] = str_list[l - i - 1], str_list[i]
		i = i + 1
	str_new = ''.join(str_list)
	print str_new, str_old
	if str_new == str_old:
		print "palindrom"
	else:
		print "not a palindrom"

def main():
	a = raw_input("enter any string or a statement: ")
	#a = "my car is great"
	checkifpalindrom(a)

if __name__ == "__main__":
main()
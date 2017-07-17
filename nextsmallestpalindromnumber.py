# Given a number, find the next smallest palindrome larger than the number. 
# For example if the number is 125, next smallest palindrome is 131.


def nextsmallestpalindrom(num):
	global strlength 
	strlength = len(str(num))
	oddlength = (strlength%2 != 0)
	lefthalf = getlefthalf(num)
	middledigit = getmiddledigit(num)
	#nextsmallestpalindrom(num)

	if oddlength:
		increament = pow(10, strlength/2)
		newnum = int(lefthalf + middledigit + lefthalf[::-1])
	else: 
		#increament = int (1.1* pow(10, strlength/2))
		increament = int (1.1 * pow(10, strlength/2))
		newnum = int(lefthalf + lefthalf[::-1])

	if newnum > int(num):
		return newnum
	elif int(middledigit) != 9:
		return int(newnum) + increament
	else:
		return nextsmallestpalindrom(roundup(num))


def getlefthalf(num):
	return str(num)[:strlength/2]

def getmiddledigit(num):
	return str(num)[(strlength-1)/2]

def roundup(num):
	increament = int(pow(10,((strlength/2) + 1)))
	num = int(num)
	return ((num/increament) + 1)*increament	


if __name__ == "__main__":
	num = raw_input("enter any number: ")
	print nextsmallestpalindrom(num)
def strmul(a, b):
	a = int(a)
	b = int(b)

	c = str(a * b)
	return c
	return type(c)


def main():
	str1 = raw_input("enter long digits: ")
	str2 = raw_input("ener another long digit: ")
	print type(str1), type(str2)
	print strmul(str1, str2)

main()
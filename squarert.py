def squarert(num):
	i = 1.00
	#for i in range(1, num/2, 0.01)
	while (i <= (num/2)):
		if num / i == i:
			return i
			break
		else:
			pass
			i = i + 1
	#print "No sqrt for the given number"

def main():
	b = raw_input("enter any number: ")
	print squarert(float(b))

if __name__ == "__main__":
	main()

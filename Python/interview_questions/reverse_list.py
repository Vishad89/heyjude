# reverse list between two given numbers

def rev_list(list, a, b):

	print("Before swap:" , list)

	if (b > a):
		while (a < b):
			list[a], list[b] = list[b], list[a]
			a += 1
			b -= 1
	else:
		while(a > b):
			list[b], list[a] = list[a], list[b]
			b += 1
			a -= 1

	print("After swap: " , list)
	

"""create an array"""
def userarr():

	arr1 = []
	elem = int(input("insert how many elements you want:"))
	for i in range(0, elem):
    		arr1.append(int(input("Enter element no {}: ".format(i+1))))
	return (arr1)

def main():

	print ("Let's create the List first")
	print ("We will need some inputs from you \n")
	listA = userarr()
	print (listA)
	
	l = int(len(listA))
	print ("enter two number less than " , l)
	num1 = int(input("first number: "))
	num2 = int(input("second number: "))

	rev_list(listA, num1, num2)

if __name__ == "__main__" :
	main()


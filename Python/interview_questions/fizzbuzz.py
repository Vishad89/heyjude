#fizzbuzz

def fizzbuzz(num, i, j):
	for n in range(1,num+1):
		result = ""
		if n%i == 0:
			result = "fizz"
		if n%j == 0:
			result += "buzz"
		if not result:
			result = n 
		print(result)

def main():
	n = int(input("a number: "))
	n1 = int(input("a number less than {} :".format(n)))
	n2 = int(input("a number less than {} :".format(n)))
	
	fizzbuzz(n,n1,n2)

if __name__ == "__main__" :
	main()
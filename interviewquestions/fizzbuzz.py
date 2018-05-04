#fizzbuzz

def fizzbuzz(num, i, j):
	print (num, i, j)
	for n in range(1,num+1):
		if n%(i*j) == 0:
			print("fizzbuzz")
		elif n%i == 0:
			print("fizz")
		elif n%j == 0:
			print("buzz")
		else: 
			print(n)

def main():
	n = int(input("a number: "))
	n1 = int(input("a number less than {} :".format(n)))
	n2 = int(input("a number less than {} :".format(n)))
	
	fizzbuzz(n,n1,n2)

if __name__ == "__main__" :
	main()
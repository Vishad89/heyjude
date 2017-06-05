def is_prime(num):
	factors = []
	for i in xrange(2, (num // 2)):
		#print i
		if num%i == 0:
			factors.append(i)
	return factors


a = raw_input("input any number:")
is_prime(a)

# def prime(n):
# 	myList = []
# 	for i in xrange(1, int(n ** 0.5 + 1)):
# 	    if n % i == 0:
# 	        if (i != n/i):
# 	            myList.append(i)
# 	            myList.append(n / i)
# 	        else:
# 	            myList.append(i)
# 	return myList 


# print prime(15)
def arrcrt():

	arr = []
	elem = int(raw_input("insert how many elements you want:"))
    random= bool(raw_input("do you need it to be random? [y/n]:"))
	if random:
        for j in range (elem):
            arr.append(random.randrange(1,100,1))
    else:
        for i in range(0, elem):
        	arr.append(int(raw_input("Enter next no :")))
	print arr
arrcrt()
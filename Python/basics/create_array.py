import random as r

def create_array():
    arr = []
    elem = int(input("insert how many elements you want:"))
    random= bool(input("do you need it to be random? [y/n]:"))
    if random:
        for _ in range (elem):
            arr.append(r.randrange(1,1000))
    else:
        for _ in range(elem):
            arr.append(int(input("Enter next no in range [1,1000] : ")))
    return arr 
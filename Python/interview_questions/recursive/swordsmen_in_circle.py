#!/usr/bin/python

def eliminate_swordsmen(num):
    if len(num) == 2:
        num.pop(1)
        print(num[0])
    else:
        num.pop(1)
        a = num.pop(0)
        num.append(a)
        eliminate_swordsmen(num)

def main():
    a = int(input("Enter how many swordmen are in the circle: "))
    arr = list(range(1,a+1))
    eliminate_swordsmen(arr)

main()

#!/usr/bin/python

def findnumber(arr,k):
  if k in arr:
    return "yes"
  else: 
    print "no"

if __name__ == "__main__":
    arr = [5,1,2,3,4]
    k = 1
    res = findnumber(arr,k)
    print res

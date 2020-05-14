#!/usr/bin/python3
def fib(n):
   fibValues = [0,1]
   for i in range(2,n+1):
      fibValues.append(fibValues[i-1] + fibValues[i-2])
   return fibValues[n]

def main():
    num = input("enter a postive number: ")
    print(fib(int(num)))

main()
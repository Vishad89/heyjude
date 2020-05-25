"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""
class Solution:
    def powr(self, x : int, n : int) -> float:
        if not n :
            return 1
        if n < 0:
            return 1 / (x *self.powr(x,-n))
        elif n > 0:
            return (x * self.powr(x, n-1))
        return (powr(x*x,n/2))

num = float(input("input a number between [-100 , 100] : " ))
power = int(input("input a power between [-231 , 230] : "))
p = Solution()
print(num," ** ", str(power), " = ", p.powr(num,power))
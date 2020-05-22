"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

"""

def majority_element_p2(arr):
    num1, num2, count1, count2 = 0,1,0,0
    for i in arr:
        if i == num1:
            count1 +=1
        elif i == num2:
            count2 +=1
        elif count1 == 0:
            num1 = i
            count1 == 1
        elif count2 ==0:
            num2 = i
            count1 == 1
        else:
            count1, count2 = count1 - 1, count2 - 1
        #print(num1, count1, num2, count2)
    return [n for n in (num1, num2)
                    if arr.count(n) > len(arr) // 3]

print(majority_element_p2([1,1,1,3,3,2,2,2]))


#method2
from typing import List
from collections import Counter
class Solution:
    def majorityElement2(self, nums : List[int]) -> List[int]:
        counts = Counter(nums)
        threshold = len(nums) / 3
        res = []
        for key, count in counts.items():
            if count > threshold:
                res.append(key)
        return res

f = Solution()
print(f.majorityElement2([1,1,1,3,3,2,2,2]))


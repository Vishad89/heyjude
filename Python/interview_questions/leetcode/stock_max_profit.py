#!/usr/bin/python3

""""
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def max_profit_stock(arr):
    pro = 0
    max_Profit = 0
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > 0:
            pro += arr[i] - arr[i-1]
        else:
            pro = 0
        max_Profit = max(max_Profit, pro)
    return max_Profit

arr = [100,180,260,310,40,595,610]
print(max_profit_stock(arr))

# def maxProfit(prices):
#     max_profit, min_price = 0, float('inf')
#     for price in prices:
#         min_price = min(min_price, price)
#         profit = price - min_price
#         max_profit = max(max_profit, profit)
#     return max_profit

# print(maxProfit([100,180,260,310,40,595,610]))
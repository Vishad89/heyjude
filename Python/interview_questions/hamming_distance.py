#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
def hammingdistance(a,b):

    arra = convert2binary(a)
    arrb = convert2binary(b)
    hd = 0
    print arra, arrb
    rng = min(len(arra), len(arrb))
    diff= abs(len(arra) - len(arrb))
    print rng, diff
    for i in range(0,rng):
        print i,arra[i], arrb[i]
        if arra[i] != arrb[i]:
            hd += 1
    hd = hd + diff
    return hd


def convert2binary(num):
    num = int(num)
    binary = []
    while num > 1:
        binary.append(num%2)
        num = (num // 2)
    if num == 1:
        binary.append(num)
    return binary

print hammingdistance(1,4)
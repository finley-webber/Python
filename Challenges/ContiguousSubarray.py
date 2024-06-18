"""
Challenge: Maximum Product Subarray
Objective: Write a Python function called max_product that finds the maximum product of a contiguous subarray
 within a given array of integers.

Description:
Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest 
product. The function should return the maximum product.
"""

num = 0
arr = []

while num == 0 or num != "":
    num = input("Enter a number: ")
    if num.isalpha() or num == "":
        num = ""
    else:
        arr.append(int(num))

def max_product(arr):
    highestValue = 0
    for x in len(arr):
        currentArr = [arr[x]]
        currentValue = arr[x]
        

print(arr)
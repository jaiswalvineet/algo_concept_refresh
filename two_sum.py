#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:23:30 2022

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""

from typing import List

## python function with function annotation O(n2)

# # Brute-force solution:
def twoSumBF(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


## another better method 

def twoSumBetter(nums: List[int], target: int) -> List[int]:
    dictionary = {}
    
    for i in range(len(nums)):
        secondNumber = target-nums[i]
        print(secondNumber)
        if(secondNumber in dictionary.keys()):
            secondIndex = nums.index(secondNumber)
            if(i != secondIndex):
                # return [i, secondIndex]
                return sorted([i, secondIndex])
        dictionary.update({nums[i]: i})
        print(dictionary)

nums = [1,2,4,5,9]
target = 6

# print(twoSumBF(nums, target))
print(twoSumBetter(nums, target))
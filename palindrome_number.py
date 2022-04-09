#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 12:23:29 2022

"""
## need to check coplexity of all the solutions
class Solution:
    def isPelindromeStringSlicing(self, x:str)-> bool:
        if(x == x[::-1]):
            return True
        else:
            return False
        
    def isPelindromeReverse(self, x:str)-> bool:
         reversed_string = ''.join(reversed(x))
         print(reversed_string)
         if(x == reversed_string):
             return True
         else:
             return False
    
    ## integer only
    def isPelindromeNumericWhile(self, x:int)-> bool:
        temp = x
        rev = 0 
        while(x>0):
            last= x%10
            rev = rev*10 + last
            print('reverse', rev)
            x = x//10
            print('x', x)
        if(rev==temp):
            return True
        else:
            return False
    
    def isPelindromeStringReverse(self, x:str)-> bool:
        temp = x
        rev = ''
        for i in range(len(x), 0, -1):
            print(i)
            rev = rev + x[i-1]
            print('reverse', rev)
        if(rev==temp):
            return True
        else:
            return False
    def isPelindromeWhileString(self, x:str)-> bool:
        # both way journey 
        l = len(x)
        first = 0
        last = l-1
        isPelindrome = True
        while(first<last):
            if(x[first]==x[last]):
                first += 1
                last -= 1
            else:
                isPelindrome = False    
                break
        return isPelindrome
            
        
            
        
s = Solution()     
# print(s.isPelindromeNumericWhile(121121))
# print(s.isPelindromeStringSlicing('madam'))
# print(s.isPelindromeStringReverse('madam'))
#print(s.isPelindromeReverse('vineet'))    
print(s.isPelindromeWhileString(('madam')))    

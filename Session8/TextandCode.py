# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:32:44 2020

@author: raajesh.rameshbabu
"""
1.
# write a python function to check user provided number is prime or not and print the result
def primeornot(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

primeornot(7)                

2.
# write a python program to swap two numbers and print it
num1 = 5
num2 = 10
temp = num1
num1 = num2
num2 = temp
print("The value of num1 after swapping: {}".format(num1))
print("The value of num2 after swapping: {}".format(num2))

3. 
# write a python function to add user provided list and return the result
def addlist(list1,list2):
    result = list1+list2
    return result

answer = addlist(['cat','dog'],['samsung','oneplus'])

4.
# write a python function to reverse user provided list and return the result
def reverselist(inlist):    
    inlist = inlist[::-1] 
    return inlist

result = reverselist([1,2])

5.
# write a python function to find the factorial of the user provided number and print the result
def findfactorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
        
findfactorial(3)        

6.
# write a python function to find the largest element in an array and return the result
def largest(arr):
    max = arr[0]
    n = len(arr)
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
        return max

largest([1,20,3])    

7.
# write a python function to check if a string is palindrome or not and print the result
def isPalindrome(s):
    if (s == s[::-1]):
        print("Given string is palindrome")
    else:
        print("Given string is not palindrome")

s = "malayalam"
isPalindrome(s)

8.
# 

                
        




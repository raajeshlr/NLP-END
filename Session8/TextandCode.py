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
# write a python function to reverse the user provided sentence and return the result
def revsentence(insentence):
    words = insentence.split(" ")
    outsentence = " ".join(reversed(words))
    return outsentence

revsentence("I am doing NLP Course")

9.
# write a python function to interchange first and last elements in a list
def swaplist(inlist):
    size = len(inlist)
    temp = inlist[0]    
    inlist[0] = inlist[size-1]
    inlist[size-1] = temp
    return inlist

swaplist([1,2,3,4,232,5343,21,7])

10.
# write a python function to print even length words in a string
def evenprintwords(s):
    s = s.split(" ")
    for word in s:
        if len(word)%2==0:
            print(word)
            
evenprintwords("i am doing nlp course")            

11.
# write a python function to Calculate and return mean of user provided list of numbers
def calmean(the_list):
  return sum(the_list)/len(the_list)

calmean([1,2,3,4,5])

12.
# write a python function to empty an user provided list of items
def emptylist(inlist):
  inlist.clear()
  return inlist
               
emptylist([1,2,3]) 

13.
# write a python function to divide all items in user provided list by n
def dividebyn(inlist,n):
  inlist=[x/n for x in inlist]
  return inlist
        
dividebyn([1,2,3],2)

14.
# Write a Python function to Return a copy of a user provided list
def get_copy(the_list):
  return the_list.copy()

get_copy([1,2,3])

15.
# Write a python function to remove duplicates from a list
def remove_duplicates(the_list):
  return list(set(the_list))

remove_duplicates([1,2,3,2])

16.
# Write a python function to combine and return only unique items from two user provided lists 
def get_combined_unique(list1,list2):
  return list(set(list1).union(set(list2))) 

list1 = [1,2,3,4,2]
list2 = [1,2,3,4,3]
get_combined_unique(list1,list2)

17.
# write a python program to Replace a substring
str1='This is a about animals and cars and scooters'
str2='animals'
str3='vehicles'
str4=str1.replace(str2,str3)
print(str4)

18.
# write a python program to remove an element to a dictionary
dictionary = {'item1': 'value1', 'item2': 'value2'}
dictionary.pop("item2")


19.
# write a python program to return velocity given displacement(m) and time(s)
displacement = 50
time = 34
velocity = displacement/time
print(velocity)

20.
# write a python function to convert feets to meters
def feets_to_meters(feets):    
    meters = 0.3048 * feets    
    return meters

21.
# write a python function to convert celcius to farenheit
def celcius_to_farenheit(celcius):    
    farenheit = (celcius * 9/5) + 32    
    return farenheit

22.
# write a python program to display current time
from datetime import datetime
now = datetime.now() 
print("now =", now)

23.
# write a python function to check if a traingle is a right-angled triangle given sides a,b and c
def is_right_angled_traingle(a, b, c):    
    x, y, z = sorted([a,b,c])    
    if x**2+y**2==z**2:
        print(True)
    else:
        print(False)
        
24.
# write a python program that calculates the time taken for the light(in seconds) to reach an object given its distance(km) from sun
distance_from_sun = 1600000
light_speed = 300000 # km/s
time_taken = distance_from_sun / light_speed
print(time_taken)       

25.
# write a python function to return Return On Investment given first value, last value and number of years
def roi(first_value, last_value, time):    
    return ((last_value/first_value)**(1/time)-1) * 100 

26.
# write a python function to Calculate the distance travelled by a wheel given its radius, rpm and time(minutes)
import math
def distance_travelled(radius, rpm, time):
    perimeter = 2 * math.pi * radius    
    distance_travelled = perimeter * rpm * time    
    return distance_travelled

27.
# write a function to sort all the elements in a list and then print the element with maximum length along with its length value
def print_element_with_max_length(l):
    l = [str(i) for i in l]
    l = sorted(l, key=len, reverse=True)
    return l[0], len(l[0])

28.
# write python function to drop and print elements from a list for a given set of indexes
def drop_print_elements_for_indexes(l, i):
    i = sorted(i, reverse=True)
    for idx in i:
        print(l.pop(idx))
        
29.
# write a python function to sort a list of words based on their first character unsing lambda function
def sort_string_based_1st_chr(sl):
    f = lambda x: x[0]
    sl = sorted(sl, key = f)
    return sl        

30.
# write a python program to update a global variable
var = 0
def update_global(inp):
    global var
    var = inp

update_global(5)
var

31.
# write a python function to take and print any number of positional and keyword arguments
def print_any_args_and_kwargs(*args, **kwargs):
    print("postional arguments", args)
    print("keywords arguments", kwargs)
    
print_any_args_and_kwargs(1,2,3, a=4, b=5)

32.
# write a python function to find a list of common elements between two lists using set operation
def find_comm_elems_using_set(l1, l2):
    l1, l2 = set(l1), set(l2)
    return list(l1.intersection(l2))

find_comm_elems_using_set([1,2,3,4,5,5], [3,3,6,4,2,0])

33.
# write a python function to sum all the input values
def sum_all_values(*args):
    return sum(args)

sum_all_values(2,3,4)

34.
# write a python function to return the sum of all the elements in a list using lambda and reduce
from functools import reduce
l = [1,2,3,4,5,5,6,7,8,9,0]
new_l = reduce(lambda x, y: x + y, l)

new_l

35.
# write a function to convert kelometer to miles where conversion factor is 0.621371
def convert_km_to_miles(km):
    return km*0.621371

convert_km_to_miles(100)

36.
# write a python function to extend a list by another list
def extend_list_by_another(l1, l2):
    l1.extend(l2)
    return l1

extend_list_by_another([1,2,3,4,5], [6,7])

37.
# write a python program to print a string in reverse order
def print_string_reverse_order(s):
    print(s[::-1])

print_string_reverse_order("Hello")

38.
# write a python function to convert an integer to hexa decimant format
def convert_int_to_hexa(n):
    return hex(n)

convert_int_to_hexa(100)

39.
# write a python program to print 0.1 upto 30 decimal positions
n = 0.1
print(format(n, '0.30f'))

40.
# write a python program to merge three dictionaries using unpacking
d1 = {'a': 1, 'b':2}
d2 = {'c': 3, 'd':4}
d3 = {'e': 5, 'f':6}

d = {**d1, **d2, **d3}
d

41.
# write a python function to get average value for all the numbers given as input
def avg_of_all_nbr(*args):
    return sum(args) / len(args)

avg_of_all_nbr(1,2,3,4,5)

42.
# write a python lambda function to sum any number of given input numbers
f = lambda *args: sum(args)

f(1,2,3,4,5,6)

43.
# write a python function to get a square root of a number
def sqrt_func(n):
    return n**0.5

sqrt_func(10)

44.
# write a python function to join all the elements of a list with a given separator
def join_all_elems(l, s):
    return s.join(l)

join_all_elems(['hello', 'I', 'am', 'XOR'], ' ')

45.
# write a python function to print the maximum number from a tuple
def print_max_tuple(t):
    print(max(t))

print_max_tuple((1, 6, 4, -3, 2))

46.
# write a python program to remove all the elements from list a that are present in list b using set up operation
a = [1,2,3,4,5]
b = [3,5,7,8]

list(set(a) - (set(b)))

47.
# write a python function to take an interger and print its previous and next integers
def print_prev_next_ints(n):
    print(n-1, n+1)

print_prev_next_ints(10)

48.
# write a python function to print if a given number is less than 100
def check_nbr_less_than_100(n):
    print(n < 100)

check_nbr_less_than_100(80)

49.
# write a python function to take a string as input and print a list of all the characters
def string_to_list(s):
    print(list(s))

string_to_list("hello")

50.
# write a python function to print last five chacters from a given input string
def print_last_five_chrs_string(s):
    print(s[-5:])

print_last_five_chrs_string('Indians')

51.
# write a python function to add two numbers
def add_num(a, b):
    return a + b

add_num(5, 6)

52.
# write a python function print a random choice from a list [1,2,3,4,5,6] of numbers 3 times
def rand_print_list(l):
    import random
    for i in range(3):
        print(random.choice(l))

rand_print_list([1,2,3,4,5,6])

53.
# write a function to divide a number assigned to variable a by another variable b and return the rounded result
def divide_func(a, b):
    return round(a/b)

divide_func(10, 5)

54.
# write a python function to print if all of the elements in a tuple are true
def all_of_tuple(t):
    if all(t):
        print(True)
    else:
        print(False)
        
all_of_tuple((0, 4, False))

55.
# write a python function to print length of a set
def print_lenght_of_set(s):
    print(len(s))
    
print_lenght_of_set({1,3,4,5,5})

56.
# write a python function to split a sentence and create a dictionary with their indexes as keys and words as values using enumerate
def sent_to_dict(s):
    l = s.split()
    d = {k:v for k, v in enumerate(l)}
    return d

sent_to_dict("how are you today")

57.
# write a python program to convert a set to a list
myset = {1, 2, 4, 7}
mylist = list(myset)

58.
# write a python program to print the words in a sentence in reverse order
sentence = 'the quick brown fox'
words = sentence.split(' ')
words.reverse()
print(' '.join(words))

59.
# write a python function that takes a list as an input and converts all numbers to positive numbers and returns the new list
def make_all_positive(nums):
   return [num if num > 0 else -num for num in nums]

60.
# write a python program that prints the area of a rectangle
length = 10
width = 5
print(f'Area: {length * width}')

61.
# write a python program that adds the elements of a list to a set and prints the set
my_set = {1, 2, 3}
my_list = [4, 5, 6]
my_set.update(my_list)
print(my_set)

62.
# write a python function that makes all negative values in a list zero and returns it
def make_negative_zero(items):
   return [0 if item < 0 else item for item in items]

63.
# write a python program to print the first 5 items in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[:5])

64.
# write a python function that returns True if the product of two provided numbers is even
def is_prod_even(num1, num2):
   prod = num1 * num2
   return not prod % 2

65.
# write a python program to print the factorial of a number
num = 5
fact = 1
while num > 0:
   fact *= num
   num -= 1
print(fact)

66.
# write a python program that reverses an integer and prints it
num = 12345
reversed = int(str(num)[::-1])
print(reversed)

67.
# write a program to create a string variable and print the amount of memory it consumes
import sys
string_var = 'string variable'
print(sys.getsizeof(string_var))

68.
# write a python program to print 5 random vowels
import random
vowels = ['a', 'e', 'i', 'o', 'u']
print([random.choice(vowels) for _ in range(5)])

69.
# write a program that multiplies corresponding elements in two lists and prints a new list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
prod_list = [a*b for (a,b) in zip(list1, list2)]
print(prod_list)

70.
# write a program that adds corresponding elements in two lists and prints a new list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
sum_list = [a+b for (a,b) in zip(list1, list2)]
print(sum_list)

71.
# write a program to print 5 random numbers divisible by 4 between 100 and 200
import random
print(random.sample([i for i in range(10, 100) if i%4 == 0], 5))

72.
# write a program to print 5 even random numbers between 10 and 100
import random
print(random.sample([i for i in range(10, 100) if i%2 == 0], 5))

73.
# write a program to remove odd numbers from a list using list comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8]
no_odd_nums = [i for i in nums if i % 2 == 0]

74.
# write a python function that returns a dictionary with the area and perimeter of a rectangle
def calculate_rect_properties(width, height):
   return {
      'perimeter': 2 * (width + height),
      'area': width * height
   }
   
75.
# write a python program that converts a hexadecimal number to hexadecimal and prints it
hexadecimal_num = 'FF'
decimal_num = int(hexadecimal_num, 16)
print(decimal_num)

76.
# write a python program that converts a binary number to decimal and prints it
binary_num = '1010101'
decimal_num = int(binary_num, 2)
print(decimal_num)

77.
# write a python function that takes two strings as a parameter and prints the shorter one
def print_shorter(str1, str2):
   if (len(str1) > len(str2)):
      print(str2)
   else:
      print(str1)

78.
# write a python function to print a given string n times
def printn(string, n):
   print(string * n)

79.
# write a python program to print squares of numbers until 20
for i in range(20):
   print(i*i)

80.
# write a python program to print a random vowel
import random
vowels = ['a', 'e', 'i', 'o', 'u']
print(random.choice(vowels))

81.
# write a python function to return the number of lines in a file
def count_lines(filename):
   with open(filename, 'r') as f:
      contents = f.read().split('\n')
      return len(contents)

82.
# write a function to return the square of first N numbers
def get_squares(n):
   return [i*i for i in range(n)]

83.
# write a python program to print unique numbers in a list
numbers = [1, 2, 2, 3, 4, 4, 5, 6]
unique = set(numbers)
print(f'Unique numbers: {list(unique)}')

84.
# write a function that merges two dictionaries
def merge_dictionaries(dict1, dict2):
   return {**dict1, **dict2}

85.
# write a python function that inverts the key and values in a dict and returns it
def invert_dict(dictionary):
   inverted_dict = {value: key for key, value in dictionary.items()}
   return inverted_dict

86.
# write a python function that returns the weighted average of numbers
def get_weighted_average(numbers, weightage):
   return sum(x * y for x, y in zip(numbers, weightage)) / sum(weightage)

87.
# write a python function to return words in a sentence in sorted order
def get_sorted_words(sentence):
   words = [word for word in sentence.split()]
   words.sort()
   return words

88.
# write a python function to return the sum of first n numbers
def sum_of_nums(n):
   if n <= 1:
      return n
   else:
      return n + sum_of_nums(n-1)

89.
# write a python program to print the factors of a number
num = 320
for i in range(1, num + 1):
   if num % i == 0:
      print(i)

90.
# write a python program to print the ASCII value of a character
character = 'x'
print(f'The ASCII value of {character} is {ord(character)}')

91.
# write a python function to print the octal value of a decimal number
def print_octal(dec):
   print(oct(dec))

92.
# write a python program that prints the sum of natural numbers up to a given number
num = 16
sum = 0
while (num > 0):
   sum += num
   num -= 1
print(f'The sum is {sum}')

93.
# write a python program to extract the file name and extension of a file
import os
filename, extension = os.path.splitext('/path/to/some/file.ext')

94.
# write a python program to print a random vowel
import random
vowels = ['a', 'e', 'i', 'o', 'u']
print(random.choice(vowels))

95.
# write a python program to print common elements in two lists
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [2, 4, 6, 8, 10]
print(f'Common elements: { set(list_a).intersection(set(list_b)) }')

96.
# write a python program to print squares of numbers until 20
for i in range(20):
   print(i*i)

97.
# write a program that multiplies corresponding elements in two lists and prints a new list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
prod_list = [a*b for (a,b) in zip(list1, list2)]
print(prod_list)

98.
# write a program to print 5 random numbers between 100 and 200
import random
print(random.sample(range(100, 200), 5))

99.
# write a python program that reverses an integer and prints it
num = 12345
reversed = int(str(num)[::-1])
print(reversed)

100.
# write a python program that multiplies a tuple n times and print the result
my_tuple = (1, 2, 3)
n = 3
print(my_tuple * 3)
      

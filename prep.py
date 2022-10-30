# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name():
    return "hello_USERNAME!"
print(hello_name())


def hello_name(user):
    print(f"hello_{user}")
hello_name("USERNAME!")


#Question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    odds = list(range(1,101,2))
    return 
print(first_odds())

        

#Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list():
    lst = [1,10,100,1000,9999]
    max_val = None
    for val in lst:
        if max_val == None or max_val < val:
            max_val = val
    return max_val
print(max_num_in_list())


#Question 4:
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/False).
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 ==0
print(is_leap_year(399))


def is_leap_year(year):
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False 
    elif year % 4 == 0:
        leap = True 
    else: 
        leap = False 
    return leap
print(is_leap_year(4000))


#Question 5:
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive number.
#The return should be boolean Type.
#Below 2 i couldn;t get it on my own, i need more explaantion and practice. 
def is_consecutive(lst):
    return sorted(l) == list(range(min(l), max(l) + 1))
l = [1,2,3,4,6,5]
print(is_consecutive(l))



def is_consecutive(lista):
   if len(lista) < 1:
      return False
   min_val = min(lista)
   max_val = max(lista)
   if max_val - min_val + 1 == len(lista):
      for i in range(len(lista)):
         if lista[i] < 0:
            j = -lista[i] - min_val
         else:
            j = lista[i] - min_val
            if lista[j] > 0:
               lista[j] = -lista[j]
            else:
               return False
      return True
   return False
lista = [6, 8, 3, 5, 9, 7]
print(is_consecutive(lista))


# from while1 import add,sub
# add()

# -------------------------------------------------------------------------------------
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

# a=int(input("Enter the first number : "))
# b=int(input("Enter the second number : "))

# while True:
#     print("1. Addition" \
#     "\n 2. Subtraction " \
#     "\n 3. Multiplication" \
#     "\n 4. Divisin" \
#     "\n 5. Exit")
#     choice = int(input("Enter your choice : "))
    
#     if choice == 5:
#         break

#     elif choice==1:
#         c=add(a,b)
#         print(c)

#     elif choice==2:
#         c=sub(a,b)
#         print(c)
#     elif choice==3:
#         c=mul(a,b)
#         print(c)
#     elif choice==4:
#         c=div(a,b)
#         print(c)
# -------------------------------------------------------------------------------------
# ANONYMOUS FUNCTION

# a=lambda a,b:a+b
# print(a(20,30))/
# --------------------------------------------------------------------------------------
#  WITH ARGUMENT WITH RETURN TYPE 

# def square(num):
#     return num * num

# num=int(input("enter the number :"))
# result=square(num)
# print("square:",result)
# ---------------------------------------------------------
# WITH ARGUMENT WITHOUT RETURN TYPE

# def square(num):
#     print("square:",num * num)

# num=int(input("enter the number :"))
# square(num)
# ----------------------------------------------------------------
# WITHOUT ARGUMENT WITH RETURN

# def square():
#     return num * num

# num=int(input("enter the number :"))
# result=square()
# print("square:",result)
# --------------------------------------------------------------------------
# WITHOUT ARGUMENT WITHOUT RETURN

# def square():
#    square=num*num
#    print(square)

# num=int(input("enter the number :"))
# square()

# ----------------------------------------------------------------------------
# Python Function within Another Function

# def word():
#     string='Pythonfunctionstutorial'
#     x=5
#     def number():
#             print(string)
#             print(x)
#     number()
# word()
# ----------------------------------------------------------------------------------
# Recursive Function
# -------------------------------------------------------------------------------------
#1.FACTORIAL OF A NUMBER
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial (x-1))
    
# num = 3
# print("The factorial of", num, "is", factorial(num))

# 2.SUM OF NUMBERS 
# def sum(x):
#     if x==1:
#         return 1
#     else:
#         return(x + sum(x-1))

# num=10
# print("The sum of", num, "is", sum(num))
# ------------------------------------------------------------------------
# Write a function to count vowels in a given string.

# def count_vowels(s):
#     vowels = "aeiou"
#     count = 0
#     for i in s:
#         if i in vowels:
#             count += 1
#     return count

# print(count_vowels("Hello")) 
# ------------------------------------------------------------------------------
# Write a function to calculate the sum of elements in a list.

# def sum_of_list(l):
#     return sum(l)

# l=[10,20,30,40,50]
# total=sum_of_list(l)
# print("Sum of elements in list is :",total)
# -------------------------------------------------------------------------------
# Write a function to reverse a string.
# def reverse_string(s):
#     return s[::-1]

# s="good morning"
# string=reverse_string(s)
# print(string)
# --------------------------------------------------------------------------
# Write a function that takes a list and returns only unique elements.
# def unique_elements(list):
#     unique = []
#     for item in list:
#         if item not in unique:
#             unique.append(item)
#     return unique

# l=[1, 2, 2, 3, 4, 4, 5]
# print(unique_elements(l))
# --------------------------------------------------------------------------
# write a recursive function to reverse a string

# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     else:
#         return (reverse_string(s[1:]) + s[0])
    
# s="hello"
# print(reverse_string(s))  

# ----------------------------------------------------------------------------
# Write a recursive function to calculate power (xⁿ).
# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return (x * power(x, n - 1))

# print(power(2,7))

# -----------------------------------------------------------------------------
# Write a recursive function to count digits in a number.
# def count_digits(n):
#     n = abs(n)
#     if n < 10:
#         return 1
#     else:
#         return( 1 + count_digits(n // 10))

# digit=123
# print(count_digits(digit))   
# ----------------------------------------------------------------------------
# Write a recursive function to print numbers from 1 to N.
# def print_numbers(n):
#     if n == 0:
#         return 
#     else:
#         print_numbers(n - 1)
#         print(n)

# n=5
# print_numbers(n)


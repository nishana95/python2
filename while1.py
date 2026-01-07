# i=1
# while i<10:
#     print(i)
#     i=i+1
# ----------------------------------------------------------------
# n=1
# while n<20:
#     print(n)
#     n=n+2
# ---------------------------------------------------------------
# a="hello"
# l=len(a)
# i=0
# while i<l:
#     print(a[i])
#     i=i+1
# -----------------------------------------------------------------
# Write a program that repeatedly asks the user for a password until the correct one (python123) is entered. 
# Use else to print a success message when the loop completes.
# password=''
# while password!='python123':
#     password=input('Enter the password: ')
# else:
#     print('Correct password')
# --------------------------------------------------------------------------------
# Find a Number Write a program that searches for a specific number in a list.
# Use a loop and else to print whether the number was found or not.
# list=[1,3,5,7,9,10,20]
# item_to_find=int(input('Enter the item to find: '))
# for i in list:
#     if i==item_to_find:
#         print('Number found')
#         break
# else:
#     print('Number not found')
# -----------------------------------------------------------------------------
# Simple Guessing Game Write a program where the user has to guess a secret number (e.g., 7).
# If the guess is correct, print a success message. 
# If the loop ends without the correct guess, print a failure message.

# guess=int(input('Enter your guess:'))
# secret_number=7
# while guess==secret_number:
#     print('Success')
#     break
# else:
#     print('Failed')
# ------------------------------------------------------------------------------------
# CRUD OPERATIONS
# l=[]
# while True:
#     print("1. create " \
#     "\n 2. Add " \
#     "\n 3. update" \
#     "\n 4. delete" \
#     "\n 5. view" \
#     "\n 6. exit")

#     choice = int(input("Enter your choice : "))
#     if choice == 6:
#         break
    
#     elif choice == 1:
#         name = input("Enter your name : ")
#         age= int(input("Enter your age : "))
#         Phone = input("Enter your number : ")
#         s = []
#         s.append(name)
#         s.append(age)
#         s.append(Phone)
#         l.append(s)
#         print(s)
#         print(l)
    
#     elif choice==5:
#         for i in l:
#             print(f"name :{i[0]} ")
#             print(f"age :{i[1]} ")
#             print(f"phone :{i[2]} ")
#         print()

#     elif choice==3:
#         Phone=input("Enter the phone number :")
#         for i in l:
#             if i[2]==Phone:
#                 i[0]=input("Enter the name: ")
#                 i[1]=input("Enter the age :")
#                 i[2]=input("Enter the phone number:")
#                 print("Updated")
#                 break
#             else:
#                 print("Not found")

#     elif choice==4:
#         phone=input("Enter the phone number :")
#         for i in l:
#             if i[2]==phone:
#                 l.remove(i)
#                 print("Deleted")
#                 break
#         else:
#             print("Not found")
# -----------------------------------------------------------------------------
# BREAK,CONTINUE,PASS STATEMENTS

# for string in "Python Loops":
#     if string =="o" or string=="p"or string=="t":
#         continue
# print('Current Letter:',string)
# ----------------------------------------------------------------------------
# LIST COMPREHENSION

# numbers=[1,2,3,4,5]
# a=[x**2 for x in numbers]
# print(a)

# list=[i for i in range(11)if i%2==0]
# print(list)

# matrix = [[j for j in range(5)] for i in range(3)]
# print(matrix)

# ---------------------------------------------------------------------------------------
# FUNCTIONS

def add(a,b):
    return a+b
# add(b=10,a=20)
s=int(input("enter the first number : "))
p=int(input("enter the second number : "))
storage = add(s,p)
print(storage)

# def sub():
#     a=10
#     b=20
#     print(a-b)








# MULTIPLICATION TABLE OF 2
# n=2
# for i in range(1,11):
#     a=n*i
#     print(i,"*",n,"=",a)
    # OTHER PRINTING FORMATS
    # print("{} * {} = {}".format(i,n,a))
    # print(f"{i} * {n} = {a}")

    
# HOW MANY TIMES a COMES IN APPLE
# 1.NORMAL METHOD
# a="apple"
# i=a.count("a")
# print(i)
# 2.Using for loop
# a="apple"
# c=0
# for i in a:
#    if i=="a":
#       c=c+1
# print(c)


# COUNT VOWELS IN A STRING
# l=["a","e","i","o","u"]
# string=input("Enter the string: ")
# count=0
# for i in string:
#     if i in l :
#         count=count+1
# print(count)      

# AMSTRONG NUMBER
# a=int(input('Enter the number: '))
# l=len(str(a))
# n=str(a)
# answer =0
# for i in n:
#     answer=answer+int(i)**l
# if answer==a:
#     print("it is amstrng number")
# else:
#     print('it is not amstrong number')

# FIBONACCI SERIES
# a=0
# b=1
# n=int(input("Enter the range: "))
# print(a,b, end=" ")
# for i in range (n):
#     c=a+b
#     print(c, end=" ")
#     a=b
#     b=c

# PRINT LIST OF SQUARES OF GIVEN LIST
# numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# square=0
# squares=[]
# for value in numbers:
#         square=value**2
#         squares.append(square)
# print("The list of squares is",squares)

# PRINT LIST OF NUMBERS GIVEN
# a= int(input("enter the size :"))
# l=[]
# for i in range(0,a):
#     d = int(input("enter the number :  "))
#     l.append(d)
# print(l)

# PRINT HELLO IN REVERSE
# a = "hello"
# print(a[::-1])
# b=""
# for i in a:
#     b=i+b
#     print(b)

# 1. Write a program to calculate the sum of numbers from 1 to 10 using a for loop.
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print('Sum of numbers: ',sum,end=' ')

# 2. Filter Even Numbers Write a program to print only even numbers from a list.
# list=[2,5,7,10,20,15]
# for i in list:
#     if i%2==0:
#         print(i,',',end=' ')

# 3.Multiplication Table Use nested loops to create a multiplication table for numbers 1 to 5.

# for i in range(1,11):
#     for j in range(1,6):
#         a=i*j
#         print(i,'*',j,'=',a,' ',end=' ')
#     print()

# PRINT EVEN AND ODD NUMBERS UPTO 20 USING FOR LOOP
# print('Even numbers:- ')
# for i in range(1,21):
#     if i%2==0:
#         print(i,end=" ")
# print()
# print('Odd numbers:- ')
# for i in range(1,21):
#     if i%2!=0:
#         print(i,end=" ")

# [20,18,10,5,100,80]PRINT GIVEN LIST IN ACCENDING ORDER
# list=[20,18,10,5,100,80]
# list.sort()
# print(list)
# l=[20,18,10,5,100,80]
# length = len(l)
# for i in range(0,length):
#     for j in range(0,length):
#         if l[i]<l[j]:
#             c=l[i]
#             l[i]=l[j]
#             l[j]=c
# print(l)

        # ASCII TABLE

# for i in range(70,76):
#     for j in range(70,i+1):
#         print(chr(j),end=" ")
#     print()




  


        
    
        
    
         

    
            

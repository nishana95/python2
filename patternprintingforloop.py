# 1. RIGHT HALF PYRAMID
# for i in range(0,5):
#     for j in range(0,i+1):
#         print("* ",end=(" "))
#     print()

# 2. LEFT HALF PYRAMID
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" " ,end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# 3. FULL PYRAMID
# n=5
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# 4. INVERTED RIGHT HALF PYRAMID
# n=6
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()


# 5. INVERTED LEFT HALF PYRAMID
# n=5
# for i in range(1,n+1):
#     for j in range(1,i):
#         print(' ',end=" ")
#     for k in range(n-i+1):
#         print('*',end=' ')
#     print()      

# 6. INVERTED FULL PYRAMID
# n=6
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(end=" ")
#     for j in range(1*i-1):
#         print("*",end=" ")
#     print()

# 7. RHOMBUS PATTERN
# n=6
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(end=" ")
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

# 8. DIAMOND PATTERN
# n=5
# for i in range(n):
#     print(' '*(n-i-1)+"* "*(i+1))
# for j in range(n-1,0,-1):
#     print(" "*(n-j)+'* '*(j))

# 9.HOURGLASS PATTERN
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end="")
    for j in range(i):
        print("* ",end="")
    print()
for i in range(2,n+1):
    for j in range(n-1):
        print(' ',end="")
    for j in range(i):
        print("* ",end="")
    print()




# 10. HOLLOW SQUARE PATTERN

# for i in range(0,5):
#     for j in range(0,5):
#         if i==0 or i==4 or j==0 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
        
#     print()

# 11.HOLLOW FULL PYRAMID
# 12.HOLLOW INVERTED FULL PYRAMID
# 13.HOLLOW DIAMOND PYRAMID
# 14.FLOYDS TRIANGLE
# a=1
# for i in range(0,4):
#     for j in range(0,i+1):
#         print(a,end=" ")
#         a=a+1
#     print() 


# 15.PASCALS TRIANGLE
# 16.SQUARE OF STAR
# n = 5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" ")
#     print()

# 17.NUMBER SQUARE
# for i in range(0,5):
#     for j in range(1,6):
#         print(i,end=" ")
#     print() 


    



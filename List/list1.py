# list1= [1,2,"Python","Program",15.9]
# list2=["Amy","Ryan","Henry","Emma"]
# print(list1)
# print(list2)

# print(list1[0])
# print(list2[2])

# print(list1[-1])
# print(list2[-3])
# list=["p","r","o","g","i","m"]
# print(list[2:5])
# print(list[5:])
# print(list[:])

# numbers=[21,34,54,12]
# print("before append:",numbers)
# numbers.append(50)
# print("after append:",numbers)

# numbers.insert(3,11)
# print(numbers)
# list2=[2,4,6,8]
# list1.extend(list2)
# print(list1)
# prime_numbers=[2,3,5,7]
# removed_element=prime_numbers.pop(2)
# print('removed element:',removed_element)
# print('updated list:',prime_numbers)

# list1=[12,14,16,18,20]
# l=list1*2
# print(l)
# list2=[9,10,32,54,86]
# l=list1+list2
# print(l)
# a=len(list1)
# print(a)
# -----------------------------------------------------------------------------------
# NESTED LIST(LMS STUDY MATERIAL TASK)

# Create a nested list of 3 shopping lists (groceries, electronics, clothes).
# Try accessing items from each list and modifying them.

# shopping_lists = [
#     ["Rice", "Milk", "Eggs"],          
#     ["Laptop", "Headphones", "Mouse"], 
#     ["Shirt", "Jeans", "Jacket"] ]      

# print("First grocery item:", shopping_lists[0][0])
# print("Second electronic item:", shopping_lists[1][1])
# print("Third clothing item:", shopping_lists[2][2])

# shopping_lists[0][1] = "Almond Milk"   
# shopping_lists[1][0] = "Tablet"        
# shopping_lists[2].append("Shoes")      

# print("Groceries:", shopping_lists[0])
# print("Electronics:", shopping_lists[1])
# print("Clothes:", shopping_lists[2])
# -------------------------------------------------------------------------------
# 1. Generate squares of numbers from 1 to 10 using list comprehension
# squares = [x**2 for x in range(1, 11)]
# print(squares)

# text = "Python Programming is fun!"
# vowels = [ch for ch in text if ch.lower() in "aeiou"]
# print(vowels)
# ------------------------------------------------------------------------------------
# Create a list of 5 of your favorite foods. Use a for loop to print each item with the sentence: ‘I love eating _____.’"
# list=["grapes","apple","banana","pineapple","strawberry"]
# for i in list:
#     print("I Love eating ",i)
# ---------------------------------------------------------------------------------
# Extract all vowels from the string 'Python Programming is fun!
# text = "Python Programming is fun!"
# vowels = "aeiouAEIOU"

# result = [ch for ch in text if ch in vowels]
# print(result)
# ---------------------------------------------------------------------------------------
# Filter out even numbers from a list of integers from 1 to 20
# numbers = list(range(1, 21))
# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)

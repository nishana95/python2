# d={}
# while True:
#     print("1.Add")
#     print("2.Remove")
#     print("3.Display")
#     print("4..exit")

#     choice=int(input("Enter your choice :"))
#     if choice == 4:
#         break
              
#     if choice==1:
#         name=input("Enter your name: ")
#         age=input("Enter your age: ")
#         phone=input("Enter your phone number: ")
#         s={}
#         s["name"]=name
#         s["age"]=age
#         s["phone"]=phone
#         d[phone]=s
#         print(s)
#         print(d)

#     elif choice==2:
#         phone=input("Enter the phone number :")
#         if phone in d:
#             del d[phone]
#             print("Deleted")
#         else:
#             print("Not found")
      
#     elif choice==3:       
#         for i in d:
#             print(d[i])
# ---------------------------------------------------------------------
# Create a dictionary mapping student names to their grades using zip().
# students = ["Alice", "Bob", "Charlie", "Diana"]
# grades = ["A", "B", "A+", "B+"]

# student_grades = dict(zip(students, grades))
# print(student_grades)
# ---------------------------------------------------------------------------
# Combine two lists of numbers using zip() and calculate their sum
# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]

# sum_list = [a + b for a, b in zip(list1, list2)]
# print(sum_list)
# ---------------------------------------------------------------------------
# Unzip a zipped object into individual lists.
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*zipped)

numbers = list(numbers)
letters = list(letters)

print(numbers)
print(letters)
# -------------------------------------------------------------------------

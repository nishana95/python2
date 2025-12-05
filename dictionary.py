d={}
while True:
    print("1.Add")
    print("2.Remove")
    print("3.Display")
    print("4..exit")

    choice=int(input("Enter your choice :"))
    if choice == 4:
        break
              
    if choice==1:
        name=input("Enter your name: ")
        age=input("Enter your age: ")
        phone=input("Enter your phone number: ")
        s={}
        s["name"]=name
        s["age"]=age
        s["phone"]=phone
        d[phone]=s
        print(s)
        print(d)

    elif choice==2:
        phone=input("Enter the phone number :")
        if phone in d:
            del d[phone]
            print("Deleted")
        else:
            print("Not found")
      
    elif choice==3:       
        for i in d:
            print(d[i])
    

    
num = []
while True:
    print("1.add")
    print("2.remove")
    print("3.display")
    print("4.quit")
    choice=int(input("enter choice:"))
    if choice==1:
        add=int(input("integer:"))
        num.append(add)
        if add<0:
            print("invalid input")
        else:
            print("list after adding:",num)
    elif choice==2:
        if len(num)==0:
            print("list is empty")
        else:
            remove=int(input("integer:"))
            if remove not in num:
                print("element not found")
            else:
                num.remove(remove)
                print("list after removing:",remove)
    elif choice==3:
        if len(num)==0:
            print("list is empty")
        else:
            print(num)
    elif choice==4:
        break
    else:
        print("invalid choice:")
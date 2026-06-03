l=[10,20,30,40,50]
while(True):
    print("-"*30)
    print("/n 1. ADD element ")
    print("/n 2. remove element ")
    print("/n 3. display first 3 element ")
    print("/n 4. display last 3 element ")
    print("/n 5. print ")
    print("/n 6. exit /n")
    print("-"*30)

    ch = int(input("enter your choose:"))
    if ch==1:
        e= input("enter an element to add")
        l.append(e)
    elif ch==2:
        if l.count()==0:
            print("list is empty")
        else:
            l.pop(0)
    elif ch==3:
        if l.count()==0:
            print("list is empty")
        else:
            print(l[0:3])
    elif ch==4:
        if l.count()==0:
            print("list is empty")
        else:
            print(l[-1:-4])
    elif ch==5:
        if len(l)==0:
            print("list is empty")
        else:
            print(l)
    elif ch==6:
        break
    else:
        print("enter valid no")
        break
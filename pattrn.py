n = int(input("Enter the range : "))

for i in range(1,(n)):
    for j in range(i,n+1):
        print(" ",end="")
    for j in range(1,i):
        if(j==1):
            print("* ",end="")
        else:
            print("^ ",end="")
    for j in range(1,i+1):
        if(j==i):
            print("* ",end="")
        else:
            print("^ ",end="")
    print("\n")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(i,n):
        if(j==i):
            print("* ",end="")
        else:
            print("^ ",end="")
    for j in range(i,n+1):
        if(j==n):
            print("* ",end="")
        else:
            print("^ ",end="")
    print("\n")

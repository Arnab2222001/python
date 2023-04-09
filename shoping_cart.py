price=[]
p=int(input("enter th number of iteam"))
print("input the price")
total=0
for i in range (p):
    iteam=int(input())
  
    price.append(iteam)
print(price)

for m in price:
    total+=m
print(total)
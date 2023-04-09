numbers=[]
n=int(input("enter the number of input"))
for i in range(n):
    x=input()
    numbers.append(x)
print(numbers)
max=numbers[0]
for  number in numbers:#there the number is number(keyword)
    if number > max:
        max=number
print(max)
real_list = []
prime_list = []
non_prime_list = []
c = 0
n = int(input("Enter the limit : "))

for i in range(0,n):
    el = int(input("Enter the numbers : "))
    real_list.append(el)

for i in range(0,n):
    data = real_list[i]
    for j in range(1,data+1):
        if(j % data == 0):
            c = c+1
    if(c == 2):
        prime_list.append(data)
    else:
        non_prime_list.append(data)

print(prime_list)
print("\n")
print(non_prime_list)
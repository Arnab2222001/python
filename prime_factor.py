def isprime_fector(j):
    for i in range(2, j + 1):
        if (j % i == 0):
            isprime = 1
            for k in range(2, (i // 2 + 1)):
                if (i % k == 0):
                    isprime = 0
                    break

            if (isprime == 1):
                factor.append(i)
                print(factor)


number_count = int(input("enter the number of element: "))
element = []
factor = []
for i in range(number_count):
    p = int(input("enter the number: "))
    element.append(p)
print(element)
for j in element:
    isprime_fector(j)
print()

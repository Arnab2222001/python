import string
import random


def create():

    y = random.choices(string.ascii_uppercase)
    z = random.choices(string.digits)
    x = "".join(random.choices(string.ascii_lowercase +
                string.ascii_lowercase+string.digits+string.digits, k=4))
    q = str(y[0]+z[0]+x)
    return q


list = []
for i in range(50):
    a = create()
    list.append(a)
print("the string started with 'A':-")
count = 0
for j in range(len(list)):

    if (list[j][0] == "A"):
        count = count+1
        print(list[j])

print(count)

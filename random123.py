import random
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(100):
    n = random.randint(101, 200)
    if (n >= 101 and n <= 125):
        count1 = count1+1
    elif (n >= 126 and n <= 150):
        count2 = count2+1
    elif (n >= 151 and n <= 175):
        count3 = count3+1
    elif (n >= 176 and n <= 200):
        count4 = count4+1
print("101-125 :", count1)
print("126-150 :", count2)
print("151-175 :", count3)
print("176-200 :", count4)

import random

serect_number=(random.randint(0,100))
print(serect_number)
i=0
print("you have three chance")
while i<3:
    p=int(input("enterthe number: "))
    i=i+1
    if p==serect_number:
     print("yes you guess is right")
     break
    if p>serect_number:
      print("plese enter smaller number than this")
    if p<serect_number:
        print("please enter a big number than this")
    else:
        print("the guess is wrong")
print("all chance are gone")
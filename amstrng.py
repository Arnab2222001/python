
# Program to check Armstrong numbers in a certain interval
low = 1
upper = 500

for num in range(low, upper+1):

   order = len(str(num))
   sum=0
   temp=num
   while (temp> 0):
      digit = temp % 10
      sum += digit**order
      temp//=10

   if(num==sum):
      print(num)


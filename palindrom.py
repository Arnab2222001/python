def isoddpalindrome(string):
    size = len(string)
    if (size % 2 == 0):
        return 0

    if (string == string[::-1]):
        return "1"


number_of_input = int(input("entr the number of input:"))
list = []
for i in range(number_of_input):
    p = input("enter the number: ")
    x = p.upper()
    if (isoddpalindrome(x) == "1"):
        list.append(p)
print(list)

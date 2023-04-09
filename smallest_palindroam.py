pal_list = []
word_list = []
n = int(input("Enter the size of the list : "))
for i in range(n):
    string = input("Enter the words : ")
    word_list.append(string)

small_len = 100
for element in word_list:
    size = 0
    if (element == element[::-1]):
        pal_list.append(element)
        size = len(element)
        if (size <= small_len):
            small_len = size
            small_palindrome = element

print(pal_list)
print("Smallest element is : "+small_palindrome)
print("Length is : "+str(small_len))

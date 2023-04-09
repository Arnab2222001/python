file_name = input("Enter the file name : ")
document = file_name+".txt"
f = open(document, "a")
sentence = input("Write something : ")
f.write(" "+sentence)
f.close()

file = open(document, "r")
for line in file:
    string = line.lower().replace(",", "").replace(".", "").split()

k = int(input("Enter the frequency of appearing : "))
word_set = set(string)

for i in word_set:
    count = 0
    for j in string:
        if (i == j):
            count = count + 1
    if (k == count):
        print(str(k)+" times appearing word is : "+str(i))
file.close()

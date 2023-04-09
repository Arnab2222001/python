
def vowel(wordsort):
    count = 0
    for i in wordsort:

        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "o" or i == "u"):
            count = count+1
    return count


sentence = input("enterthe sentence: ")
word = sentence.split()
wordsort = sorted(sentence.split())
print(wordsort)
for j in wordsort:
    print(j, vowel(j))

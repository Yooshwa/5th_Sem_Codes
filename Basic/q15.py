# Write a program to take input for a sentence and sort the words according to their length.

sentence=input("Enter a sentence: ")

words=sentence.split()

words.sort(key=len)

print("Words Sorted by Length")

for word in words:
    print(word,end=' ')

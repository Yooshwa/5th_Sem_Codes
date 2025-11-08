# Write a program to count the frequency of each word in a sentence and remove duplicate words.

sentence=input("Enter a sentence: ")

words=sentence.split()

word_count={}

for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

print("Word Frequencies: ")

for word, count in word_count.items():
    print(word,":",count)

unique_words= list(word_count.keys())

print("Sentence without Duplicates: ")
print(" ".join(unique_words))
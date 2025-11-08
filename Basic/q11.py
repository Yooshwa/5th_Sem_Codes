# Write a program to check if a word is a palindrome.

word=str(input("Enter a word: "))
rev=''
for char in (word):
    rev = rev + char
if rev == word:
    print("Is a palindrome")
else:
    print("Not a Palindorme")
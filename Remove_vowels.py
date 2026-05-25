#Remove Vowels
word = input()
no_vowel =""
for letter in word:
	if letter not in "aeiou":
		no_vowel += letter 
print(no_vowel)

word = input("Enter a word: ").lower() # Convert to lowercase to ignore casing

is_palindrome = True
length = len(word)

# only need to loop halfway through the word
for i in range(length // 2):
	# Compare letter at the front [i] with the matching letter at the back [-1 - i]
	if word[i] != word[length - 1 - i]:
		is_palindrome = False
		break  # Exit early if a mismatch is found

if is_palindrome:
	print("It is a palindrome!")
else:
	print("It is not a palindrome.")

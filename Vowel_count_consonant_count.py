# vowel_count and consonant_count
word = input()
v_count = 0
c_count = 0
for letter in word:
	if letter in "aeiou":
	   v_count = v_count +1
	else:
	   c_count = c_count +1
   
print("vowel",v_count, "consonant", c_count)

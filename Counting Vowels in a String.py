#Counting Vowels in a String

text = input("Enter a text:")
vowels = "aeiou"
vowel_count =0

for char in text:
    if char in vowels:
        vowel_count += 1
print("The numbers of vowels is:" , vowel_count )        

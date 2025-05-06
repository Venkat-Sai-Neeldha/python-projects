#  Reverse a string
str1="hello"
print(str1[::-1])

#Check if a string is a palindrome
str2="madam"
if str2==str2[::-1]:
    print("palindrome")
else:
    print("not palindrome")

#Count vowels and consonants in a string

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowelcount = 0
consonantcount = 0
str4 = "python"

for i in str4:
    if i.isalpha():
        if i in vowels:
            vowelcount += 1
        else:
            consonantcount += 1

print(f"Number of vowels: {vowelcount} and number of consonants: {consonantcount}")


#Find the frequency of each character
text = "aabbcc"
dict1 = {}

for char in text:
    dict1[char] = dict1.get(char, 0) + 1

print(dict1)

#Remove all whitespaces from a string
text = " a b c "
text = text.replace(" ", "")
print(text)

#Replace a word in a sentence

str5="i like java"
str5=str5.replace("java", "python")
print(str5)

#Extract digits from a string

str6 = "abc123def"
str7 = "".join([char for char in str6 if char.isnumeric()])
print(str7)

#Check if a string contains only alphabets
str8="Hello123"
print(str8.isalpha())

#Capitalize the first letter of each word
str9="hello world"
print(str9.title())
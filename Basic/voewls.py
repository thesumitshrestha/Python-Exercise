# Write a Python program to test whether a passed letter is a vowel or not

def check_vowels(char):
    vowel = 'aeiou'
    return char in vowel

print(check_vowels('c'))
print(check_vowels('e'))
print(check_vowels('d'))

count_vowels = 0
count_consonant = 0
variable = input("enter any string values:")
vowls = 'AEIOUaeiou'

for i in variable:
    if i in vowels:
        count_vowels +=1
    else:
        count_consonant +=1
print("count vowels:",count_vowels)
print("count consonants:",count_consonant)

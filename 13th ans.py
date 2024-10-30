str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

if len(str1) != len(str2):
    print("Not anagrams")
else:
    if sorted(str1) == sorted(str2):
        print("Strings are anagrams")
    else:
        print("Not anagrams")

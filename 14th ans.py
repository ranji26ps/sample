def longest_name(names):
    if not names:
        return None
    
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest

name_list = ["aruna", "arun", "arun kumar"]
print(longest_name(name_list))

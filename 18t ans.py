def count_characters(input_string):
    letters_count = 0
    digits_count = 0
    special_symbols_count = 0

    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1
        elif not char.isspace():  
            special_symbols_count += 1

    return letters_count, digits_count, special_symbols_count


input_string = input("Enter a string: ")
letters, digits, special_symbols = count_characters(input_string)

print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Symbols: {special_symbols}")

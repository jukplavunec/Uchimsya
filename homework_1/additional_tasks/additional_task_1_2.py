def is_palindrom(string_to_check):
    return string_to_check == string_to_check[::-1]


print(is_palindrom('palindrom_mordnilap'))  # prints True

print(is_palindrom('palindrom'))  # prints False

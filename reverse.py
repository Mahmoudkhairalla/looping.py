def reverse_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

user_input = input("Enter a string: ")
reversed_input = reverse_string(user_input)
print("Reversed string:", reversed_input)

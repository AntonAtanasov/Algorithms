def is_palindrome(obj):
    obj = list(str(obj))
    obj_reversed = obj[::-1]

    return obj == obj_reversed


def generate_rotations(string):
    letters = list(string)
    string_rotations = []
    counter = len(letters)

    temp = letters
    while counter != 0:
        current_letter = temp.pop(0)
        temp.append(current_letter)
        string = "".join(temp)
        string_rotations.append(string)
        counter -= 1

    return string_rotations


def get_rotated_palindromes(string_rotations):
    is_empty = True

    for word in string_rotations:
        if is_palindrome(word) is True:
            print(word)
            is_empty = False

    if is_empty is True:
        print("NONE")


string = input("Enter your string: ")
rotations = generate_rotations(string)
get_rotated_palindromes(rotations)

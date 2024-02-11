str = input("Give a Name : ")
rev_str = ""

for char in str:
    rev_str = char+rev_str

if str == rev_str:
    print(str, "is a palindrome")
else:
    print(str, "is not a palindrome")

########################################################################################################
########################################################################################################
    
def is_palindrome(input_str):
    rev_str = ""

    for char in input_str:
        rev_str = char+rev_str
    return input_str == rev_str

user_input = input("Give a Name : ")

if is_palindrome(user_input):
    print(user_input, "is a Palindrome")
else:
    print(user_input, "is not a palindrome")

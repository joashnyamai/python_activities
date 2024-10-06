#Python palindrome
def is_palindrome(s):
    # Remove any spaces and convert to lowercase for accurate comparison
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get user input
user_input = input("Enter a string: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")

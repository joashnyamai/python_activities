#Python get_even_numbers
def get_even_numbers(lst):
    # Use list comprehension to filter even numbers
    return [num for num in lst if num % 2 == 0]

# Get user input
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert user input into a list of integers
numbers = [int(num) for num in user_input.split()]

# Get the even numbers
even_numbers = get_even_numbers(numbers)

# Print the result
print("The even numbers are:", even_numbers)
# Import the datetime module to work with dates
from datetime import datetime

# Define a function to calculate the fine for a book
def calculate_fine(bookID, due_date, return_date):
    # Convert the due date and return date strings to datetime objects
    due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
    return_date_obj = datetime.strptime(return_date, '%Y-%m-%d')
    
    # Calculate the number of days the book is overdue
    # Use the max function to ensure the result is not negative
    overdue_days = max(0, (return_date_obj - due_date_obj).days)
    
    # Determine the fine rate based on the number of days overdue
    # Use a conditional expression to simplify the calculation
    fine_rate = 20 if overdue_days <= 7 else 50 if overdue_days <= 14 else 100
    
    # Calculate the total fine amount
    fine_amount = overdue_days * fine_rate
    
    # Print the results
    print(f"Book ID: {bookID}")
    print(f"Due Date: {due_date}")
    print(f"Return Date: {return_date}")
    print(f"Days Overdue: {overdue_days}")
    print(f"Fine Rate (per day): Ksh. {fine_rate}")
    print(f"Total Fine Amount: Ksh. {fine_amount}")

# Check if the script is being run directly (not being imported)
if __name__ == "__main__":
    # Get the book ID, due date, and return date from the user
    bookID = input("Enter Book ID: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    return_date = input("Enter Return Date (YYYY-MM-DD): ")
    
    # Call the calculate_fine function with the user's input
    calculate_fine(bookID, due_date, return_date)
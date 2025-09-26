from datetime import datetime, date

def days_until_birthday(month, day):
    """
    Calculate how many days are left until someone's next birthday.
    
    Args:
        month (int): Birth month (1-12)
        day (int): Birth day (1-31)
    
    Returns:
        int: Number of days until the birthday
    """
    # Get today's date
    today = date.today()
    
    # Create a date object for the birthday in the current year
    current_year = today.year
    birthday_this_year = date(current_year, month, day)
    
    # If the birthday has already passed this year, calculate it for next year
    if birthday_this_year < today:
        birthday_next_year = date(current_year + 1, month, day)
        days_until = (birthday_next_year - today).days
    else:
        days_until = (birthday_this_year - today).days
    
    return days_until

def birthday_message(name, month, day):
    """
    Generate a birthday message with days until the birthday.
    
    Args:
        name (str): Person's name
        month (int): Birth month (1-12)  
        day (int): Birth day (1-31)
    
    Returns:
        str: Birthday message
    """
    days = days_until_birthday(month, day)
    
    if days == 0:
        return f"Hello {name}! Happy Birthday! Today is your special day!"
    elif days == 1:
        return f"Hello {name}! Your birthday is tomorrow!"
    else:
        return f"Hello {name}! Your birthday is in {days} days"

# Example usage:
if __name__ == "__main__":
    # Test the functions
    print("=== Birthday Calculator ===")
    
    # Example 1: Jason's birthday (you can change these values)
    jason_days = days_until_birthday(12, 25)  # December 25th
    print(f"Days until Jason's birthday: {jason_days}")
    
    # Example 2: Using the message function
    message = birthday_message("Jason", 12, 25)
    print(message)
    
    # Interactive version
    print("\n=== Try it yourself ===")
    try:
        name = input("Enter name: ")
        month = int(input("Enter birth month (1-12): "))
        day = int(input("Enter birth day (1-31): "))
        
        result = birthday_message(name, month, day)
        print(result)
        
    except ValueError:
        print("Please enter valid numbers for month and day!")
    except Exception as e:
        print(f"An error occurred: {e}")
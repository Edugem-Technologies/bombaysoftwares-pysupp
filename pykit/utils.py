from datetime import datetime,timedelta
from time import time
import random, re, string
from random import randint

def str_to_bool(s):
    """
    Converts a string to a boolean value.

    The function checks if the stripped and lowercase version of the string is 'true' or 'false'.
    If it matches 'true', the function returns boolean True.
    If it matches 'false', the function returns boolean False.
    Otherwise, it returns None.

    Parameters:
        s (str): The input string to be converted to a boolean value.

    Returns:
        bool or None: The converted boolean value if the string is 'true' or 'false'. Otherwise, None.

    Example:
        >>> str_to_bool('True')
        True
        >>> str_to_bool('False')
        False
        >>> str_to_bool('invalid')
        None

    """
    if s.strip().lower() == 'true': # If the stripped and lowercase string is 'true'
        return True # Return boolean True
    elif s.strip().lower() == 'false': # If the stripped and lowercase string is 'false'
        return False # Return boolean False
    else: 
        return None # Return None if the string is neither 'true' nor 'false'

def format_email(email):
    """
    Formats an email address.

    This function takes an email address as input and performs the following operations:
        - If the email is not empty or None, it removes leading and trailing whitespace and converts it to lowercase.
        - If the email is empty or None, it returns the email as it is.

    Parameters:
        email (str): The email address to be formatted.

    Returns:
        str: The formatted email address, or the original email if it is empty or None.

    Example:
        >>> format_email("  john@example.com ")
        'john@example.com'
        >>> format_email("MARY@example.com")
        'mary@example.com'
        >>> format_email("")
        ''
        >>> format_email(None)
        None

    """
    if email:  # If the email is not empty or None
        return email.strip().lower() # Remove leading/trailing whitespace and convert to lowercase
    return email # Return the email as it is if it is empty or None

def is_invalid(value):
    """
    Checks if a value is considered invalid.

    This function checks if the string representation of the value, after stripping leading and trailing whitespace,
    matches any of the predefined invalid values: "", None, "None", "null", or "undefined". If a match is found,
    it returns True, indicating that the value is invalid. Otherwise, it returns False.

    Parameters:
        value: The value to be checked.

    Returns:
        bool: True if the value is considered invalid, False otherwise.

    Example:
        >>> is_invalid("")
        True
        >>> is_invalid(None)
        True
        >>> is_invalid("null")
        True
        >>> is_invalid("valid")
        False

    """
    if str(value).strip() in ["", None, "None", "null", "undefined"]:
        return True # If the stripped string value is empty or matches any of the invalid values, return True
    return False # Otherwise, return False

def get_current_year():
    """
    Retrieves the current year.

    This function uses the datetime module's datetime.now() method to retrieve the current date and time.
    The year component is extracted from the current date and time, and it is returned as the current year.

    Returns:
        int: The current year.

    Example:
        >>> get_current_year()
        2023

    """
    return datetime.now().year

def generate_otp():
    """
    Generates a random OTP (One-Time Password).

    This function generates a random OTP (One-Time Password) consisting of a four-digit number.
    The generated OTP is returned.

    Returns:
        int: The generated OTP.

    Example:
        >>> generate_otp()
        4567
        >>> generate_otp()
        1234

    """
    return random.randint(1000, 9999)

def convert_date_of_birth_to_datetime(date_string):
    """
    Converts a date string to a datetime object.

    This function takes a date string in the format '%m/%d/%Y' as input and converts it to a datetime object.
    If the conversion is successful, the datetime object is returned.
    If an exception occurs during the conversion, the function returns False.

    Args:
        date_string (str): The date string to be converted.

    Returns:
        datetime or bool: The converted datetime object if successful, False otherwise.
    
    Example:
        >>> convert_date_of_birth_to_datetime('05/15/1990')
        1999-05-25 00:00:00
        >>> convert_date_of_birth_to_datetime('2022-01-01')
        False

    """
    try:
        date_time_obj = datetime.strptime(date_string, '%m/%d/%Y')
        return date_time_obj
    except Exception as e:
        return False

def convert_time(seconds):
    """
    Converts a given number of seconds to hours, minutes, and seconds.

    This function takes a number of seconds as input and converts it to hours, minutes, and seconds.
    The converted values are returned as a tuple of hours, minutes, and seconds.

    Args:
        seconds (int): The number of seconds to be converted.

    Returns:
        tuple: A tuple containing the converted values of hours, minutes, and seconds.

    Example:
        >>> convert_time(3660)
        (1, 0, 0)
        >>> convert_time(12345)
        (3, 25, 45)

    """
    hours = seconds // 3600 # Calculate the number of hours
    seconds %= 3600 # Update the remaining seconds after calculating hours
    minutes = seconds // 60 # Calculate the number of minutes
    seconds %= 60 # Update the remaining seconds after calculating minutes
    return hours, minutes, seconds

def file_name_to_readable_name(file_name):
    """
    Converts a file name to a readable name.

    This function takes a file name as input and performs the following transformations to make it readable:
        - Split the file name by the dot (.) and keep only the first part.
        - Replace any hyphens (-) with spaces.
        - Remove any non-alphabetic characters except spaces.
        - Capitalize the first letter of the resulting name and remove leading/trailing spaces.

    Args:
        file_name (str): The file name to be converted.

    Returns:
        str: The converted readable name.

    Example:
        >>> file_name_to_readable_name("my-file-name.txt")
        'My file name'
        >>> file_name_to_readable_name("another_example.pdf")
        'Another example'

    """
    file_name = file_name.split('.')[0] # Split the file name by the dot and keep only the first part
    file_name = file_name.replace('-', ' ') # Replace hyphens with spaces
    return ("".join(re.split("[^a-zA-Z\s]*", file_name))).capitalize().strip() # Remove non-alphabetic characters except spaces, Capitalize the first letter and remove leading/trailing spaces

def get_body_mass_index(weight, height):
    """
    Calculates the Body Mass Index (BMI) based on weight and height.

    This function takes weight and height as input and calculates the Body Mass Index (BMI) using the formula:
        BMI = weight / ((height * height) / 10000)

    Args:
        weight (int): The weight of a person in kilograms.
        height (int): The height of a person in centimeters.

    Returns:
        float: The calculated Body Mass Index (BMI) rounded to 2 decimal places.
        If weight or height is missing or not of integer type, it returns 0.

    Example:
        >>> get_body_mass_index(70, 170)
        24.22
        >>> get_body_mass_index(80, 180)
        24.69

    """
    if weight and height and isinstance(weight, int) and isinstance(height, int):
        # Check if weight and height are provided and of integer type
        # Calculate the BMI using the provided weight and height
        return round(weight / ((height * height) / 10000), 2)
    return 0

def is_number(string):
    """
    Checks if a string can be converted to an integer.

    This function takes a string as input and attempts to convert it to an integer using the `int()` function.
    If the conversion is successful, it returns True, indicating that the string is a valid number.
    If the conversion raises a ValueError, it returns False, indicating that the string is not a valid number.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string can be converted to an integer, False otherwise.

    Example:
        >>> is_number('123')
        True
        >>> is_number('abc')
        False
        >>> is_number('-123')
        True

    """
    try:
        int(string) # Attempt to convert the string to an integer
        return True # Return True if the conversion is successful
    except ValueError:
        return False # Return False if the conversion raises a ValueError

def days_to_seconds(days):
    """
    Convert days to seconds.

    This function takes the number of days as input and converts it to an equivalent number of seconds.

    Parameters:
        days (int): Number of days to be converted.

    Returns:
        int: Number of seconds equivalent to the provided number of days.

    Example:
        >>> days = 5
        >>> days_to_seconds(days)
        432000

    """
    seconds = 86400 * days # Convert days to seconds (1 day = 24 hours * 60 minutes * 60 seconds)
    return seconds

def generate_random_string(length):
    """
    Generate a random string of a given length.

    This function generates a random string consisting of lowercase alphabets of the specified length. If the length is negative integer it will return 0

    Parameters:
        length (int): Length of the random string to be generated.

    Returns:
        str: Random string of the specified length.

    Example:
        >>> length = 10
        >>> generate_random_string(length)
        'abcdefghij'

    """
    if (length <= 0):
        return 0
    else:
        random_string_length = length
        res = ''.join(random.choices(string.ascii_lowercase, k=random_string_length)) # Generate a random string of lowercase alphabets
        return res

def generate_random_number_string(length):
    """
    Generate a random string of numbers of a given length.

    This function generates a random string consisting of numbers of the specified length. If the length is negative integer it will return 0

    Parameters:
        length (int): Length of the random number string to be generated.

    Returns:
        str: Random string of numbers of the specified length.

    Example:
        >>> length = 6
        >>> generate_random_number_string(length)
        '123456'

    """
    if (length <= 0):
        return 0
    else:
        random_string_length = length
        res = ''.join(random.choices('123456789', k=random_string_length)) # Generate a random string of numbers
        return res

def random_with_n_digits(length):
    """
    Generate a random number with a specified number of length. If the length is negative integer it will return 0

    This function generates a random number with the specified number of digits.

    Parameters:
        num (int): Number of digits in the random number.

    Returns:
        int: Random number with the specified number of length.

    Example:
        >>> num = 5
        >>> random_with_n_digits(length)
        48297

    """
    if (length <= 0):
        return 0
    else:
        range_start = 10 ** (length - 1) # Calculate the minimum possible value based on the number of digits
        range_end = (10 ** length) - 1 # Calculate the maximum possible value based on the number of digits
        return randint(range_start, range_end) # Generate a random number within the specified range

def check_is_not_none_or_empty(object):
    """
    Check if the object is not None or empty.

    Args:
        obj (object): The object to check.

    Returns:
        bool: True if the object is not None or empty, False otherwise.

    Example:
        result = check_is_not_none_or_empty("Hello")
        print(result)
        # Output: True

    """
    if object is None:
        return False
    if isinstance(object, str) and object == '':
        return False
    if isinstance(object, list) and object == []:
        return False
    return True

def format_inr(number):
    """
    Format a number as Indian Rupees (INR).

    This function takes a number as input and formats it as Indian Rupees (INR) with the following conventions:
        - The number is divided into groups of two digits from the right.
        - Each group is separated by a comma.
        - The formatted number is prefixed with the "₹" symbol.

    Parameters:
        number (int or float): The number to be formatted as INR.

    Returns:
        str: The formatted INR string.

    Example:
        >>> format_inr(1234567.89)
        '₹ 12,34,567.89'
        >>> format_inr(-9876543)
        '₹ -98,76,543'

    """
    s, *d = str(abs(number)).partition(".") # Separate the integer and decimal parts of the absolute value of the number
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]]) # Format the integer part with commas
    if number < 0:
        formatted_number = "₹ " + "-" + "".join([r] + d)  # Add the negative sign for negative numbers
    else:      
        formatted_number = "₹ " + "".join([r] + d) # Prefix the formatted number with "₹" symbol and rejoin the integer and decimal parts

    return formatted_number

def aadhaar_format(aadhar_number):
    """
    Format an Aadhaar number by adding spaces every four digits.

    This function takes an Aadhaar number as input and adds spaces every four digits to improve readability.

    Parameters:
        aadhar_number (str): The Aadhaar number to be formatted.

    Returns:
        str: The formatted Aadhaar number.

    Example:
        >>> aadhaar_format("123456789012")
        '1234 5678 9012'

    """
    aadhar_number = aadhar_number.replace(" ", "") # Remove any existing spaces in the Aadhaar number
    correct_aadhaar_number = [aadhar_number[i:i+4] for i in range(0, len(aadhar_number), 4)] # Split the Aadhaar number into groups of four digits
    return ' '.join(correct_aadhaar_number) # Join the groups of digits with spaces in between

def format_datetime(dt, fmt='%Y-%m-%d %H:%M:%S'):
    """
    Format a datetime object as a string using the specified format.

    This function takes a datetime object and formats it as a string using the specified format. The default format is '%Y-%m-%d %H:%M:%S'.

    Parameters:
        dt (datetime): The datetime object to be formatted.
        fmt (str): The format string. Default is '%Y-%m-%d %H:%M:%S'.

    Returns:
        str: The formatted datetime string.

    Example:
        >>> from datetime import datetime
        >>> dt = datetime(2022, 1, 15, 10, 30, 0)
        >>> format_datetime(dt, '%Y/%m/%d %I:%M %p')
        '2022/01/15 10:30 AM'

    """
    return dt.strftime(fmt)

def get_time_duration(start_date,end_date):
    """
    Calculate the time duration between two dates.

    This function takes two datetime objects, `start_date` and `end_date`, and calculates the time duration between them in days, hours, and minutes.

    Parameters:
        start_date (datetime): The start date and time.
        end_date (datetime): The end date and time.

    Returns:
        str: The formatted time duration in days, hours, and minutes.

    Example:
        >>> from datetime import datetime
        >>> start = datetime(2022, 1, 1, 10, 0, 0)
        >>> end = datetime(2022, 1, 3, 12, 30, 0)
        >>> get_time_duration(start, end)
        '2 days, <br>2 hours, <br>30 minutes'

    """
    diff = end_date - start_date
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60

    return "{days} days, <br>{hours} hours, <br>{minutes} minutes".format(days=days, hours=hours, minutes=minutes)

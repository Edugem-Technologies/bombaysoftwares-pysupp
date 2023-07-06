import random, re, string, uuid, jwt, math, pytz
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from time import time
from random import randint
from hashids import Hashids
from slugify import slugify

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
    return ("".join(re.split("[^a-zA-Z\\s]*", file_name))).capitalize().strip() # Remove non-alphabetic characters except spaces, Capitalize the first letter and remove leading/trailing spaces

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

def get_api_key():
    """
    Generate and return a new API key using UUID.

    This function generates a new API key using the UUID (Universally Unique Identifier) library.
    It returns the generated API key as a UUID object.

    Returns:
        UUID: The generated API key.

    Example:
        >>> get_api_key()

    """
    return uuid.uuid4() # Generate and return a new UUID as the API key

def generate_slug_by_org_id(title, org_id):
    """
    Generate a slug by combining a title and organization ID.

    This function takes a title and organization ID as input, and generates a slug by combining them.
    The generated slug is converted to lowercase and any whitespace is replaced with hyphens.

    Args:
        title (str): The title to be included in the slug.
        org_id (int or str): The organization ID to be included in the slug.

    Returns:
        str: The generated slug.

    Example:
        >>> generate_slug_by_org_id('Hello World', 123)
        'hello-world-123'

    """
    title = str(title).strip() # Remove leading/trailing whitespace from the title
    slug = title.lower() + '-' + str(org_id) # Combine the lowercase title and organization ID with a hyphen
    slug = re.sub(' +', '-', slug) # Replace any whitespace with hyphens
    return slug

class InputValidation:
    """
    A class for input validation patterns and methods.

    Example:
        # Validating a string using a specific pattern
        string = "HelloWorld123"
        if InputValidation.is_valid(string, InputValidation.ALPHA_NUMERIC):
            print("String is valid!")
        else:
            print("String is not valid!")

    """
    STRING = '^[a-zA-Z]+$' # Matches strings with only alphabetic characters
    STRING_SPACE = '^[a-zA-Z\\s]+$' # Matches strings with alphabetic characters and spaces
    STRING_UPPERCASE = '^[A-Z]+$' # Matches strings with only uppercase alphabetic characters
    STRING_UPPERCASE_SPACE = '^[A-Z\\s]+$' # Matches strings with uppercase alphabetic characters and spaces
    STRING_LOWERCASE_SPACE = '^[a-z\\s]+$'  # Matches strings with lowercase alphabetic characters and spaces
    NUMERIC = '^[1-9][0-9]*$' # Matches positive integers
    ALPHA_NUMERIC = '^[A-Za-z0-9]+$' # Matches alphanumeric strings
    ALPHA_NUMERIC_SPACE = '^[A-Za-z0-9\\s]+$' # Matches alphanumeric strings with spaces
    MOBILE_NUMBER = '^[0-9]{10}+$' # Matches 10-digit mobile numbers
    EMAIL = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$' # Matches valid email addresses
    ALPHA_NUMERIC_SPACE_DASH = '^[-A-Za-z0-9\\s]+$' # Matches alphanumeric strings with spaces and dashes

    @classmethod
    def is_valid(cls, string, validation_type):
        """
        Validate if the given string matches the specified validation type.

        Args:
            string (str): The string to be validated.
            validation_type (str): The validation type to match against.

        Returns:
            bool: True if the string matches the validation type, False otherwise.

        """
        return bool(re.fullmatch(validation_type, str(string)))

def datetime_from_utc_to_local(utc_datetime):
    """
    Converts a datetime object from UTC to the local timezone.

    This function takes a datetime object in UTC and converts it to the local timezone.
    It calculates the offset between the local timezone and UTC based on the current timestamp.
    The offset is then added to the UTC datetime object to obtain the corresponding local datetime.

    Args:
        utc_datetime (datetime): The datetime object in UTC.

    Returns:
        datetime: The datetime object converted to the local timezone.

    Example:
        >>> utc_dt = datetime(2022, 3, 15, 10, 30, 0)
        >>> local_dt = datetime_from_utc_to_local(utc_dt)
        >>> local_dt
        2022-03-15 10:30:00

    """
    now_timestamp = time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

def encode_jwt_token(data, JWT_SECRET_KEY):
    """
    Encodes data into a JWT token using the specified secret key.

    This function takes a dictionary `data` and a `JWT_SECRET_KEY` as input and encodes the data into a JWT token.
    The encoded token is returned.

    Args:
        data (dict): The data to be encoded into the JWT token.
        JWT_SECRET_KEY (str): The secret key used for encoding the token.

    Returns:
        str: The encoded JWT token.

    Example:
        >>> data = {"user_id": 123, "role": "admin"}
        >>> JWT_SECRET_KEY = "mysecretkey"
        >>> encode_jwt_token(data, JWT_SECRET_KEY)
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInJvbGUiOiJhZG1pbiJ9.H2jxN8d_WBbs83n_5tYnq2sblYs'

    """
    return jwt.encode(data, JWT_SECRET_KEY)

def decode_jwt_token(encoded_jwt, JWT_SECRET_KEY):
    """
    Decodes a JWT token using the specified secret key.

    This function takes an encoded JWT token `encoded_jwt` and a `JWT_SECRET_KEY` as input and decodes the token.
    The decoded token containing the original data is returned.

    Args:
        encoded_jwt (str): The encoded JWT token to be decoded.
        JWT_SECRET_KEY (str): The secret key used for decoding the token.

    Returns:
        dict: The decoded JWT token containing the original data.

    Example:
        >>> encoded_jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInJvbGUiOiJhZG1pbiJ9.H2jxN8d_WBbs83n_5tYnq2sblYs'
        >>> JWT_SECRET_KEY = "mysecretkey"
        >>> decode_jwt_token(encoded_jwt, JWT_SECRET_KEY)
        {'user_id': 123, 'role': 'admin'}

    """

    return jwt.decode(encoded_jwt, JWT_SECRET_KEY, algorithms=["HS256"])

def encrypt_value(value, hashid_salt):
    """
    Encrypt a non-negative integers value using Hashids and return the encoded Hashid.

    This function encrypts a given value using the specified salt and minimum length.
    If a valid value is provided, it returns the encoded Hashid; otherwise, it returns None.

    Args:
        value(int): The value to encrypt.

    Returns:
        str or None: The encoded Hashid if a valid value is provided, None otherwise.

    Example:
        >>> encrypt_value(12345)

    """
    if value:
        try:
            _hashids = Hashids(hashid_salt, min_length=10)
            encoded_val = _hashids.encode(value) # Encode the value into a Hashid
            if encoded_val:
                return encoded_val # Return the encoded Hashid
        except Exception as e:  # type: ignore  # noqa: F841
            pass
    return None # Return None if no valid value or encoded Hashid is found

def decrypt_hashid(hashval, hashid_salt):
    """
    Decrypt a Hashid and return the decoded value.

    This function decrypts a given Hashid using the specified salt and minimum length.
    If a valid Hashid is provided, it returns the decoded value; otherwise, it returns None.

    Args:
        hashval (str): The Hashid to decrypt.

    Returns:
        int or None: The decoded value if a valid Hashid is provided, None otherwise.

    Example:
        >>> decrypt_hashid("LX9znW34ab")

    """
    if hashval:
        _hashids = Hashids(hashid_salt, min_length=10)
        decoded_val = _hashids.decode(hashval) # Decode the Hashid
        if decoded_val:
            return decoded_val[0] # Return the decoded value
    return None # Return None if no valid Hashid or decoded value is found

def get_pagination_meta(current_page, page_size, total_items):
    """
    Generate pagination metadata for frontend.

    Args:
        current_page (int): The current page number.
        page_size (int): The number of items per page.
        total_items (int): The total number of items.

    Returns:
        dict: Pagination metadata.

    Example:
        pagination_meta = get_pagination_meta(current_page=2, page_size=10, total_items=100)
        print(pagination_meta)
        # Output: {
        #     'current_page': 2,
        #     'page_size': 10,
        #     'total_items': 100,
        #     'total_pages': 10,
        #     'has_next_page': True,
        #     'has_previous_page': True,
        #     'next_page': 3,
        #     'previous_page': 1
        # }

    """
    if page_size:
        total_pages = math.ceil(total_items / page_size)
        has_next_page = current_page < total_pages
        has_previous_page = current_page > 1
        next_page = current_page + 1 if has_next_page else None
        previous_page = current_page - 1 if has_previous_page else None
    else:
        # If page_size is not provided, treat the current_page as the total_pages
        total_pages = current_page
        has_next_page = None
        has_previous_page = None
        next_page = None
        previous_page = None
        page_size = None

    return {
        'current_page': current_page,
        'page_size': page_size,
        'total_items': total_items,
        'total_pages': total_pages,
        'has_next_page': has_next_page,
        'has_previous_page': has_previous_page,
        'next_page': next_page,
        'previous_page': previous_page
}

def monthdelta(date, delta):
    """
    Add or subtract a specified number of months to/from a given date.

    This function calculates a new date by adding or subtracting the specified number of months to/from the given date.
    It takes into account the varying number of days in each month and handles leap years correctly.

    Args:
        date (datetime.date): The date to which the months should be added or subtracted.
        delta (int): The number of months to add (if positive) or subtract (if negative).

    Returns:
        datetime.date: The resulting date after adding or subtracting the specified number of months.

    Example:
        >>> input_date = datetime(2022, 3, 15)
        >>> delta_months = 2
        >>> result_date = monthdelta(input_date, delta_months)
        >>> result_date
        2022-05-15

    """
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12
    if not m:
        m = 12
    d = min(date.day, [31, 29 if y % 4 == 0 and (not y % 100 == 0 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return datetime(year=y, month=m, day=d)

def format_time_utc_to_est(datetime_object, datetime_format = '%Y-%m-%d %I:%M:%S %p'):
    """
    Convert a UTC datetime object to Eastern Standard Time (EST) and format it as a string.

    Args:
        datetime_object (object): The UTC datetime object to convert.
        datetime_format (str): The format string for the output datetime. Defaults to '%Y-%m-%d %I:%M:%S %p'.

    Returns:
        str: The formatted datetime string in EST.

    Example:
        utc_time = datetime.datetime(2023, 6, 29, 10, 30, 0)
        formatted_time = format_time_utc_to_est(utc_time)
        print(formatted_time)
        # Output: '2023-06-29 06:30:00 AM'

    """
    est = pytz.timezone('US/Eastern') # Define the Eastern Standard Time (EST) timezone
    utc = pytz.utc # Define the UTC timezone
    fmt = datetime_format # Define the format string for the output datetime
    formatted_datetime_string = utc.localize(
        datetime_object).astimezone(est).strftime(fmt)
    return formatted_datetime_string  

def get_slug(string):
    """
    Generates a slug for a given string.

    This function generates a unique timestamp by converting the current time to a string and extracting the 0'th index.
    The original string and the unique timestamp are then concatenated, and the resulting string is slugified.
    The slug is returned as the result.

    Parameters:
        string (str): The original string to generate a slug from.

    Returns:
        str: The generated slug.

    Example:
        >>> get_slug('Hello, World!')
        'hello-world-1629937512'

    """
    unique_timestamp = str(time()).split(".")[0] # Generate a unique timestamp by converting the current time to a string and extracting the 0'th index.
    return slugify(f"{string} {unique_timestamp}") # Concatenate the original string and the unique timestamp, and then slugify the resulting string

def convert_seconds_to_time(seconds):
    """
    Converts a given number of seconds to a formatted time string.

    This function takes a number of seconds as input and converts it to a formatted time string in the format "%Y-%m-%d %H:%M:%S".
    The converted time string is returned.

    Args:
        seconds (int): The number of seconds to be converted.

    Returns:
        str: The formatted time string representing the converted time.

    Example:
        >>> convert_seconds_to_time(3600)
        converted= 2023-06-29 15:00:00
        '2023-06-29 15:00:00'
        >>> convert_seconds_to_time(86400)
        converted= 2023-06-30 12:00:00
        '2023-06-30 12:00:00'

    """
    a = datetime.utcnow() # Get the current UTC time
    b = a + timedelta(0,seconds) # Add the given number of seconds to the current time
    print("converted=",b.strftime("%Y-%m-%d %H:%M:%S")) # Print the converted time
    return b.strftime("%Y-%m-%d %H:%M:%S") # Return the formatted time string

def get_user_age(date):
    """
    Calculates the age of a user based on their birthdate.

    This function takes a birthdate as input and calculates the user's age in years, months, and days.
    It uses the `datetime.utcnow()` function to get the current date and time and the `relativedelta` class
    from the `dateutil` module to calculate the difference between the current date and the birthdate.

    Args:
        date (datetime): The birthdate of the user.

    Returns:
        dict: A dictionary containing the user's age in years, months, and days.

    Example:
        >>> get_user_age(datetime(1990, 5, 15))
        {'year': 33, 'month': 11, 'day': 14}
        >>> get_user_age(datetime(1985, 10, 3))
        {'year': 37, 'month': 8, 'day': 26}
        
    """
    diff = relativedelta(datetime.utcnow(), date)
    return {"year": diff.years, "month": diff.months, "day": diff.days} 

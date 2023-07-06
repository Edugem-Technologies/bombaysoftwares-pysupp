# pysupp

The bombaysoftwares-pysupp package provides a comprehensive set of utility functions for various operations in Python. These functions simplify common tasks such as date formatting, timestamp conversion, manipulating strings. This package is designed to enhance the functionality of various operations in your Python projects.

## Installation

To use the Date Utils package, you can install it via pip:

```bash
pip install bombaysoftwares_pysupp
```

## Usage

Import the desired functions from the package:

```bash
from bombaysoftwares_pysupp import str_to_bool, format_email
```

## str_to_bool

This Function converts a string to a boolean value. It checks if the stripped and lowercase version of the string is 'true' or 'false'. If it matches 'true', the function returns boolean True. If it matches 'false', the function returns boolean False. Otherwise, it returns None.

```bash

str_to_bool('True')
// Output: True
str_to_bool('False')
// Output: False
str_to_bool('invalid')
// Output: None

```

## format_email

This Function formats an email address. This function removes leading and trailing whitespace, converts the email to lowercase, and returns the formatted email address.

```bash

format_email("  john@example.com ")
// Output: 'john@example.com'
format_email("MARY@example.com")
// Output: 'mary@example.com'
format_email("")
// Output: ''
format_email(None)
// Output: None

```

## get_body_mass_index

This function calculates the Body Mass Index (BMI) based on weight and height.

```bash

get_body_mass_index(70, 170)
// Output: 24.22
get_body_mass_index(80, 180)
// Output: 24.69

```

## Other Functions

The package also includes other useful functions:
- `is_number(string)` : Checks if a string can be converted to an integer.
- `file_name_to_readable_name(file_name)` : Converts a file name to a readable name. It removes file extensions, replaces hyphens with spaces, removes non-alphabetic characters except spaces, capitalizes the first letter, and removes leading/trailing spaces.
- `convert_date_of_birth_to_datetime(date_string)` : Converts a date string in the format '%m/%d/%Y' to a datetime object.
- `get_current_year()` : Retrieves the current year.
- `is_invalid(value)` : Checks if a value is considered invalid. It checks if the string representation of the value matches any of the predefined invalid values: "", None, "None", "null", or "undefined". If a match is found, it returns True; otherwise, it returns False.


For detailed usage and examples, refer to the inline documentation and code samples within each function.

## Author

[Bombay Softwares](https://www.bombaysoftwares.com/)

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more info.
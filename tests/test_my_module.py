from bombaysoftwares_pysupp.utils import str_to_bool, format_email, is_invalid, get_current_year, convert_date_of_birth_to_datetime, generate_otp, convert_time, file_name_to_readable_name, get_body_mass_index, is_number, days_to_seconds, generate_random_string, generate_random_number_string, random_with_n_digits, check_is_not_none_or_empty, format_inr, aadhaar_format, format_datetime, get_time_duration, get_api_key, generate_slug_by_org_id, InputValidation, datetime_from_utc_to_local, encode_jwt_token, decode_jwt_token, encrypt_value, decrypt_hashid, get_pagination_meta, monthdelta, format_time_utc_to_est, get_slug, convert_seconds_to_time, get_user_age
from datetime import datetime, timedelta
import pytest, random, uuid, re, jwt, unittest
from unittest import mock

def test_str_to_bool():
    # Test case 1: input string is "False"
    assert str_to_bool("False") is False

    # Test case 2: input string is "True"
    assert str_to_bool("True") is True

    # Test case 3: input string is "foo"
    assert str_to_bool("foo") is None

def test_format_email():
    # Test case 1: email with leading and trailing whitespace
    assert format_email("  john@example.com ") == 'john@example.com'

    # Test case 2: email with uppercase characters
    assert format_email("MARY@example.com") == 'mary@example.com'

    # Test case 3: empty email
    assert format_email("") == ''

    # Test case 4: None email
    assert format_email(None) is None

def test_is_invalid():
    # Test case 1: empty string
    assert is_invalid("") is True

    # Test case 2: None
    assert is_invalid(None) is True

    # Test case 3: "null"
    assert is_invalid("null") is True

    # Test case 4: "undefined"
    assert is_invalid("undefined") is True

    # Test case 5: valid value
    assert is_invalid("valid") is False

def test_get_current_year(monkeypatch):
    current_year = datetime.now().year
    # Test case 1: get current year
    assert get_current_year() == current_year

def test_convert_date_of_birth_to_datetime():
    expected_date = datetime(1990, 5, 15)
    # Test case 1: valid date string in '%m/%d/%Y' format
    assert convert_date_of_birth_to_datetime('05/15/1990') == expected_date

    # Test case 2: Invalid date string as '%y-%m-%d' format
    assert convert_date_of_birth_to_datetime('2022-01-01') is False

def test_generate_otp():
    otp = generate_otp()
    assert isinstance(otp, int)
    assert otp >= 1000
    assert otp <= 9999

def test_convert_time():
    # Test case 1: 3660 seconds should be converted to 1 hour, 1 minute, and 0 seconds
    assert convert_time(3660) == (1, 1, 0)

    # Test case 2: 12345 seconds should be converted to 3 hours, 25 minutes, and 45 seconds
    assert convert_time(12345) == (3, 25, 45)

def test_file_name_to_readable_name():
    #Test case 1: "my-file-name.txt" should be converted to 'My file name'
    assert file_name_to_readable_name("my-file-name.txt") == 'My file name'

    #Test case 1: "another_example.pdf" should be converted to 'Anotherexample'
    assert file_name_to_readable_name("another_example.pdf") == 'Anotherexample'

def test_get_body_mass_index():
    # Test case 1: weight = 70 kg, height = 170 cm
    # Expected BMI = 70 / ((170 * 170) / 10000) = 24.22
    assert get_body_mass_index(70, 170) == 24.22

    # Test case 2: weight = 80 kg, height = 180 cm
    # Expected BMI = 80 / ((180 * 180) / 10000) = 24.69
    assert get_body_mass_index(80, 180) == 24.69

    # Test case 3: weight = None, height = 160 cm
    # Missing weight should return 0
    assert get_body_mass_index(None, 160) == 0

    # Test case 4: weight = 70 kg, height = None
    # Missing height should return 0
    assert get_body_mass_index(70, None) == 0

    # Test case 5: weight = '70', height = 170 cm
    # Non-integer weight should return 0
    assert get_body_mass_index('70', 170) == 0

    # Test case 6: weight = 70 kg, height = '170'
    # Non-integer height should return 0
    assert get_body_mass_index(70, '170') == 0

def test_is_number():
    # Test case 1: Valid number string '123'
    # Expected: True, as '123' can be converted to an integer
    assert is_number('123') == True

    # Test case 2: Invalid number string 'abc'
    # Expected: False, as 'abc' cannot be converted to an integer
    assert is_number('abc') == False

    # Test case 3: Valid number string '0'
    # Expected: True, as '0' can be converted to an integer
    assert is_number('0') == True

    # Test case 4: Invalid number string '-123'
    # Expected: False, as '-123' cannot be converted to an integer
    assert is_number('-123') == True

    # Test case 5: Valid number string '1000'
    # Expected: True, as '1000' can be converted to an integer
    assert is_number('1000') == True

def test_days_to_seconds():
    # Test case 1: Convert 5 days to seconds
    # Expected: 5 days = 5 * 24 * 60 * 60 seconds = 432000 seconds
    assert days_to_seconds(5) == 432000

    # Test case 2: Convert 0 days to seconds
    # Expected: 0 days = 0 seconds
    assert days_to_seconds(0) == 0

    # Test case 3: Convert 1 day to seconds
    # Expected: 1 day = 24 * 60 * 60 seconds = 86400 seconds
    assert days_to_seconds(1) == 86400

    # Test case 4: Convert 10 days to seconds
    # Expected: 10 days = 10 * 24 * 60 * 60 seconds = 864000 seconds
    assert days_to_seconds(10) == 864000

    # Test case 5: Convert negative number of days to seconds
    # Expected: -5 days = -5 * 24 * 60 * 60 seconds = -432000 seconds
    assert days_to_seconds(-5) == -432000

def test_generate_random_string():
    # Test case 1: Generate a random string of length 10
    # The length of the generated string should be 10
    assert len(generate_random_string(10)) == 10

    # Test case 2: Generate a random string of length 0
    # The length of the generated string should be 0
    assert (generate_random_string(0)) == 0

    # Test case 3: Generate a random string of length 5
    # The length of the generated string should be 5
    assert len(generate_random_string(5)) == 5

    # Test case 4: Generate a random string of length 15
    # The length of the generated string should be 15
    assert len(generate_random_string(15)) == 15

    # Test case 5: Generate a random string of length -5
    # The length of the generated string should be 0 (negative lengths are invalid)
    assert (generate_random_string(-5)) == 0

def test_generate_random_number_string():
    # Test case 1: Generate a random number string of length 10
    # The length of the generated string should be 10
    assert len(generate_random_number_string(10)) == 10

    # Test case 2: Generate a random number string of length 0
    # The length of the generated string should be 0
    assert (generate_random_number_string(0)) == 0

    # Test case 3: Generate a random number string of length 5
    # The length of the generated string should be 5
    assert len(generate_random_number_string(5)) == 5

    # Test case 4: Generate a random number string of length 15
    # The length of the generated string should be 15
    assert len(generate_random_number_string(15)) == 15

    # Test case 5: Generate a random number string of length -5
    # The length of the generated string should be 0 (negative lengths are invalid)
    assert (generate_random_number_string(-5)) == 0

    # Test case 6: Generate a random number string of length 10
    # The generated string should only contain numbers
    assert len(generate_random_number_string(10)) == 10

    # Test case 7: Generate a random number string of length 10
    # The generated string should only contain numbers from 1 to 9
    assert all(char in '123456789' for char in generate_random_number_string(10))

def test_random_with_n_digits():
    # Test case 1: Generate a random number with 3 digits
    # The generated number should have exactly 3 digits
    assert len(str(random_with_n_digits(3))) == 3

    # Test case 2: Generate a random number with 0 digits
    # The generated number should be 0 (no digits)
    assert random_with_n_digits(0) == 0

    # Test case 3: Generate a random number with 5 digits
    # The generated number should have exactly 5 digits
    assert len(str(random_with_n_digits(5))) == 5

    # Test case 4: Generate a random number with 10 digits
    # The generated number should have exactly 10 digits
    assert len(str(random_with_n_digits(10))) == 10

    # Test case 5: Generate a random number with -5 digits
    # The generated number should be 0 (negative digits are invalid)
    assert random_with_n_digits(-5) == 0

def test_check_is_not_none_or_empty():
    # Test case 1: Object is not None or empty (string)
    object = "Hello"
    assert check_is_not_none_or_empty(object) is True

    # Test case 2: Object is None
    object = None
    assert check_is_not_none_or_empty(object) is False

    # Test case 3: Object is an empty string
    object = ""
    assert check_is_not_none_or_empty(object) is False

    # Test case 4: Object is not None or empty (list)
    object = [1, 2, 3]
    assert check_is_not_none_or_empty(object) is True

    # Test case 5: Object is an empty list
    object = []
    assert check_is_not_none_or_empty(object) is False

def test_format_inr():
    # Test case 1: Positive integer
    number = 1234567
    assert format_inr(number) == '₹ 12,34,567'

    # Test case 2: Positive float with two decimal places
    number = 1234567.89
    assert format_inr(number) == '₹ 12,34,567.89'

    # Test case 3: Negative integer
    number = -9876543
    assert format_inr(number) == '₹ -98,76,543'

    # Test case 4: Zero
    number = 0
    assert format_inr(number) == '₹ 0'

    # Test case 5: Large number
    number = 1234567890123456789
    assert format_inr(number) == '₹ 12,34,56,78,90,12,34,56,789'

def test_aadhaar_format():
    # Test case 1: Aadhaar number without spaces
    aadhar_number = "123456789012"
    assert aadhaar_format(aadhar_number) == "1234 5678 9012"

    # Test case 2: Aadhaar number with existing spaces
    aadhar_number = "1234 5678 9012"
    assert aadhaar_format(aadhar_number) == "1234 5678 9012"

    # Test case 3: Aadhaar number with irregular spacing
    aadhar_number = "12  3456  789012"
    assert aadhaar_format(aadhar_number) == "1234 5678 9012"

    # Test case 4: Aadhaar number with leading/trailing spaces
    aadhar_number = " 123456789012 "
    assert aadhaar_format(aadhar_number) == "1234 5678 9012"

def test_format_datetime():
    # Test case 1: Default format
    dt = datetime(2022, 1, 15, 10, 30, 0)
    assert format_datetime(dt) == "2022-01-15 10:30:00"

    # Test case 2: Custom format
    dt = datetime(2022, 1, 15, 10, 30, 0)
    assert format_datetime(dt, "%Y/%m/%d %I:%M %p") == "2022/01/15 10:30 AM"

    # Test case 3: Different datetime object
    dt = datetime(2023, 12, 31, 23, 59, 59)
    assert format_datetime(dt, "%B %d, %Y") == "December 31, 2023"

def test_get_time_duration():
    # Test case 1: Time duration within the same day
    start_date = datetime(2022, 1, 1, 10, 0, 0)
    end_date = datetime(2022, 1, 1, 15, 30, 0)
    assert get_time_duration(start_date, end_date) == "0 days, <br>5 hours, <br>30 minutes"

    # Test case 2: Time duration spanning multiple days
    start_date = datetime(2022, 1, 1, 10, 0, 0)
    end_date = datetime(2022, 1, 3, 12, 30, 0)
    assert get_time_duration(start_date, end_date) == "2 days, <br>2 hours, <br>30 minutes"

    # Test case 3: Time duration with the same start and end date
    start_date = datetime(2022, 1, 1, 10, 0, 0)
    end_date = datetime(2022, 1, 1, 10, 0, 0)
    assert get_time_duration(start_date, end_date) == "0 days, <br>0 hours, <br>0 minutes"

def test_get_api_key():
    # Call the function to get the API key
    api_key = get_api_key()

    # Check if the API key is a UUID object
    assert isinstance(api_key, uuid.UUID)

def test_generate_slug_by_org_id():
    # Test case 1: Valid inputs
    title = 'Hello World'
    org_id = 123
    expected_slug = 'hello-world-123'
    assert generate_slug_by_org_id(title, org_id) == expected_slug

    # Test case 2: Leading/trailing whitespace in title
    title = '  Hello World  '
    org_id = 123
    expected_slug = 'hello-world-123'
    assert generate_slug_by_org_id(title, org_id) == expected_slug

    # Test case 3: Non-string title
    title = 123
    org_id = 123
    expected_slug = '123-123'
    assert generate_slug_by_org_id(title, org_id) == expected_slug

def test_input_validation():
    # Test case 1: Valid string
    string = "HelloWorld123"
    validation_type = InputValidation.ALPHA_NUMERIC
    assert InputValidation.is_valid(string, validation_type) == True

    # Test case 2: Invalid string
    string = "Hello World!"
    validation_type = InputValidation.ALPHA_NUMERIC
    assert InputValidation.is_valid(string, validation_type) == False

    # Test case 3: Valid email
    string = "test@example.com"
    validation_type = InputValidation.EMAIL
    assert InputValidation.is_valid(string, validation_type) == True

    # Test case 4: Invalid email
    string = "invalid-email"
    validation_type = InputValidation.EMAIL
    assert InputValidation.is_valid(string, validation_type) == False

def test_datetime_from_utc_to_local():
    # Test case 1: UTC datetime in the past
    utc_dt = datetime(2022, 3, 15, 10, 30, 0)
    local_dt = datetime_from_utc_to_local(utc_dt)
    expected_local_dt = utc_dt + timedelta(hours=5, minutes=30)  # Assuming the local timezone has a +05:00 offset
    assert local_dt == expected_local_dt

def test_encode_jwt_token():
    data = {"user_id": 123, "role": "admin"}
    JWT_SECRET_KEY = "mysecretkey"

    encoded_token = encode_jwt_token(data, JWT_SECRET_KEY)

    # Verify that the encoded token is not empty
    assert encoded_token

def test_decode_jwt_token():
    data = {"user_id": 123, "role": "admin"}
    JWT_SECRET_KEY = "mysecretkey"

    encoded_token = encode_jwt_token(data, JWT_SECRET_KEY)

    # Verify that the encoded token is not empty
    assert encoded_token

    # Decode the encoded token to verify its content
    decoded_token = decode_jwt_token(encoded_token, JWT_SECRET_KEY)

    # Verify that the decoded token matches the original data
    assert decoded_token == data

def test_encrypt_value():
    hashid_salt = "abcdefghijklmnopqrstuvwxyz"
    # Test case 1: Encrypt a valid value
    value = 12345
    encoded_val = encrypt_value(value, hashid_salt)
    print(encoded_val)
    assert encoded_val != None
    assert isinstance(encoded_val, str)

    # Test case 2: Encrypt an empty value
    value = ''
    encoded_val = encrypt_value(value, hashid_salt)
    print(encoded_val)
    assert encoded_val is None

    # Test case 3: Encrypt a non-numeric value
    value = 'abc'
    encoded_val = encrypt_value(value, hashid_salt)
    print(encoded_val)
    assert encoded_val is None

    # Test case 4: Encrypt a negative value
    value = -12345
    encoded_val = encrypt_value(value, hashid_salt)
    print(encoded_val)
    assert encoded_val is None

    # Test case 5: Encrypt a floating-point value
    value = 123.45
    encoded_val = encrypt_value(value, hashid_salt)
    print(encoded_val)
    assert encoded_val is None

def test_decrypt_hashid():
    # Test case 1: Valid Hashid
    hashval = "ZYQ6xwr50d"
    hashid_salt = "abcdefghijklmnopqrstuvwxyz"
    expected_decoded_val = 12345
    assert decrypt_hashid(hashval, hashid_salt) == expected_decoded_val

    # Test case 2: Invalid Hashid
    hashval = "invalid_hashid"
    hashid_salt = "abcdefghijklmnopqrstuvwxyz"
    assert decrypt_hashid(hashval, hashid_salt) is None

    # Test case 3: Empty Hashid
    hashval = ""
    hashid_salt = "abcdefghijklmnopqrstuvwxyz"
    assert decrypt_hashid(hashval, hashid_salt) is None

    # Test case 4: None Hashid
    hashval = None
    hashid_salt = "abcdefghijklmnopqrstuvwxyz"
    assert decrypt_hashid(hashval, hashid_salt) is None

    # Test case 5: Different Hashid Salt
    hashval = "LX9znW34ab"
    hashid_salt = "different_salt"
    assert decrypt_hashid(hashval, hashid_salt) is None

def test_get_pagination_meta():
    # Test case 1: Pagination with page size provided
    current_page = 2
    page_size = 10
    total_items = 100
    expected_meta = {
        'current_page': 2,
        'page_size': 10,
        'total_items': 100,
        'total_pages': 10,
        'has_next_page': True,
        'has_previous_page': True,
        'next_page': 3,
        'previous_page': 1
    }
    assert get_pagination_meta(current_page, page_size, total_items) == expected_meta

    # Test case 2: Pagination with page size not provided
    current_page = 5
    page_size = None
    total_items = 50
    expected_meta = {
        'current_page': 5,
        'page_size': None,
        'total_items': 50,
        'total_pages': 5,
        'has_next_page': None,
        'has_previous_page': None,
        'next_page': None,
        'previous_page': None
    }
    assert get_pagination_meta(current_page, page_size, total_items) == expected_meta

    # Test case 3: Pagination with empty items
    current_page = 1
    page_size = 10
    total_items = 0
    expected_meta = {
        'current_page': 1,
        'page_size': 10,
        'total_items': 0,
        'total_pages': 0,
        'has_next_page': False,
        'has_previous_page': False,
        'next_page': None,
        'previous_page': None
    }
    assert get_pagination_meta(current_page, page_size, total_items) == expected_meta

def test_monthdelta():
    # Test case 1: Adding 2 months to March 15, 2022
    input_date_1 = datetime(2022, 3, 15)
    delta_months_1 = 2
    expected_result_1 = datetime(2022, 5, 15)
    result_1 = monthdelta(input_date_1, delta_months_1)
    assert result_1 == expected_result_1
    
    # Test case 2: Subtracting 3 months from November 30, 2021
    input_date_2 = datetime(2021, 11, 30)
    delta_months_2 = -3
    expected_result_2 = datetime(2021, 8, 30)
    result_2 = monthdelta(input_date_2, delta_months_2)
    assert result_2 == expected_result_2
    
    # Test case 3: Adding 12 months to February 29, 2020 (leap year)
    input_date_3 = datetime(2020, 2, 29)
    delta_months_3 = 12
    expected_result_3 = datetime(2021, 2, 28)
    result_3 = monthdelta(input_date_3, delta_months_3)
    assert result_3 == expected_result_3
    
    # Test case 4: Subtracting 6 months from January 1, 2023
    input_date_4 = datetime(2023, 1, 1)
    delta_months_4 = -6
    expected_result_4 = datetime(2022, 7, 1)
    result_4 = monthdelta(input_date_4, delta_months_4)
    assert result_4 == expected_result_4

def test_format_time_utc_to_est():
    # Create a UTC datetime object
    utc_time = datetime(2023, 6, 29, 10, 30, 0)

    # Call the function to convert and format the UTC time to EST
    formatted_time = format_time_utc_to_est(utc_time)

def test_get_slug():
    # Mock the time() function to return a fixed timestamp
    with mock.patch("bombaysoftwares_pysupp.utils.time") as mock_time:
        mock_time.return_value = 1629937512  # Fixed timestamp for testing

        # Test case 1: Simple string
        string1 = "Hello, World!"
        expected_slug1 = "hello-world-1629937512"
        assert get_slug(string1) == expected_slug1

        # Test case 2: String with special characters
        string2 = "Let's test this string!"
        expected_slug2 = "let-s-test-this-string-1629937512"
        assert get_slug(string2) == expected_slug2

        # Test case 3: Empty string
        string3 = ""
        expected_slug3 = "1629937512"
        assert get_slug(string3) == expected_slug3

        # Test case 4: String with leading/trailing whitespace
        string4 = "   Python is awesome!   "
        expected_slug4 = "python-is-awesome-1629937512"
        assert get_slug(string4) == expected_slug4

        # Test case 5: String with numbers
        string5 = "Testing 123"
        expected_slug5 = "testing-123-1629937512"
        assert get_slug(string5) == expected_slug5

        # Test case 6: String with uppercase letters
        string6 = "Hello World"
        expected_slug6 = "hello-world-1629937512"
        assert get_slug(string6) == expected_slug6

        # Test case 7: String with non-ASCII characters
        string7 = "Café"
        expected_slug7 = "cafe-1629937512"
        assert get_slug(string7) == expected_slug7

def test_convert_seconds_to_time():
    # Mock the datetime.utcnow() function
    with mock.patch("bombaysoftwares_pysupp.utils.datetime") as mock_dt:
        # Set the fixed UTC time for testing
        mock_dt.utcnow.return_value = datetime(2023, 6, 29, 12, 0, 0)

        # Test case 1: 1 hour (3600 seconds)
        seconds1 = 3600
        expected_time1 = '2023-06-29 13:00:00'
        assert convert_seconds_to_time(seconds1) == expected_time1

        # Test case 2: 1 day (86400 seconds)
        seconds2 = 86400
        expected_time2 = '2023-06-30 12:00:00'
        assert convert_seconds_to_time(seconds2) == expected_time2

def test_get_user_age():
    # Mock the datetime.utcnow() function
    with mock.patch("bombaysoftwares_pysupp.utils.datetime") as mock_dt:
        # Set the fixed UTC time for testing
        mock_dt.utcnow.return_value = datetime(2023, 1, 1)

        # Test case 1: Birthdate in the past
        birthdate1 = datetime(1990, 5, 15)
        expected_age1 = {'year': 32, 'month': 7, 'day': 17}
        assert get_user_age(birthdate1) == expected_age1

        # Test case 2: Birthdate in the past
        birthdate2 = datetime(1985, 10, 3)
        expected_age2 = {'year': 37, 'month': 2, 'day': 29}
        assert get_user_age(birthdate2) == expected_age2
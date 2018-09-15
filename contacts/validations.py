import argparse
import re

email_pattern = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'


def validate_phone_number(val):
    """
    Checks if the parameter contains only numbers and atleast of length 3.
    :param val: input argument
    :return: input argument on valid number
            Exception on invalid number
    """
    if not val.isdigit() or len(val) < 3:
        raise argparse.ArgumentTypeError("Invalid phone number")
    return val


def validate_email(val):
    """
    Checks if the parameter is of valid email address.
    :param val: input argument
    :return: input argument on valid email address
            Exception on invalid email address
    """
    match = re.match(email_pattern, val)
    if not match:
        raise argparse.ArgumentTypeError("Invalid email address")
    return val

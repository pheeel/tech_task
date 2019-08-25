import logging
import random
import string


def get_ip():
    """
    Returns a random string of digits in IPv4 format.
    """
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def get_log_name():
    """
    Returns a random string with 5 symbols in length as a log mask name.
    Only lowercase characters are used.
    """
    length = 5
    chars = string.ascii_lowercase
    return "".join(random.choice(chars) for _ in range(length))


def get_login():
    """
    Returns a random string from 6 to 10 in length as a login.
    Only uppercase characters are used.
    """
    length = random.randint(6, 10)
    chars = string.ascii_uppercase
    return "".join(random.choice(chars) for _ in range(length))


def get_pass():
    """
    Returns a random string from 8 to 12 in length as a password.
    Only uppercase characters and digits are used.
    """
    length = random.randint(8, 12)
    chars = string.digits + string.ascii_letters
    return "".join(random.choice(chars) for _ in range(length))


def generate_log(lines_amount):
    """
    Generates logs in the "logfile.log" file.

    :param lines_amount:  required number of lines in the logfile.
    """
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(filename="logfile.log", level=logging.INFO)

    for i in range(lines_amount):
        logging.info(
            "ID: {}, Log name:{}, IP:{}, Login:{}, Password:{}".format(
                i, get_log_name(), get_ip(), get_login(), get_pass()
            )
        )


generate_log(500)

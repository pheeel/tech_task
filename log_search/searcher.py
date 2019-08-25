import re


def get_log_data_by_id(log_id):
    """
    Finds the line by ID in "logfile.log" as well as -100 and +100 lines relative to this line,
    including the line itself, and writes the result of searching to the "output.py" file.

    :param log_id: (int or str) log ID in logfile.
    """
    range_to_get = 100
    logfile = r"logfile.log"
    result = list()

    with open(logfile) as logs:
        logs = logs.readlines()

    for index, line in enumerate(logs):
        if f"ID: {log_id}" in line:
            result.append(logs[max(0, index - range_to_get):index + (range_to_get + 1)])
            output_file = open("output.txt", "w")
            output_file.write("".join(*result))
            output_file.close()
            break

    if not result:
        raise Exception(f"Log with ID {log_id} was not found.")


def get_credentials_by_ip(ip):
    """
    Searches for an IP in the "logfile.log" file.
    Returns a string with Login and Password of the found IP.

    :param ip: (str) IP in IPv4 format to search for credentials.
    """
    logfile = r"logfile.log"
    with open(logfile) as logs:
        logs = logs.readlines()

    for index, line in enumerate(logs):
        if f"IP:{ip}" in line:
            login = re.search("(Login:)(.*)(?=,)", line)
            password = re.search("(Password:)(.*)", line)
            return f"{login.group()}, {password.group()}"

    raise Exception(f"Log with IP {ip} was not found.")


# The result of calling this function is placed in "output.txt".
get_log_data_by_id("150")

# The search of the IP is carried out in "logfile.log".
AUTH_DATA = get_credentials_by_ip("186.55.35.169")
print(AUTH_DATA)

"""
Validate IP Address
Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.
For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" are valid IP addresses,
while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.
ip = '192.168.0.1'
output: true
ip = '0.0.0.0'
output: true
ip = '123.24.59.99'
output: true
ip = '192.168.123.456'
output: false
"""

"""
Solution:
split by period character. check if the length is 4.
check if every part is integer and between 0 and 255.

Time Complexity: O(N)
Space Complexity: O(1)
"""


def is_valid_ip_part(part):
    for char in part:
        if ord(char) < ord('0') or ord(char) > ord('9'):  # if not char.isdigit():
            return False
    number = int(part)
    if number > 255:
        return False
    if part[0] == '0' and len(part) > 1:
        return False
    return True


def solution(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for i in parts:
        if not is_valid_ip_part(i):
            return False
    return True


def main():
    assert solution('192.168.123.456') == False
    assert solution('192.168.00.456') == False
    assert solution('192.168.0.123') == True


if __name__ == '__main__':
    main()

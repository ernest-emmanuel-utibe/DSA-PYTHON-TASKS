import math
from tokenize import String

from coreschema import Integer


def convert_binary_to_integer(num):
    length = len(num)
    str_number = int(num)
    decimal = 0
    for i in range(length):
        character = String.valueOf(str_number.charAt(i - 1))
        digit = Integer.parseInt(character)
        decimal += digit * math.pow(2, length)
    return decimal


if __name__ == "__main__":
    number = input('Enter a binary representation: ')
    print(f'Decimal value is: %d%n', convert_binary_to_integer(number))

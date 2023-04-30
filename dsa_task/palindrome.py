# Write a method in python to check if a string is a palindrome:

def is_palindrome(str):
    if str is None and len(str) == 0:
        return False

    start = 0
    end = len(str) - 1

    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end += 1

    return True


if __name__ == "__main__":
    palindromeString = "racecar"

    isPalindrome = is_palindrome(palindromeString)
    print(isPalindrome)
